import unittest
from string_calculator import *

class TestStringCalculator(unittest.TestCase):

    #1 
    def test_non_string_input(self):
        SC=StringCalculator()
        numb_list = ['10','20','30']
        with self.assertRaises(TypeError):
            SC.add(10,20,30)
            SC.add(numb_list)
            SC.add(a,b,c)
    #2
    def test_add(self):
        SC=StringCalculator()
        
        self.assertEqual(SC.add('1,2,3'), 6)
        self.assertEqual(SC.add('9,10,4'), 23)
        self.assertEqual(SC.add('2,2,2,2,6'), 14)
        self.assertEqual(SC.add('100,123,1000'), 1223)
        self.assertEqual(SC.add('2'), 2)
    #3
    def test_empty_string(self):
        SC=StringCalculator()
        
        self.assertEqual(SC.add(''), 0)
        self.assertEqual(SC.add(',,'), 0)
        
    #4
    def test_negative_numbers(self):
        SC=StringCalculator()
        with self.assertRaises(ValueError):
            SC.add('-9,-6,-10')
            SC.add('9,-79,30,-50')
    #5
    def test_numbers_greater_than_1000(self):
        SC=StringCalculator()
        
        self.assertEqual(SC.add('1050,1010,1001'), 0)
        self.assertEqual(SC.add('50,1010,1001,60'), 110)
        
    #6(FAILED)
    def test_non_numerical_string(self):
        SC=StringCalculator()
        with self.assertRaises(ValueError):
            SC.add('a,b,c')
            SC.add('*,/,=,&&&,\n')

    #7
    def test_custom_delimiter_add(self):
        SC=StringCalculator()
        self.assertEqual(SC.add('//[ ]\n5 6'), 11)
        self.assertEqual(SC.add('//[//]\n10//20//30//40'), 100)
        self.assertEqual(SC.add('//[a]\n2a2a2a2a2'), 10)
        self.assertEqual(SC.add('//[50]\n3503503503'), 12)

    #8
    def test_custom_delimiter_with_negative_numbers(self):
        SC=StringCalculator()
        with self.assertRaises(ValueError):
            SC.add('//[+]\n-5+-6')
            SC.add('//[&&&&]\n-5&&&&-6')
            SC.add('//[*]\n-7*10*20')
    #9
    def test_custom_delimiter_with_number_numbs_greater_than_1000(self):
        SC=StringCalculator()
        self.assertEqual(SC.add('//[+]\n50+1010+1001+50'), 100)
        self.assertEqual(SC.add('//[\\]\n1300\\1210\\1501'), 0)
        self.assertEqual(SC.add('//[=]\n900050=101900=17801'), 0)

    #10 (FAILED)
    def test_custom_delimiter_with_none_numerical_string(self):
        SC=StringCalculator()
        with self.assertRaises(ValueError):
            SC.add('//[===]\na===b===c')
            SC.add('//[+]\n*+/+=+&&&+\n')
    
    #11
    def test__custom_delimiter_with_empty_string(self):
        SC=StringCalculator()
        self.assertEqual(SC.add('//[+]\n + + + + '),0)
        self.assertEqual(SC.add('//[===]\n'),0)
    #12
    def test_if_Instance_StringCalculator(self):
        Calc = StringCalculator()
        SC = StringCalculator()
        self.assertIsInstance(Calc, StringCalculator)
        self.assertIsInstance(SC, StringCalculator)
        

    #13
    def test_custom_delimiter_with_non_string_input(self):
        SC = StringCalculator()
        with self.assertRaises(TypeError):
            SC.add('//[+]\n',10+20+30)
            SC.add('//[==]\n',a==b==c)

    #14(FAILED)
    def test_add_numbers_with_multiple_custom_delimiters(self):
        sc = StringCalculator()
        with self.assertRaises(SyntaxError):
            sc.add('//[*][%]\n1*2%3')

    #15(FAILED)
    def test_add_numbers_with_incorrect_custom_delimiter_syntax(self):
        sc = StringCalculator()
        with self.assertRaises(SyntaxError):
            sc.add('//[*]\n1+2+3')
        

if __name__ == '__main__':
    unittest.main()






    



    
