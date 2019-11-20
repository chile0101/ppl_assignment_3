import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):

    def test_redeclared_two_vardecl(self):
        input = """
                    int x,x;
                """
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_redeclared_two_vardecl(self):
        input = """
                    int foo(){}
                    float foo(){}
                """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,402))

   
    # def test_redeclared_param_and_variable_of_func(self):
    #     input = """
    #     int x,y;
    #     float foo(int foo){
    #         int foo;
    #     }"""
    #     expect = "Redeclared Variable: foo"
    #     self.assertTrue(TestChecker.test(input,expect,403))

    # def test_true_redeclared_diff_scope(self):
    #     input = """
    #     int x;
    #     float foo(int para){
    #         int x;
    #         int para;
    #     }"""
    #     expect = "Redeclared Variable: para"
    #     self.assertTrue(TestChecker.test(input,expect,403))

    def test_true_redeclared_diff_scope(self):
        input = """
        int x;
        float foo(){
            int x;
        }
        float foo1(){
            int x;
        }
        int x;  // for require
        """
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input,expect,403))

    # def test_undeclared_identifier(self):
    #     input = """
    #     float foo(){
    #         z = 1;
    #     }"""
    #     expect = "Undeclared Identifier: z"
    #     self.assertTrue(TestChecker.test(input,expect,404))

    # def test_true_undeclared_identifier_outside_func(self):
    #     input = """
    #     int z;
    #     float foo(){
    #         z = 1;
    #         x = z;  // for require
    #     }"""
    #     expect = "Undeclared Identifier: x"
    #     self.assertTrue(TestChecker.test(input,expect,404))

    def test_true_undeclared_identifier_leftside(self):
        input = """
        int z;
        float foo(){
            int x;
            x = z;
            y = 1;
            
        }"""
        expect = "Undeclared Identifier: y"
        self.assertTrue(TestChecker.test(input,expect,404))

    # def test_undeclared_callExpr_func(self):
    #     input = """
    
    #     float foo(){
    #         int z;
    #         callFunc(z);
    #     }"""
    #     expect = "Undeclared Function: callFunc"
    #     self.assertTrue(TestChecker.test(input,expect,404))
        
    # def test_undeclared_callExpr_param(self):
    #     input = """
    
    #     int callFunc(int x){}
    #     float foo(){
    #         int z;
    #         callFunc(a);
    #     }"""
    #     expect = "Undeclared Identifier: a"
    #     self.assertTrue(TestChecker.test(input,expect,405))

    def test_undeclared_callExpr_multi_param(self):
        input = """
        int callFunc(int x){}
        int x;
        float foo(){
            int y;
            callFunc(x,y,z);
        }"""
        expect = "Undeclared Identifier: z"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_undeclared_vardecl_assign_boolean(self):
        input = """
        int callFunc(int x){}
        float foo(){
            x = true;
        }"""
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input,expect,406))

    # def test_type_mismatch_in_expression_add_boolean_interger(self):
    #     input = """
    #     int callFunc(int x){}
    #     float foo(){
    #         1 + 1.1;
    #         true + 2;
    #         false - 1;
    #         "str" + 123;
            
    #     }"""
    #     expect = "Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(true),IntLiteral(2))"
    #     self.assertTrue(TestChecker.test(input,expect,407))

    # def test_type_mismatch_in_expression_add_boolean_interger(self):
    #     input = """
    #     int callFunc(int x){}
    #     float foo(){
    #         1 + 1.1;
    #         true + 2;
    #         false - 1;
    #         "str" + 123;
            
    #     }"""
    #     expect = "Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(true),IntLiteral(2))"
    #     self.assertTrue(TestChecker.test(input,expect,407))

    def test_type_mismatch_in_expression_assign_left_float_right_boolean(self):
        input = """
        int callFunc(int x){}
        float foo(){
            
            float x;
            x = 1;
            x = 1.123;
            1.1 = true;  // For require
            1.1 = "str"  // Fro require

            
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(true),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,407))

    # def test_type_mismatch_in_expression_call_func_mismatch_param(self):
    #     input = """
    #     int push(int x){}
    #     int foo(int x){
    
    #         push();
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: CallExpr(Id(push),[])"
    #     self.assertTrue(TestChecker.test(input,expect,408))

   














    

#   test("Redeclare params") {

#     val input = "int a; float x(int b, float b){}"
#     val expected = "Redeclared Parameter: b"
#     assert(checkCkr(input, expected, 405))

#   }

#   test("Redeclare Variable inside a function body") {

#     val input = "int a; float b(){int x, x;}"
#     val expected = "Redeclared Variable: x"
#     assert(checkCkr(input, expected, 406))

#   }
#   test("Redeclare Variable") {

#     val input = "int a; float a;"
#     val expected = "Redeclared Variable: a"
#     assert(checkCkr(input, expected, 407))

#   }
#   test("New Redeclare Variable") {

#     val input = "int a,a;"
#     val expected = "Redeclared Variable: a"
#     assert(checkCkr(input, expected, 408))

#   }
#   test("Another Redeclared Variable inside a function body") {

#     val input = "int a; float b(){int x; boolean x;}"
#     val expected = "Redeclared Variable: x"
#     assert(checkCkr(input, expected, 409))

#   }


    
    # def test_undeclared_function_use_ast(self):
    #     """Simple program: int main() {} """
    #     input = Program([FuncDecl(Id("main"),[],IntType(),Block([
    #         CallExpr(Id("foo"),[])]))])
    #     expect = "Undeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,403))
    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],IntType(),Block([
    #                 CallExpr(Id("putIntLn"),[
    #                     CallExpr(Id("getInt"),[IntLiteral(4)])
    #                     ])]))])
    #     expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(4)])"
    #     self.assertTrue(TestChecker.test(input,expect,404))
    # def test_diff_numofparam_stmt_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],IntType(),Block([
    #                 CallExpr(Id("putIntLn"),[])]))])
    #     expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),[])"
    #     self.assertTrue(TestChecker.test(input,expect,405))
    