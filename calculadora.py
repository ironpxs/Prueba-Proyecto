def suma(num1,num2):
    total = num1 + num2
    return total

def resta(num1,num2):
    total = num1 - num2
    return total

def multiplicacion(num1,num2):
    total = num1 * num2
    return total

def division(num1,num2):
    if num2 == 0:
        return 0
    else:
        total = num1 / num2
        return total

def calculadora(operacion,num1,num2):
    if operacion == 'suma':
        total = suma(num1,num2)
    elif operacion == 'resta':
        total = resta(num1,num2)
    elif operacion == 'multiplicacion':
        total = multiplicacion(num1,num2)
    elif operacion == 'division':
        total = division(num1,num2)
    else:
        total = 0
        print('Esa operacion no existe.')
    return total