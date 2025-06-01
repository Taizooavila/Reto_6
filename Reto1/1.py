
def Operaciones (num1:float, num2:float, operador:float):
    '''
    Función que recibe dos números y un string que indica la operación
    evalua el string y retorna el resultado de los números de a cuerdo
    a la operación recibida.

    '''
    if operador == "+":
        return num1 + num2
    elif operador == "-":
        return num1 - num2
    elif operador == "*":
        return num1 * num2
    else:
        return num1 / num2

def Main():
    '''
    Función que pide input de 2 números y un string que sería el operador.
    Si el input de los números no se puede convertir a float,
    la función se vuelve a llamar
    '''

    try:
        num1: float = float(input("Ingrese el primer número: "))
        num2: float = float(input("Ingrese el segundo número: "))
        operador: str = input("Ingrese el símbolo de la operación que quiere realizar (+, -, *, /)")
        lista_operadores = ("+", "-", "*", "/")
        while operador not in lista_operadores:
            operador = input("inserte un operador válido (+, -, *, /)")
        print(Operaciones(num1, num2, operador))
    except ValueError:
        print("El dato ingresado no es un número")
        Main()

if __name__ == "__main__":
    Main()
    