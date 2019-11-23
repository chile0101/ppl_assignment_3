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

    # def test_main_func_wrong_type_not_raise_error(self):
    #     input = """
    #                int main(){
    #                    x = 1;  // For error
    #                }

    #             """
    #     expect = "Undeclared Identifier: x"
    #     self.assertTrue(TestChecker.test(input,expect,402))

    # def test_main_func_with_param_invalid_not_raise_error(self):
    #     input = """
    #                void main(int x, float y){
    #                    z = 1;
    #                }
    #             """
    #     expect = "Undeclared Identifier: z"
    #     self.assertTrue(TestChecker.test(input,expect,403))

    # def test_main_func_redeclared(self):
    #     input = """
    #                void main(){
    #                }

    #                int main(){
                    
    #                }
    #             """
    #     expect = "Redeclared Function: main"
    #     self.assertTrue(TestChecker.test(input,expect,404))

    # def test_built_in_func_getInt(self):
    #     input = """
    #                int getInt(){
    #                }
    #                void main(){

    #                }
    #             """
    #     expect = "Redeclared Function: getInt"
    #     self.assertTrue(TestChecker.test(input,expect,405))

    # def test_built_in_func_putString(self):
    #     input = """
    #             int putString(){}
    #             float putString;
    #             """
    #     expect = "Redeclared Function: putString"
    #     self.assertTrue(TestChecker.test(input,expect,406))

    # def test_redeclared_two_vardecl(self):
    #     input = """
    #                 int x,x;
    #             """
    #     expect = "Redeclared Variable: x"
    #     self.assertTrue(TestChecker.test(input,expect,407))

    # def test_redeclared_two_func(self):
    #     input = """
    #                 void main(){

    #                 }
    #                 int foo(){}
    #                 float foo(){}
    #             """
    #     expect = "Redeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,408))

   
    # def test_redeclared_param_and_variable_of_func(self):
    #     input = """
    #     int x,y;
    #     float main(int foo){
    #         int foo;
    #     }"""
    #     expect = "Redeclared Variable: foo"
    #     self.assertTrue(TestChecker.test(input,expect,409))

    # def test_true_redeclared_diff_scope(self):
    #     input = """
    #     int x;
    #     float main(int para){
    #         int x;
    #         int para;
    #     }"""
    #     expect = "Redeclared Variable: para"
    #     self.assertTrue(TestChecker.test(input,expect,410))

    # def test_true_redeclared_diff_function(self):
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
    #     self.assertTrue(TestChecker.test(input,expect,411))

    # def test_undeclared_identifier(self):
    #     input = """
    #     float foo(){
    #         z = 1;
    #     }"""
    #     expect = "Undeclared Identifier: z"
    #     self.assertTrue(TestChecker.test(input,expect,412))

    # def test_true_undeclared_identifier_outside_func(self):
    #     input = """
    #     int z;
    #     float foo(){
    #         z = 1;
    #         x = z;  // for require
    #     }"""
    #     expect = "Undeclared Identifier: x"
    #     self.assertTrue(TestChecker.test(input,expect,413))

    # def test_true_undeclared_identifier_leftside(self):
    #     input = """
    #     int z;
    #     float foo(){
    #         int x;
    #         x = z;
    #         y = 1;
            
    #     }"""
    #     expect = "Undeclared Identifier: y"
    #     self.assertTrue(TestChecker.test(input,expect,414))

    # def test_undeclared_callExpr_func(self):
    #     input = """
    
    #     float foo(){
    #         int z;
    #         callFunc(z);
    #     }"""
    #     expect = "Undeclared Function: callFunc"
    #     self.assertTrue(TestChecker.test(input,expect,415))
        
    # def test_undeclared_callExpr_param(self):
    #     input = """
    
    #     int callFunc(int x){}
    #     float foo(){
    #         int z;
    #         callFunc(a);
    #     }"""
    #     expect = "Undeclared Identifier: a"
    #     self.assertTrue(TestChecker.test(input,expect,416))

    # def test_undeclared_callExpr_multi_param(self):
    #     input = """
    #     int callFunc(int x){}
    #     int x;
    #     float foo(){
    #         int y;
    #         callFunc(x,y,z);
    #     }"""
    #     expect = "Undeclared Identifier: z"
    #     self.assertTrue(TestChecker.test(input,expect,417))

    # def test_undeclared_vardecl_assign_boolean(self):
    #     input = """
    #     int callFunc(int x){}
    #     float foo(){
    #         x = true;
    #     }"""
    #     expect = "Undeclared Identifier: x"
    #     self.assertTrue(TestChecker.test(input,expect,418))

    # def test_undeclared_var_after_used(self):
    #     input = """
    #     void main(){
    #         x = 1;
    #         int x;
    #     }
    #     """
    #     expect = "Undeclared Identifier: x"
    #     self.assertTrue(TestChecker.test(input,expect,419))

    # def test_true_undeclared_in_add_operator(self):
    #     input = """
    #     void main(int x){
    #         x = 1;
    #         y = x // For error
    #     }
    #     """
    #     expect = "Undeclared Identifier: y"
    #     self.assertTrue(TestChecker.test(input,expect,419))

    

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
    #     self.assertTrue(TestChecker.test(input,expect,420))

    # def test_type_mismatch_in_expression_add_string_interger(self):
    #     input = """
    #     int callFunc(int x){}
    #     float foo(){
    #         1 + 1.1;
    #         true + 2;
    
    #         "str" + 123;
            
    #     }"""
    #     expect = "Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(true),IntLiteral(2))"
    #     self.assertTrue(TestChecker.test(input,expect,421))

    # def test_type_mismatch_in_expression_assign_left_float_right_boolean(self):
    #     input = """
    #     int callFunc(int x){}
    #     float foo(){
    #         1.2 = true;
    #     }"""
    #     expect = "Type Mismatch In Expression: BinaryOp(=,FloatLiteral(1.2),BooleanLiteral(true))"
    #     self.assertTrue(TestChecker.test(input,expect,422))

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
    #     self.assertTrue(TestChecker.test(input,expect,423))

    # def test_type_mismatch_in_expression_assign_left_int_right_float(self):
    #     input = """
    #     int callFunc(int x){}
    #     float foo(){
    #         11 = 11;
    #         12.3 = 12.3;
    #         12.0 = 12;
           
    #         1 = 12.3
    #     }"""
    #     expect = "Type Mismatch In Expression: BinaryOp(=,IntLiteral(1),FloatLiteral(12.3))"
    #     self.assertTrue(TestChecker.test(input,expect,424))

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
    #     self.assertTrue(TestChecker.test(input,expect,425))

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
    #     self.assertTrue(TestChecker.test(input,expect,427))

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
    #     self.assertTrue(TestChecker.test(input,expect,428))

    # def test_type_mismatch_in_expression_combined_operators_simple(self):
    #     input = """
    #     int callFunc(int x){}
    #     void main(){
    #        int x;
    #        x = 123 * 12 + 15 - 67/14.2;
        
    #     }"""
    #     expect = "Type Mismatch In Expression: BinaryOp(=,Id(x),BinaryOp(-,BinaryOp(+,BinaryOp(*,IntLiteral(123),IntLiteral(12)),IntLiteral(15)),BinaryOp(/,IntLiteral(67),FloatLiteral(14.2))))"
    #     self.assertTrue(TestChecker.test(input,expect,429))


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
    #     self.assertTrue(TestChecker.test(input,expect,430))

    # def test_type_mismatch_in_expression_compare_greater(self):
    #     input = """
        
    #     int foo(){
    #         int x ;
    #         x = 1 > 0;
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(=,Id(x),BinaryOp(>,IntLiteral(1),IntLiteral(0)))"
    #     self.assertTrue(TestChecker.test(input,expect,431))


    # def test_type_mismatch_in_expression_compare_greater_assign(self):
    #     input = """
        
    #     int foo(){
    #         string x ;
    #         x = 123 >= 111 + 1;
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(=,Id(x),BinaryOp(>=,IntLiteral(123),BinaryOp(+,IntLiteral(111),IntLiteral(1))))"
    #     self.assertTrue(TestChecker.test(input,expect,432))
   

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
    #     self.assertTrue(TestChecker.test(input,expect,433))


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
    #     self.assertTrue(TestChecker.test(input,expect,434))

    # def test_type_mismatch_in_expression_operator_and(self):
    #     input = """
        
    #     int foo(){
    #         boolean x ;
    #         x = true && false;
    #         x = 123 and -123;
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(=,Id(x),IntLiteral(123))"
    #     self.assertTrue(TestChecker.test(input,expect,435))

    # def test_type_mismatch_in_expression_operator_and_combine(self):
    #     input = """
        
    #     int foo(){
    #         boolean x ;
    #         x = true && true && false;
    #         x = false && "true" ;
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(&&,BooleanLiteral(false),StringLiteral(true))"
    #     self.assertTrue(TestChecker.test(input,expect,436))


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
    #     self.assertTrue(TestChecker.test(input,expect,437))

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
    #     self.assertTrue(TestChecker.test(input,expect,438))

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
    #     self.assertTrue(TestChecker.test(input,expect,439))

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
    #     self.assertTrue(TestChecker.test(input,expect,440))


    # def test_true_type_mismatch_in_expression_operator_and_combine_complex(self):
    #     input = """
        
    #        int foo(){
    #         boolean x ;
    #         x = true && true && -123 == -123 && 1 == 1 && true == true;
    #         x = false && "false" ; // For error
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(&&,BooleanLiteral(false),StringLiteral(false))"
    #     self.assertTrue(TestChecker.test(input,expect,441))


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
    #     self.assertTrue(TestChecker.test(input,expect,442))

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
    #     self.assertTrue(TestChecker.test(input,expect,443))

    # def test_true_type_mismatch_in_expression_operator_mod(self):
    #     input = """
        
    #         int foo(){
    #         int n;
    #         n = n%12;
    #         n = 123%1.1; // For error
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(%,IntLiteral(123),FloatLiteral(1.1))"
    #     self.assertTrue(TestChecker.test(input,expect,444))

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
    #     self.assertTrue(TestChecker.test(input,expect,445))

    ## def test_TypeMismatchInExpression_funcall_arraytype(self):
    ##     input = """
    ##                 int[] foo (int b []){
    ##                     int a[1] ;
    ##                     if (1 + 1 == 2) return a ; //CORRECT
    ##                     else return b ; //CORRECT
    ##                 }
    ##                 void main(){
    ##                     int arr[];
    ##                    foo(arr); // CORRECT
    ##                     return;
    ##                 }
    ##     """
    ##     expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(arr)])"
    ##     self.assertTrue(TestChecker.test(input,expect,445))


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
    #     self.assertTrue(TestChecker.test(input,expect,446))

    # # def test_if_condition_is_boolean_expresion(self):
    # #     input = """
    # #         int x;
    # #         void main(){
    # #             if(true){}else{}
    # #             if(false){}else{}
    # #             if(1==1){}else{}
    # #             if(true == true){}else{}

    # #             boolean bool ;
    # #             bool = x >= 4 ;  // error undeclared x

    # #             int x = 5;
    # #             if(true){}else{}
    # #             if(1 + 2){}else{}
    # #         }
    # #     """
    # #     expect = "Type Mismatch In Statement: If(IntLiteral(1),Block([]),Block([]))"
    # #     self.assertTrue(TestChecker.test(input,expect,447))


    # def test_undeclared_variable_in_if_thenStmt(self):
    #     input = """
    #         void main(){
    #             int var;
    #             if(true){
    #                 x = 1;
    #             }else{}
                
    #         }
    #     """
    #     expect = "Undeclared Identifier: x"
    #     self.assertTrue(TestChecker.test(input,expect,448))

    # def test_undeclared_func_in_if_thenStmt(self):
    #     input = """
    #         void main(){
    #             int var;
    #             if(true){
    #                 foo();
    #             }else{
                    
    #             }
                
    #         }
    #     """
    #     expect = "Undeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,449))

    # def test_undeclared_variable_in_if_elseStmt(self):
    #     input = """
    #         void main(){
    #             int var;
    #             if(true){
    #                 //foo();
    #             }else{
    #                 status = true;
    #             }
                
    #         }
    #     """
    #     expect = "Undeclared Identifier: status"
    #     self.assertTrue(TestChecker.test(input,expect,450))

    # def test_undeclared_func_in_if_elseStmt(self):
    #     input = """
    #         void main(){
    #             int var;
    #             if(true){
    #                 //foo();
    #             }else{
    #                 foo()
    #             }
                
    #         }
    #     """
    #     expect = "Undeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,451))

    # def test_true_undeclared_in_if(self):
    #     input = """
    #         void main(){
    #             boolean have = true;
    #             boolean checked;
            
    #             int sum ;
    #             sum = 0;
    #             if(have){
    #                 sum = 1;
    #                 checked = 123;  // For error type
    #             }else{
    #                 sum = 2;
    #             }
    #             sum = 3;
    #         }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(=,Id(checked),IntLiteral(123))"
    #     self.assertTrue(TestChecker.test(input,expect,452))

    # def test_Undeclared_Function_in_Else(self):
    #     input = """
    #         void main(){
    #             if(5<6){
    #                 int foo;
    #             }
    #             else{
    #                 foo();
    #             }
    #         }
    #     """
    #     expect = "Undeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,453))

    # def test_TypeMismatchInStatement_for(self):
    #     input = """
    #         void main(){
    #            for(5;"test";5){
    #                foo();
    #            }
    #         }
    #     """
    #     expect = "Type Mismatch In Statement: For(IntLiteral(5);StringLiteral(test);IntLiteral(5);Block([CallExpr(Id(foo),[])]))"
    #     self.assertTrue(TestChecker.test(input,expect,454))

    # def test_TypeMismatchInStatement_In_expr1(self):
    #     input = """
    #         void main(){
    #            for(true;5>6;5){
    #                foo();
    #            }
    #         }
    #     """
    #     expect = "Type Mismatch In Statement: For(BooleanLiteral(true);BinaryOp(>,IntLiteral(5),IntLiteral(6));IntLiteral(5);Block([CallExpr(Id(foo),[])]))"
    #     self.assertTrue(TestChecker.test(input,expect,455))

    # def test_TypeMismatchInStatement_In_expr3(self):
    #     input = """
    #         void main(){
    #            for(4;5>6;false){
    #                foo();
    #            }
    #         }
    #     """
    #     expect = "Type Mismatch In Statement: For(IntLiteral(4);BinaryOp(>,IntLiteral(5),IntLiteral(6));BooleanLiteral(false);Block([CallExpr(Id(foo),[])]))"
    #     self.assertTrue(TestChecker.test(input,expect,456))

    # def test_TypeMismatchInStatement_In_doWhile(self):
    #     input = """
    #         void main(){
    #            do{
    #                foo();
    #            }
    #            while("test");
    #         }
    #     """
    #     expect = "Type Mismatch In Statement: Dowhile([Block([CallExpr(Id(foo),[])])],StringLiteral(test))"
    #     self.assertTrue(TestChecker.test(input,expect,457))

    # def test_TypeMismatchInStatement_In_doWhile1(self):
    #     input = """
    #         void main(){
    #             int a;
    #             a = 6;
    #            do{
    #                foo();
    #            }
    #            while(a);
    #         }
    #     """
    #     expect = "Type Mismatch In Statement: Dowhile([Block([CallExpr(Id(foo),[])])],Id(a))"
    #     self.assertTrue(TestChecker.test(input,expect,458))

    # def test_TypeMismatchInStatement_In_doWhile2(self):
    #     input = """
    #         void main(){
    #             int a;
    #             a = 6;
    #            do{
    #                foo();
    #            }
    #            while(a+5);
    #         }
    #     """
    #     expect = "Type Mismatch In Statement: Dowhile([Block([CallExpr(Id(foo),[])])],BinaryOp(+,Id(a),IntLiteral(5)))"
    #     self.assertTrue(TestChecker.test(input,expect,459))

    # def test_TypeMismatchInStatement_In_func_void_return_inttype(self):
    #     input = """
    #         void main(){
    #            return 5;
    #         }
    #     """
    #     expect = "Type Mismatch In Statement: Return(IntLiteral(5))"
    #     self.assertTrue(TestChecker.test(input,expect,460))

    # def test_TypeMismatchInStatement_In_void_return_empty(self):
    #     input = """
    #         void main(){
    #            return;
    #         }
    #         void foo(int x){
    #             x = x + 1; 
    #             return 1;
    #         }
    #     """
    #     expect = "Type Mismatch In Statement: Return(IntLiteral(1))"
    #     self.assertTrue(TestChecker.test(input,expect,461))

    # def test_TypeMismatchInStatement_return1(self):
    #     input = """
    #         int foo(){
    #             return true;
    #         }
    #         void main(){
    #            foo();
    #         }
    #     """
    #     expect = "Type Mismatch In Statement: Return(BooleanLiteral(true))"
    #     self.assertTrue(TestChecker.test(input,expect,462))

    # def test_TypeMismatchInStatement_return2(self):
    #     input = """
    #         int foo(string c){
    #             return c;
    #         }
    #         void main(){
    #            foo("chi");
    #         }
    #     """
    #     expect = "Type Mismatch In Statement: Return(Id(c))"
    #     self.assertTrue(TestChecker.test(input,expect,463))

    # def test_TypeMismatchInStatement_return3(self):
    #     input = """
    #         int foo(string c,float e){
    #             return e;
    #         }
    #         void main(){
    #            foo("thien",1.5);
    #         }
    #     """
    #     expect = "Type Mismatch In Statement: Return(Id(e))"
    #     self.assertTrue(TestChecker.test(input,expect,464))

    # def test_TypeMismatchInStatement_return_void(self):
    #     input = """
    #         void foo(string c,float e){
    #             return 5;
    #         }
    #         void main(){
    #            foo("thien",1.5);
    #         }
    #     """
    #     expect = "Type Mismatch In Statement: Return(IntLiteral(5))"
    #     self.assertTrue(TestChecker.test(input,expect,465))

    # def test_TypeMismatchInStatement_return_string(self):
    #     input = """
    #         string foo(string c,float e){
    #             return e;
    #         }
    #         void main(){
    #            foo("thien",1.5);
    #         }
    #     """
    #     expect = "Type Mismatch In Statement: Return(Id(e))"
    #     self.assertTrue(TestChecker.test(input,expect,466))

    # def test_TypeMismatchInStatement_return_boolean(self):
    #     input = """
    #         boolean foo(string c,float e){
    #             return e;
    #         }
    #         void main(){
               
    #         }
    #     """
    #     expect = "Type Mismatch In Statement: Return(Id(e))"
    #     self.assertTrue(TestChecker.test(input,expect,467))

    # def test_TypeMismatchInStatement_return_type_invalid(self):
    #     input = """
    #         boolean foo(string str,float f){
    #             boolean result;
    #             result = true; 
    #             return 1 == 1;
    #         }
    #         int foo1(int x, string str){
    #             return str;
    #         }
    #         void main(){
    #            foo("chi",1.5);
    #            return ;
    #         }
    #     """
    #     expect = "Type Mismatch In Statement: Return(Id(str))"
    #     self.assertTrue(TestChecker.test(input,expect,468))

    # def test_FunctionNotReturn_func_inttype_not_return(self):
    #     input = """
           
    #         int foo(string str){
                
    #         }
    #         void main(){
    #            foo("chi");
    #            return ;
    #         }
    #     """
    #     expect = "Function foo Not Return "
    #     self.assertTrue(TestChecker.test(input,expect,469))

    # def test_FunctionNotReturn_func_inttype_return_empty(self):
    #     input = """
           
    #         void foo(string str){
    #             return ;
    #         }
    #         int foo1(){
    #             return;
    #         }
    #         void main(){
    #            return ;
    #         }
    #     """
    #     expect = "Function foo1 Not Return "
    #     self.assertTrue(TestChecker.test(input,expect,470))

    # def test_FunctionNotReturn_if_thenStmt_not_return(self):
    #     input = """
           
    #         int foo(string str){
    #             int x;
    #             x = 0;
    #             if(true){
    #                 x = 1;
    #                          // Missing return 
    #             }else{
    #                 x = 2;
    #                 return 1;
    #             }
    #             return x;
    #         }
    #         void main(){
    #            foo("chi");
    #            return;
    #         }
    #     """
    #     expect = "Function foo Not Return "
    #     self.assertTrue(TestChecker.test(input,expect,471))

    # def test_FunctionNotReturn_if_elseStmt_not_return(self):
    #     input = """
           
    #         int foo(string str){
    #             int x;
    #             x = 0;
    #             if(true){
    #                 x = 1;
    #                 return x;         
    #             }else{
    #                 x = 2;
    #                        // Missing return 
    #             }
    #             return x;
    #         }
    #         void main(){
    #            foo("chi");
    #            return;
    #         }
    #     """
    #     expect = "Function foo Not Return "
    #     self.assertTrue(TestChecker.test(input,expect,472))


    # def test_Function_Not_Return_only_return_in_for(self):
    #     input = """
    #         int foo2(){
    #         int i;
    #         for( i = 0; i < 2;i = i + 1){
    #                 return 0;
    #             }
    #         //return 1;   // For error
    #         }
    #         int foo(){

    #         }
    #         void main(){
    #            foo2();
    #            foo();
    #         }
    #     """
    #     expect = "Function foo2 Not Return "
    #     self.assertTrue(TestChecker.test(input,expect,473))

    # def test_function_no_return_with_for(self):
    #     input = """
    #         int foo2(){
    #         int i;
    #         for( i = 0; i < 2;i = i + 1){
    #                 return 0;
    #             }
    #         return 1;   // For error
    #         }
    #         int foo(){

    #         }
    #         void main(){
    #            foo2();
    #            foo();
    #         }
    #     """
    #     expect = "Function foo Not Return "
    #     self.assertTrue(TestChecker.test(input,expect,474))

    # def test_function_no_return_with_doWhile(self):
    #     input = """
    #         int foo2(){
    #             do{
    #                 return 5;
    #             }
    #             while(5<3);
    #         }
    #         int foo(){
                
    #         }
    #         void main(){
    #            foo2();
    #            foo();
    #         }
    #     """
    #     expect = "Function foo2 Not Return "
    #     self.assertTrue(TestChecker.test(input,expect,475))

    # def test_function_no_return_with_doWhile(self):
    #     input = """
    #         int foo2(){
    #             do{
    #                 return 5;
    #             }
    #             while(5<3);
    #         }
    #         int foo(){
                
    #         }
    #         void main(){
    #            foo2();
    #            foo();
    #           return;
    #         }
    #     """
    #     expect = "Function foo2 Not Return "
    #     self.assertTrue(TestChecker.test(input,expect,476))

    # def test_Break_Not_In_Loop_Inside_Outside_For(self):
    #     input = """
    #         void main(){
    #             int x;
    #             x = 0;
    #             int i;
    #             for( i = 0; i < 2;i = i + 1){
    #                 x = x + 1;   
    #                 break;
    #             }
    #             break;

    #             return;
                
                
    #         }
    #     """
    #     expect = "Break Not In Loop"
    #     self.assertTrue(TestChecker.test(input,expect,477))

    # def test_Break_Not_In_Loop_Inside_Outside_do_while(self):
    #     input = """
    #         void main(){
    #             int x,i;
    #             x = 0;
    #             i = 10;
    #             break;
    #             do{
    #                 x = x + i;
    #                 break;
    #             }while(1 == 1);

    #             return;
                
                
    #         }
    #     """
    #     expect = "Break Not In Loop"
    #     self.assertTrue(TestChecker.test(input,expect,478))

    # def test_Break_Not_In_Loop_Inside_Outside_for_in_func(self):
    #     input = """
    #         int foo(int x){
    #             int i;
    #             i = 0;
    #             for (i;i<10;i =  i+1){
    #                 x = x + 1;
    #                 break;
    #             }
    #             break;
    #             return 1;
    #         }
    #         void main(){
    #             int x;
    #             x = 123;
    #             foo(x);
    #             return;
    #         }
    #     """
    #     expect = "Break Not In Loop"
    #     self.assertTrue(TestChecker.test(input,expect,479))

    # def test_Break_Not_In_Loop_Inside_If_thenStmt_outside_for(self):
    #     input = """
    #         int foo(int x){
    #             int i;
    #             i = 0;
    #             for (i;i<10;i =  i+1){
    #                 x = x + 1;
    #                 break;
    #             }
    #             boolean bool ;
    #             bool = true;
    #             if(true){
    #                 bool = false;
    #                 break;
    #                 return 1;
    #             }
    #             return 1;
    #         }
    #         void main(){
    #             int x;
    #             x = 123;
    #             foo(x);
    #             return;
    #         }
    #     """
    #     expect = "Break Not In Loop"
    #     self.assertTrue(TestChecker.test(input,expect,480))

    # def test_Break_Not_In_Loop_Inside_If_thenStmt_inside_for(self):
    #     input = """
    #         int foo(int x){
    #             int i; boolean bool;
    #             i = 0;
    #             bool = true;
    #             for (i;i<10;i =  i+1){
    #                 if(true){
    #                     bool = false;
    #                     break;         // CORRECT
    #                     return 1;      // Bug
    #                 }
    #                 break;             // CORRECT
    #                 return 1;           // Bug
    #             }
    #             break;   
    #             return 1;
    #         }
    #         void main(){
    #             int x;
    #             x = 123;
    #             foo(x);
    #             return;
    #         }
    #     """
    #     expect = "Break Not In Loop"
    #     self.assertTrue(TestChecker.test(input,expect,481))

    # def test_true_Unreachable_function(self):
    #     input = """
    #         int foo(int x){
    #             x = 2;
    #             return x;
    #         }
    #         string bar(){
                
    #             return "chile";
    #         }
    #         void main(){
    #             foo(1);
    #             return;
    #         }
    #     """
    #     expect = "Unreachable Function: bar"
    #     self.assertTrue(TestChecker.test(input,expect,482))

    # def test_true_Unreachable_function_multi_not_called(self):
    #     input = """
    #         int foo(int x){
    #             x = 2;
    #             return x;
    #         }
    #         string bar(){
    #             return "chile";
    #         }
    #         void main(){
    #             return;
    #         }
    #     """
    #     expect = "Unreachable Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,483))

    # def test_Unreachable_func_called_in_if(self):
    #     input = """
    #         int nobita(){
    #             return 5;
    #         }
    #         int sasuke(int a){
    #             return a;
    #         }
    #         void main(){
    #             if(true){
    #                 nobita();
    #                 return;
    #             }
    #             return;
    #         }
    #     """
    #     expect = "Unreachable Function: sasuke"
    #     self.assertTrue(TestChecker.test(input,expect,484))

    # def test_true_Unreachable_call_func_call_func(self):
    #     input = """
    #         int bar(int a){
    #             return 1;
    #         }
    #         int foo(){
    #             bar(1);
    #             return 1;
    #         }
    #         int foobar(boolean x){   // For error
    #             return true;
    #         }
    #         void main(){
    #             foo();
    #             return;
    #         }
    #     """
    #     expect = "Unreachable Function: foobar"
    #     self.assertTrue(TestChecker.test(input,expect,485))

    # def test_Not_Left_Value_left_inlit(self):
    #     input = """
    
    #         void main(int a[]){
    #             int z;
    #             3 = z + 1;
    #             //z + 1 = 2;
    #             //int d[3] ;
    #             //d[0] = 0 ; 
    #             return;
    #         }
    #     """
    #     expect = "Not Left Value: IntLiteral(3)"
    #     self.assertTrue(TestChecker.test(input,expect,486))

    # def test_Not_Left_Value_left_expression(self):
    #     input = """
    
    #         void main(int a[]){
    #             int z;
    #             //3 = z + 1;
    #             z + 1 = 2;
    #             //int d[3] ;
    #             //d[0] = 0 ; 
    #             return;
    #         }
    #     """
    #     expect = "Not Left Value: BinaryOp(+,Id(z),IntLiteral(1))"
    #     self.assertTrue(TestChecker.test(input,expect,487))

    # def test_Not_Left_Value_left_expression(self):
    #     input = """
    
    #         void main(int a[]){
    #             int z;
               
    #             int d[3] ;
    #             d[0] = 0 ; 
    #             d  = 3;  // For error
    #             return;
    #         }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(=,ArrayCell(Id(d),IntLiteral(0)),IntLiteral(0))"
    #     self.assertTrue(TestChecker.test(input,expect,488))


    def test_Not_Left_Value_left_in_if(self):
        input = """
    
            void main(int a[]){
                int z;
                if(true){
                    z + 1 = 123;
                    return;
                }
                return;
            }
        """
        expect = "Not Left Value: BinaryOp(+,Id(z),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,489))
