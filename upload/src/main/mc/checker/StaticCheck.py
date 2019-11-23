
"""
 * @author : Le Van Chi 
 MSSV      : 1510289
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce


class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype
    def __str__(self):
        return 'MType(['+','.join(str(i) for i in self.partype)+']'+','+str(self.rettype)+')'

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
    def __str__(self):
        return 'Symbol('+self.name+','+str(self.mtype)+')'

class StaticChecker(BaseVisitor,Utils):

    global_envi = [
        Symbol("getInt", MType([], IntType())),
        Symbol("putInt", MType([IntType()], VoidType())),
        Symbol("putIntLn", MType([IntType()], VoidType())),
        Symbol("getFloat", MType([], FloatType())),
        Symbol("putFloat", MType([FloatType()], VoidType())),
        Symbol("putFloatLn", MType([FloatType()], VoidType())),
        Symbol("putBool", MType([BoolType()], VoidType())),
        Symbol("putBoolLn", MType([BoolType()], VoidType())),
        Symbol("putString", MType([StringType()], VoidType())),
        Symbol("putStringLn", MType([StringType()], VoidType())),
        Symbol("putLn", MType([], VoidType()))
    ]

    curFunc = FuncDecl("",[],VoidType(),[])
    funDeclaredNotCalled = []
    ok = 0
            
    def __init__(self,ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def checkRedeclared(self, sym, kind, env):
        if self.lookup(sym.name, env, lambda x: x.name):
            raise Redeclared(kind, sym.name)
        else :
            return sym

    def visitProgram(self, ast, c): 
        self.funDeclaredNotCalled = []

        res = reduce(lambda x,y: [self.visit(y,x+c)] + x,ast.decl,[])

        findMain = self.lookup("main",res,lambda x:x.name)
        if (findMain is None) or (not isinstance(findMain.mtype,MType)):
            raise NoEntryPoint()

        if self.funDeclaredNotCalled:
            raise UnreachableFunction(self.funDeclaredNotCalled[0])

        return res

    def visitVarDecl(self, ast, c):
        symVar = Symbol(ast.variable, ast.varType)
        return self.checkRedeclared(symVar, Variable(), c)

    
    def checkFuncNotVoidReturnEmpty(self,returnTypeFunc, returnTypeReturn):
        if ( not type (returnTypeFunc) is VoidType) and (returnTypeReturn == []):
            return True
        else:
            return False

    def visitFuncDecl(self,ast, c): 
        self.curFunc = ast
        if ast.name.name != 'main':
            self.funDeclaredNotCalled.append(ast.name.name)

        flag_return=0
        flag_break=0
        flag_continue=0
        symFunc = Symbol(ast.name.name,MType([x.varType for x in ast.param],ast.returnType))
        self.checkRedeclared(symFunc, Function(), c)
        listParaOfFunc  = reduce(lambda x,y:x + [self.checkRedeclared(Symbol(y.variable,y.varType),Parameter(),x)],ast.param,[])
        
        listVarInBody = []
        listVarInBlock = listParaOfFunc

        for i in ast.body.member:
            if(type(i) is VarDecl):
                listVarInBody.append(i)
                listVarInBlock =reduce(lambda x,y : x+ [self.checkRedeclared(Symbol(y.variable,y.varType),Variable(),x)],listVarInBody,listParaOfFunc)      
            elif (type(i) is Return): 
                
                if (not self.checkFuncNotVoidReturnEmpty(self.curFunc.returnType,i.expr)):
                    self.visit(i,listVarInBlock + c)
                    flag_return += 1
            elif (type(i) is Break):
                flag_break += 1
            elif (type(i) is Continue):  
                flag_continue += 1
            else:
                self.visit(i,listVarInBlock + c)
        if(not type( ast.returnType) is VoidType):
            if flag_return == 0:
                raise FunctionNotReturn(ast.name.name)
        if flag_break >= 1:
            raise BreakNotInLoop()
        if flag_continue>=1:
            raise ContinueNotInLoop()
        

        return symFunc

    def visitBinaryOp(self,ast,c):
        left = self.visit(ast.left,c)
        right = self.visit(ast.right,c)

    
        if (ast.op == "+" or ast.op == "-" or ast.op == "*" or ast.op == "/" ):
            
            if (isinstance(left,IntType)) and (isinstance(right,IntType)):
                return IntType()
            elif (isinstance(left,IntType)) and (isinstance(right,FloatType)) or (isinstance(left,FloatType)) and (isinstance(right,IntType)) or (isinstance(left,FloatType)) and (isinstance(right,FloatType)):
                return FloatType()
            else:
                raise TypeMismatchInExpression(ast)
        elif (ast.op == "<" or ast.op == ">" or ast.op == "<=" or ast.op == ">=" ):
            if (isinstance(left,IntType)) and (isinstance(right,IntType)) or (isinstance(left,IntType)) and (isinstance(right,FloatType)) or (type(left) is FloatType()) and (isinstance(right,IntType)) or (type(left) is FloatType()) and (isinstance(right,FloatType)):
                return BoolType()
            raise TypeMismatchInExpression(ast)
        elif(ast.op == "==" or ast.op == "!="):
            if (type(left) is IntType and type(right) is IntType) or (type(left) is BoolType and type(right) is BoolType):
                return BoolType()
            raise TypeMismatchInExpression(ast)

        elif (ast.op == "="):
           
            if(not type(ast.left) is Id) and (not type(ast.left) is ArrayCell):
                raise NotLeftValue(ast.left)
        
            if( type(left) is FloatType and type(right) is IntType or type(left) is FloatType and type(right) is FloatType):
                return FloatType()
            elif(type(left) is IntType and type(right) is IntType):
                return IntType()
            elif(type(left) is BoolType and type(right) is BoolType):
                return BoolType()
            elif(type(left) is StringType and type(right) is StringType):
                return StringType()
            else: 
                raise TypeMismatchInExpression(ast)
        elif (ast.op == "&&" or ast.op == "||"):
            if(type(left) is BoolType and type(right) is BoolType):
                 return BoolType()
            raise TypeMismatchInExpression(ast)
        elif (ast.op == "%"):
            if(type(left) is IntType and type(right) is IntType):
                return IntType()
            raise TypeMismatchInExpression(ast)
        raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self,ast,c):
        exp=self.visit(ast.body,c)
        if(ast.op == "-"):
            if(type(exp) is IntType):
                return IntType()
            elif(type(exp) is FloatType):
                return FloatType()
            raise TypeMismatchInExpression(ast)
        elif(ast.op == "!"):
            if(type(exp) is BoolType):
                return BoolType()
            raise TypeMismatchInExpression(ast)
        raise TypeMismatchInExpression(ast)
    

    def visitCallExpr(self,ast,c): 
    
        at = [self.visit(x,c) for x in ast.param]
        res = self.lookup(ast.method.name,c,lambda x:x.name)
      
        if res is None: # miss check type
            raise Undeclared(Function(),ast.method.name)
        
        elif len(res.mtype.partype) != len(at) or any(type(a)!=type(b) for a,b in zip(at,res.mtype.partype)):
            raise TypeMismatchInExpression(ast)
        
        self.funDeclaredNotCalled.remove(ast.method.name)

    def visitId(self,ast,c):
    
        temp=self.lookup(ast.name,c,lambda x:x.name)
        if (temp is None) or type(temp.mtype) is MType:
            raise Undeclared(Identifier(),ast.name)
        else:
            return temp.mtype

    def visitIntLiteral(self,ast, c): 
        return IntType()
    def visitFloatLiteral(self,ast,c):
        return FloatType()
    def visitBooleanLiteral(self,ast, c): 
        return BoolType()
    def visitStringLiteral(self,ast, c): 
        return StringType()

    def visitBlock(self,ast,c):  
        [self.visit(x,c) for x in ast.member]

    def visitIf(self,ast,c):
        expr = self.visit(ast.expr,c)

        if not type(expr) is BoolType:
            raise TypeMismatchInStatement(ast)
        if ast.elseStmt:
            elseStmt = self.visit(ast.elseStmt,c)
            flag = 0;
            if ast.elseStmt.member:
                for x in ast.elseStmt.member:
                    if (type(x) is Return): 
                        if (not self.checkFuncNotVoidReturnEmpty(self.curFunc.returnType,x.expr)):  
                            flag = 1
                            break
                    elif (self.ok==0) and (type(x) is Break):
                        raise BreakNotInLoop()
                    elif (self.ok==0) and (type(x) is Continue):
                        raise ContinueNotInLoop()
            # if flag == 0:
            #     raise FunctionNotReturn(self.curFunc.name.name)

        if ast.thenStmt:
            thenStmt = self.visit(ast.thenStmt,c)
            flag = 0;
            for x in ast.thenStmt.member:
                if (type(x) is Return): 
                    if (not self.checkFuncNotVoidReturnEmpty(self.curFunc.returnType,x.expr)):
                        flag = 1
                        break
                elif (self.ok==0) and (type(x) is Break):
                    raise BreakNotInLoop()
                elif (self.ok==0) and (type(x) is Continue):
                    raise ContinueNotInLoop()
            # if flag == 0:
            #     raise FunctionNotReturn(self.curFunc.name.name)

    def visitFor(self,ast,c):
        self.ok=1
        expr1 = self.visit(ast.expr1,c)
        expr2 = self.visit(ast.expr2,c)
        expr3 = self.visit(ast.expr3,c)

        if ( type(expr1) is IntType and type(expr2) is BoolType and type(expr3) is IntType):
            res=[self.visit(x,c) for x in ast.loop.member]
        else:
            raise TypeMismatchInStatement(ast)

        self.ok=0
    def visitDowhile(self,ast,c):
        self.ok=1
        exp = self.visit(ast.exp,c)
        if not type(exp) is BoolType:
            raise TypeMismatchInStatement(ast)
        
        self.ok==0
    def checkMatchOfFuncAndReturnType(self,x,y):
        if isinstance(x,IntType) and isinstance(y,IntType) :
            return True
        elif (isinstance(x,FloatType) and isinstance(y,FloatType)) or (isinstance(x,FloatType) and isinstance(y,IntType)) :
            return True
        elif isinstance(x,BoolType) and isinstance(y,BoolType):
            return True
        elif isinstance(x,StringType) and isinstance(y,StringType):
            return True
        elif (isinstance(x,ArrayType) and isinstance(y,ArrayType)) or (isinstance(x,ArrayPointerType) and isinstance(y,ArrayPointerType)) or (isinstance(x,ArrayPointerType) and isinstance(y,ArrayType)) :
            if x.eleType == y.eleType:
                return True
            else:
                return False
        else:
            return False

    def visitReturn(self,ast,c):
       
        funcType = self.curFunc.returnType
        
        if ast.expr:
            if type(funcType) is VoidType:
                raise TypeMismatchInStatement(ast)
            elif( (not type(funcType) is VoidType) and (not ast.expr)):
                raise TypeMismatchInStatement(ast)
            expr = self.visit(ast.expr,c)
            if (not self.checkMatchOfFuncAndReturnType(funcType,expr)): 
                raise TypeMismatchInStatement(ast)
            
    def visitBreak(self,ast,c):
        return;
    def visitContinue(self,ast,c):
        return;
    def visitArrayCell(self,ast,c):
        return;