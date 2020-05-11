'''
Author : Artur Assis Alves
Date   : 10/05/2020
Title  : Question 8
'''
import abc, sys, math

'''
Resposta para a questão 8: Os métodos estáticos foram inseridos no exemplo da calculadora para ilustrar métodos que não
necessitam de acesso nem ao objeto da classe nem à classe em si. São métodos mais simples de se testar, pois não necessitam
da criação de instâncias da classe para o teste além de possuírem maior grau de independência. Os métodos abstratos foram
utilizados para demonstrar a possibilidade de se criar uma classe em relação à qual todas a subclasses devem ter esses métodos
sobrescritos. Isso impede que alguma das subclasses não sobrescrevam o método. Os métodos de classe são menos independentes que
os métodos estáticos, pois já têm acesso à classe por meio do argumento cls. São uteis para métodos que não necessitam de acesso
a uma instanciação da classe. Podem ser utilizados para criação de iniciadores alternativos, por exemplo.
'''

#Classes:
class Calculator(abc.ABC):
    ''' Performs basic calculations between two decimal numbers such as addition, subtraction, multiplication, and division. '''    
    
    @staticmethod
    @abc.abstractmethod
    def addition(*args):
        pass
    
    @staticmethod
    @abc.abstractmethod
    def multiplication(*args):
        pass

    @staticmethod
    @abc.abstractmethod
    def subtraction (a, b):
        pass
    
    @staticmethod
    @abc.abstractmethod
    def division (a, b):
        pass

class SimpleCalculator(Calculator):
    ''' Performs basic calculations between two decimal numbers such as addition, subtraction, multiplication, and division. '''
    @staticmethod
    def addition(a, b):
        '''
        Returns a + b.

        Input:
            a      -> float
            b      -> float

        Output:
            a + b -> float
        '''
        return a + b

    @staticmethod
    def multiplication(a, b):
        '''
        Returns a*b.

        Input:
            a      -> float
            b      -> float

        Output:
            a*b    -> float
        '''
        return a*b

    @staticmethod
    def subtraction (a, b):
        '''
        Returns a - b.

        Input:
            a      -> float
            b      -> float

        Output:
            a - b -> float
        '''
        return a - b

    @staticmethod
    def division (a, b):
        '''
        Returns a/b.

        Input:
            a   -> float
            b   -> float

        Output:
            a/b -> float
        '''
        return a/b


class SophisticatedCalculator(Calculator):
    ''' Performs basic calculations between two decimal numbers such as addition, subtraction, multiplication, and division. '''

    @classmethod #É um método de classe e não um estático pois utiliza outros métodos da classe.
    def all_operations(cls, a, b):
        '''
        Returns the addition, multiplication, subtraction, and division of 'a' and 'b'.

        Input:
            a      -> float
            b      -> float

        Output:
            result -> tuple        
        '''
        return (cls.addition(a, b), cls.multiplication(a, b), cls.subtraction(a, b), cls.division(a, b))
    
    @staticmethod
    def addition(*args):
        '''
        Returns the sum of all numbers gathered in the arguments.

        Input:
            args   -> float

        Output:
            result -> float
        '''
        result = 0
        for n in args:
            result += n
        return result

    @staticmethod
    def multiplication(*args):
        '''
        Returns the multiplication of all numbers gathered in the arguments.

        Input:
            args   -> float

        Output:
            result -> float
        '''
        result = 1
        for n in args:
            result *= n
        return result

    @staticmethod
    def subtraction (a, b):
        '''
        Returns a - b.

        Input:
            a      -> float
            b      -> float

        Output:
            a - b -> float
        '''
        return a - b

    @staticmethod
    def division (a, b):
        '''
        Returns a/b.

        Input:
            a   -> float
            b   -> float

        Output:
            a/b -> float
        '''
        return a/b


def test(did_pass):
    ''' Print the result of a test.'''
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} is OK.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


def test_suite():
    '''
    Run the suite of tests for code in this module (this file).'''
    test(SophisticatedCalculator.addition(12.34, 2.34, 3.0, 4, 5, 10.701) == 37.381)
    test(SophisticatedCalculator.multiplication(3, 201, 3.4, 5) == 10251)
    test(SophisticatedCalculator.subtraction(10, 34.5) == -24.5)
    test(math.isclose(SophisticatedCalculator.division(23.45, 45.99), 23.45/45.99))
    test(SimpleCalculator.addition(2, 3) == 5)
    test(SimpleCalculator.multiplication(45, 7) == 315)
    test(SimpleCalculator.subtraction(-12, 4) == -16)
    test(math.isclose(SimpleCalculator.division(2, 3), 2/3))


    
#Main:
if __name__=='__main__':
    test_suite()

