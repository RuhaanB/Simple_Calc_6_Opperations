# This is basically the instructions
print(' ')

print('This is a basic 2 figure calculator. Input any 2 figures, then input a function... and wait for the results')
print(' ')

print('PLEASE follow all of the instructions as directed, press enter after completing the given step')
print(' ')

# This is value 1

print('Use your cursor to enter the first value. Subtraction, division and exponentiation are operations... '
      'in which the order matters.')
Value1 = float(input('Enter First Value: '))
print(' ')

# This is value 2

print('Use your cursor to enter the second value.')
Value2 = float(input('Enter Second Value: '))
print(' ')

# This is the operator

print('Please input the desired operator')
print('''You can only input these operators
      + = Addition
      - = Subtraction
      / = Division
      x = Multiplication
      ^ = Power
      rt = Value 1 Root Value 2
      ''')

print(' ')

# Defining how to root using the power function


# All of the functions

Sum = Value1 + Value2
difference = Value1 - Value2
product = Value1 * Value2
quotient = Value1 / Value2
power = Value1 ** Value2
root = Value1 ** (1/Value2)

Opp = input('Input your Operation here ')
print(' ')

if Opp == '+':
    print(str(Value1) + ' + ' + str(Value2) + ' = ' + str(Sum))

elif Opp == '-':
    print(str(Value1) + ' - ' + str(Value2) + ' = ' + str(difference))

elif Opp == 'x':
    print(str(Value1) + ' x ' + str(Value2) + ' = ' + str(product))

elif Opp == '/':
    print(str(Value1) + ' ÷ ' + str(Value2) + ' = ' + str(quotient))

elif Opp == '^':
    print(str(Value1) + ' ^ ' + str(Value2) + ' = ' + str(power))

elif Opp == 'rt':
    print(str(Value2) + ' √ ' + str(Value1) + ' = ' + str(root))

else:
    print('You have not typed a valid operator, please run the program again. Remember to read instructions carefully')

print(' ')

print('Thank you for using this calculator!')
