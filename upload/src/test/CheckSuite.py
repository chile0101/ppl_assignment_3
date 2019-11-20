import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):

    # def test_main_func_not_found(self):
    #     input = """
    #                int foo(){

    #                }

    #             """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input,expect,401))

    # def test_main_func_wrong_type(self):
    #     input = """
    #                int main(){
    #                    int x ;
    #                    x = 1;
    #                }

    #             """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input,expect,402))

    # def test_main_func_with_param_invalid(self):
    #     input = """
    #                void main(int x, float y){
    #                }
    #             """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input,expect,403))

    # def test_main_func_redeclared(self):
    #     input = """
    #                void main(){
    #                    x = 1;
    #                }

    #                int main(){
                    
    #                }
    #             """
    #     expect = "Redeclared Function: main"
    #     self.assertTrue(TestChecker.test(input,expect,401))

    # def test_built_in_func_getInt(self):
    #     input = """
    #                int getInt(){
    #                }
    #                void main(){

    #                }
    #             """
    #     expect = "Redeclared Function: getInt"
    #     self.assertTrue(TestChecker.test(input,expect,401))

    def test_built_in_func_putString(self):
        input = """
                int putString(){}
                float putString;
                """
        expect = "Redeclared Function: putString"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_redeclared_two_vardecl(self):
        input = """
                    int x,x;
                """
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input,expect,401))

    # def test_redeclared_two_vardecl(self):
    #     input = """--
    #                 int foo(){}
    #                 float foo(){}
    #             """
    #     expect = "Redeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,402))

   
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

    # def test_true_redeclared_diff_scope(self):
    #     input = """
    #     int x;
    #     float foo(){
    #         int x;
    #     }
    #     float foo1(){
    #         int x;
    #     }
    #     int x;  // for require
    #     """
    #     expect = "Redeclared Variable: x"
    #     self.assertTrue(TestChecker.test(input,expect,403))

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

    # def test_true_undeclared_identifier_leftside(self):
    #     input = """
    #     int z;
    #     float foo(){
    #         int x;
    #         x = z;
    #         y = 1;
            
    #     }"""
    #     expect = "Undeclared Identifier: y"
    #     self.assertTrue(TestChecker.test(input,expect,404))

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

    # def test_undeclared_callExpr_multi_param(self):
    #     input = """
    #     int callFunc(int x){}
    #     int x;
    #     float foo(){
    #         int y;
    #         callFunc(x,y,z);
    #     }"""
    #     expect = "Undeclared Identifier: z"
    #     self.assertTrue(TestChecker.test(input,expect,405))

    # def test_undeclared_vardecl_assign_boolean(self):
    #     input = """
    #     int callFunc(int x){}
    #     float foo(){
    #         x = true;
    #     }"""
    #     expect = "Undeclared Identifier: x"
    #     self.assertTrue(TestChecker.test(input,expect,406))


    # Error
    def test_undeclared_var_after_used(self):
        input = """
        void main(){
            x = 1;
            int x;
        }
        """
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

    # def test_type_mismatch_in_expression_assign_left_float_right_boolean(self):
    #     input = """
    #     int callFunc(int x){}
    #     float foo(){
    #         1.2 = true;
    #     }"""
    #     expect = "Type Mismatch In Expression: BinaryOp(=,FloatLiteral(1.2),BooleanLiteral(true))"
    #     self.assertTrue(TestChecker.test(input,expect,407))

    # def test_type_mismatch_in_expression_assign_left_float_right_string(self):
    #     input = """
    #     int callFunc(int x){}
    #     float foo(){
    #         11 = 11;
    #         12.3 = 12.3;
    #         12.0 = 12;
    #         1.2 = "string";
    #         1 = 12.3
    #     }"""
    #     expect = "Type Mismatch In Expression: BinaryOp(=,FloatLiteral(1.2),StringLiteral(string))"
    #     self.assertTrue(TestChecker.test(input,expect,407))

    # def test_type_mismatch_in_expression_assign_left_float_right_string(self):
    #     input = """
    #     int callFunc(int x){}
    #     float foo(){
    #         11 = 11;
    #         12.3 = 12.3;
    #         12.0 = 12;
    #         1.2 = "string";
    #         1 = 12.3
    #     }"""
    #     expect = "Type Mismatch In Expression: BinaryOp(=,FloatLiteral(1.2),StringLiteral(string))"
    #     self.assertTrue(TestChecker.test(input,expect,407))

    # def test_type_mismatch_in_expression_add(self):
    #     input = """
    #     int callFunc(int x){}
    #     float foo(){
    #        int x;
    #        x = 1 + 1;
    #        float y ;
    #        y = 1 + 1.1;
    #        y = 1.012 + 123;
    #        y = 134.234 + 134.146;
    #        x = 1.1 + true;  // For error
    #        y = true;   // For error
    #     }"""
    #     expect = "Type Mismatch In Expression: BinaryOp(+,FloatLiteral(1.1),BooleanLiteral(true))"
    #     self.assertTrue(TestChecker.test(input,expect,407))

    # def test_type_mismatch_in_expression_sub(self):
    #     input = """
    #     int callFunc(int x){}
    #     float foo(){
    #        int x;
    #        x = 1 - 1;
    #        float y ;
    #        y = 1 - 1.1;
    #        y = 1.012 - 123;
    #        y = 134.234 - 134.146;
    #        x = 1.1 - true;  // For error
    #        y = true;   // For error
    #     }"""
    #     expect = "Type Mismatch In Expression: BinaryOp(-,FloatLiteral(1.1),BooleanLiteral(true))"
    #     self.assertTrue(TestChecker.test(input,expect,408))

    # def test_type_mismatch_in_expression_muti(self):
    #     input = """
    #     int callFunc(int x){}
    #     float foo(){
    #        int x;
    #        x = 1 * 1;
    #        float y ;
    #        y = 1 * 1.1;
    #        y = 1.012 * 123;
    #        y = 134.234 * 134.146;
    #        x = 1 * -123;  
    #        x = 1 * 0;  
    #        x = "string" * 12;  // For errr
        
    #     }"""
    #     expect = "Type Mismatch In Expression: BinaryOp(*,StringLiteral(string),IntLiteral(12))"
    #     self.assertTrue(TestChecker.test(input,expect,408))

    # def test_type_mismatch_in_expression_div(self):
    #     input = """
    #     int callFunc(int x){}
    #     float foo(){
    #        int x;
    #        x = 1 / 1;
    #        float y ;
    #        y = 1 / 1.1;
    #        y = 1.012 / 123;
    #        y = 134.234 / 134.146;
    #        x = 1 / -123;  
    #        x = 1 / 0;  // Chua check error
    #        x = true / 12;  // For errr
        
    #     }"""
    #     expect = "Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(true),IntLiteral(12))"
    #     self.assertTrue(TestChecker.test(input,expect,408))

    # def test_type_mismatch_in_expression_combined_operators_simple(self):
    #     input = """
    #     int callFunc(int x){}
    #     float foo(){
    #        float x;
    #        x = 123 * 12 + 15 - 67/14;
        
    #     }"""
    #     expect = "Type Mismatch In Expression: BinaryOp(/,BooleanLiteral(true),IntLiteral(12))"
    #     self.assertTrue(TestChecker.test(input,expect,408))


    # def test_type_mismatch_in_expression_combined_operators_complex(self):
    #     input = """
    #     int callFunc(int x){}
    #     float foo(){
    #        float x;
    #        x = 123 * 12 + 15 - 67/14;
    #        x = 134/12 - 42 * 09/12 + 145;
    #        int y;
    #         y = 1/32 + 123 - 153.13;
        
    #     }"""
    #     expect = "Type Mismatch In Expression: BinaryOp(=,Id(y),BinaryOp(-,BinaryOp(+,BinaryOp(/,IntLiteral(1),IntLiteral(32)),IntLiteral(123)),FloatLiteral(153.13)))"
    #     self.assertTrue(TestChecker.test(input,expect,409))

    # def test_type_mismatch_in_expression_compare_greater(self):
    #     input = """
        
    #     int foo(){
    #         int x ;
    #         x = 1 > 0;
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(=,Id(x),BinaryOp(>,IntLiteral(1),IntLiteral(0)))"
    #     self.assertTrue(TestChecker.test(input,expect,410))


    # def test_type_mismatch_in_expression_compare_greater_assign(self):
    #     input = """
        
    #     int foo(){
    #         string x ;
    #         x = 123 >= 111 + 1;
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(=,Id(x),BinaryOp(>=,IntLiteral(123),BinaryOp(+,IntLiteral(111),IntLiteral(1))))"
    #     self.assertTrue(TestChecker.test(input,expect,410))
   

    # def test_true_type_mismatch_in_expression_compare_less(self):
    #     input = """
        
    #     int foo(){
    #         boolean x ;
    #         x = 123 < 111 + 1;
    #         float y;
    #         y = -134 < true;  // For error
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(<,UnaryOp(-,IntLiteral(134)),BooleanLiteral(true))"
    #     self.assertTrue(TestChecker.test(input,expect,410))


    # def test_true_type_mismatch_in_expression_compare_less_assign(self):
    #     input = """
        
    #     int foo(){
    #         boolean x ;
    #         x = 123 - 13 <= 111 + 1;
    #         x = 26 + 12 + 14/14 -12*8  <= 41;
    #         float y;
    #         y = -134 <= "abc";  // For error
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(<=,UnaryOp(-,IntLiteral(134)),StringLiteral(abc))"
    #     self.assertTrue(TestChecker.test(input,expect,410))

    # def test_type_mismatch_in_expression_operator_and(self):
    #     input = """
        
    #     int foo(){
    #         boolean x ;
    #         x = true && false;
    #         x = 123 and -123;
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(=,Id(x),IntLiteral(123))"
    #     self.assertTrue(TestChecker.test(input,expect,410))

    # def test_type_mismatch_in_expression_operator_and_combine(self):
    #     input = """
        
    #     int foo(){
    #         boolean x ;
    #         x = true && true && false;
    #         x = false && "true" ;
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(&&,BooleanLiteral(false),StringLiteral(true))"
    #     self.assertTrue(TestChecker.test(input,expect,410))


    # def test_true_type_mismatch_in_expression_operator_assign_assign_type(self):
    #     input = """
    #         int foo(){
    #             boolean status;
    #             status = 1 == 1;
    #             status = true == true;
    #             string bool;
    #             bool = "str" == "str";
    #         }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(==,StringLiteral(str),StringLiteral(str))"
    #     self.assertTrue(TestChecker.test(input,expect,410))

    # def test_true_type_mismatch_in_expression_operator_assign_assign_invalid(self):
    #     input = """
    #         int foo(){
    #             boolean status;
    #             status = 1 == 1;
    #             status = true == true;
    #             boolean bool;
    #             bool = "str" == "str";  // For error
    #         }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(==,StringLiteral(str),StringLiteral(str))"
    #     self.assertTrue(TestChecker.test(input,expect,410))

    # def test_true_type_mismatch_in_expression_operator_assign_assign_complex(self):
    #     input = """
    #         int foo(){
    #             boolean status;
    #             status = 1 == 1;
    #             status = true == true == false == 1 + 1 >= 12 ;
    #             status = 1.1 == 1.1; // for error
              
    #         }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(==,FloatLiteral(1.1),FloatLiteral(1.1))"
    #     self.assertTrue(TestChecker.test(input,expect,410))

    # def test_type_mismatch_in_expression_operator_not_equal(self):
    #     input = """
    #         int foo(){
    #             boolean status;
    #             status = 1 != 1;
    #             status = true != true != false != 1 + 1 >= 12 ;
    #             status = 1.1 != 1.1; // for error
              
    #         }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(!=,FloatLiteral(1.1),FloatLiteral(1.1))"
    #     self.assertTrue(TestChecker.test(input,expect,410))


    # def test_true_type_mismatch_in_expression_operator_and_combine_complex(self):
    #     input = """
        
    #        int foo(){
    #         boolean x ;
    #         x = true && true && -123 == -123 && 1 == 1 && true == true;
    #         x = false && "false" ; // For error
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(&&,BooleanLiteral(false),StringLiteral(false))"
    #     self.assertTrue(TestChecker.test(input,expect,410))


    # def test_true_type_mismatch_in_expression_operator_or_simple(self):
    #     input = """
        
    #        int foo(){
    #         boolean x ;
    #         x = true || true ;
    #         int y ;
    #         y = true || false;
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(=,Id(y),BinaryOp(||,BooleanLiteral(true),BooleanLiteral(false)))"
    #     self.assertTrue(TestChecker.test(input,expect,410))

    # def test_true_type_mismatch_in_expression_operator_or_combine(self):
    #     input = """
        
    #        int foo(){
    #         int count;
    #         boolean x ;
    #         x = true || true || 1 == 1 || true == false || count + 1 == 12 ;
    #         boolean z ;
    #         z = 1 - 1 + 134 || "chi" == "chi" || true;
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(==,StringLiteral(chi),StringLiteral(chi))"
    #     self.assertTrue(TestChecker.test(input,expect,410))

    # def test_true_type_mismatch_in_expression_operator_mod(self):
    #     input = """
        
    #         int foo(){
    #         int n;
    #         n = n%12;
    #         n = 123%1.1; // For error
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(%,IntLiteral(123),FloatLiteral(1.1))"
    #     self.assertTrue(TestChecker.test(input,expect,410))

    # def test_true_type_mismatch_in_expression_operator_mod_complex(self):
    #     input = """
        
    #         int foo(){
    #         int n;
    #         int sum;
    #         sum = 123;
    #         n = n%12;
    #         n = sum%(1+1); // For error
    #         n = sum%(1+1)/12.1; // For error
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(=,Id(n),BinaryOp(/,BinaryOp(%,Id(sum),BinaryOp(+,IntLiteral(1),IntLiteral(1))),FloatLiteral(12.1)))"
    #     self.assertTrue(TestChecker.test(input,expect,410))


    # def test_if_condition_is_boolean(self):
    #     input = """
    #         int x;
    #         void main(){
    #             if(true){}else{}
    #             if(false){}else{}
    #             if(1){}else{}
    #         }
    #     """
    #     expect = "Type Mismatch In Statement: If(IntLiteral(1),Block([]),Block([]))"
    #     self.assertTrue(TestChecker.test(input,expect,410))

    # def test_if_condition_is_boolean_expresion(self):
    #     input = """
    #         int x;
    #         void main(){
    #             if(true){}else{}
    #             if(false){}else{}
    #             if(1==1){}else{}
    #             if(true == true){}else{}

    #             boolean bool ;
    #             bool = x >= 4 ;  // error undeclared x

    #             int x = 5;
    #             if(true){}else{}
    #             if(1 + 2){}else{}
    #         }
    #     """
    #     expect = "Type Mismatch In Statement: If(IntLiteral(1),Block([]),Block([]))"
    #     self.assertTrue(TestChecker.test(input,expect,410))


    # def test_undeclared_in_if_condition(self):
    #     input = """
    #         void main(){
    #             if(true){}else{}
    #             if(false){}else{}
    #             if(1 == 1){}else{}
    #             if(have){}else{}
    #         }
    #     """
    #     expect = "Undeclared Identifier: have"
    #     self.assertTrue(TestChecker.test(input,expect,410))

    # def test_undeclared_in_if_thenStmt(self):
    #     input = """
    #         void main(){
    #             boolean have = true;
    #             if(have){}else{
    #                 sum = 123;
    #             }
    #         }
    #     """
    #     expect = "Undeclared Identifier: have"
    #     self.assertTrue(TestChecker.test(input,expect,410))

    # def test_undeclared_in_if_elseStmt(self):
    #     input = """
    #         void main(){
    #             boolean have = true;
    #             if(have){}else{
    #                 sum = 123;
    #             }
    #         }
    #     """
    #     expect = "Undeclared Identifier: have"
    #     self.assertTrue(TestChecker.test(input,expect,410))
















    

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
    