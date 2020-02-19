import logging

# DEBUG: Detalled information. typically of interest only when diagnosting problems.
# Info: Confirmation that things are working as excpected
# Warning: An indication that something unexpected hapenned, or indicative of some problem in the near future. The software is still working as expected
# Error: Due to a more serious problem, the software has not been able to perfore some function
# Critical: A serious error, indicating that program itself may be unable to continue running

logging.basicConfig(filename="test.log",level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

num1=10
num2=5
mul_result=multiply(num1,num2)
logging.debug("Mul: {} * {} = {}".format(num1,num2,mul_result))
div_result=divide(num1,num2)
logging.debug("Div: {} / {} = {}".format(num1,num2,div_result))
