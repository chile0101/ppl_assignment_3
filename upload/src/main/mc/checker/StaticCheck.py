
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
            
    
    def __init__(self,ast):
        self.ast = ast

    def printC(self,c):
        for i in c:
            print('ccccccccccccccc',i.name)


    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def checkRedeclared(self, sym, kind, env):
        if self.lookup(sym.name, env, lambda x: x.name):
            raise Redeclared(kind, sym.name)
        else :
            return sym

    def visitProgram(self, ast, c): 
        for i in ast.decl:
            print('>>>>> decl: ',i)
        res = reduce(lambda x,y: [self.visit(y,x+c)] + x,ast.decl,[])

        return res

    def visitVarDecl(self, ast, c):
        symVar = Symbol(ast.variable, ast.varType)
        return self.checkRedeclared(symVar, Variable(), c)

        
    def visitFuncDecl(self,ast, c): 
        symFunc = Symbol(ast.name.name,MType([x.varType for x in ast.param],ast.returnType))
        self.checkRedeclared(symFunc, Function(), c)
        listPara  = reduce(lambda x,y:x + [self.checkRedeclared(Symbol(y.variable,y.varType),Parameter(),x)],ast.param,[])
        
        listLocal = []
        for i in ast.body.member:
            if type(i) is VarDecl:
                listLocal = reduce(lambda x,y:x+ [self.checkRedeclared(Symbol(y.variable,y.varType),Variable(),x)],[i],listPara)     
            #if type(i) is CallExpr:
            else:   
                self.visit(i,listLocal + c)
            

        return Symbol(ast.name.name,MType([x.varType for x in ast.param],ast.returnType))

    def visitBinaryOp(self,ast,c):
        left = self.visit(ast.left,c)
        right = self.visit(ast.right,c)

        if (ast.op == "+" or ast.op == "-" or ast.op == "*" or ast.op == "/" ):
            if (isinstance(left,IntType)) and (isinstance(right,IntType)):
                return IntType()
            elif (isinstance(left,IntType)) and (isinstance(right,FloatType)) or (isinstance(left,FloatType)) and (isinstance(right,IntType)) or (isinstance(left,FloatType)) and (isinstance(right,FloatType)):
                return FloatType()
            raise TypeMismatchInExpression(ast)
        elif (ast.op == "<" or ast.op == ">" or ast.op == "<=" or ast.op == ">=" ):
            if (isinstance(left,IntType)) and (isinstance(right,IntType)) or (isinstance(left,IntType)) and (isinstance(right,FloatType)) or (type(left) is FloatType()) and (isinstance(right,IntType)) or (type(left) is FloatType()) and (isinstance(right,FloatType)):
                return BoolType()
            raise TypeMismatchInExpression(ast)
        elif(ast.op == "==" or ast.op == "!="):
            if (type(left) is IntType and type(right) is IntType) and (type(left) is BoolType and type(right) is BoolType):
                return BoolType()
            raise TypeMismatchInExpression(ast)

        elif (ast.op == "="):
            if( type(left) is FloatType and type(right) is IntType or FloatType):
                return FloatType()
            elif(type(left) is IntType and type(right) is IntType):
                return IntType()
            elif(type(left) is BoolType and type(right) is BoolType):
                return BoolType()
            elif(type(left) is StringType and type(right) is StringType):
                return StringType()
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
        print("resssssssssss",res)
        if res is None: # miss check type
            raise Undeclared(Function(),ast.method.name)
        
        elif len(res.mtype.partype) != len(at) or any(type(a)!=type(b) for a,b in zip(at,res.mtype.partype)):
            raise TypeMismatchInExpression(ast)
        else:
            return res.mtype.rettype

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


    def visitIf(self,ast,c):
        condition = self.visit(ast.expr,c)
        if not type(condition) is BoolType:
            raise TypeMismatchInStatement(ast)