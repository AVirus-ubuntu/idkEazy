import os as os

try:
    oper = str  (input('OPER #>'))
    num1 = float(input('NUM1 #>'))
    num2 = float(input('NUM2 #>'))
except Exception as e: print('ERROR!'); exit()

if oper in ['+','-','*','/']:
    if False: ...
    elif oper == '+': print(f'{num1+num2}')
    elif oper == '-': print(f'{num1-num2}')
    elif oper == '*': print(f'{num1*num2}')
    elif oper == '/': print(f'{num1/num2}')
else:
    print(f'oper isnt valid')