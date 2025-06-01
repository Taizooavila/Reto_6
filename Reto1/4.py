def mayor_suma():
    '''
    Esta función recibe una lista de números e itera por cada uno de estos,
    almacenando el número anterior a este y sumándolo, luego compara esta suma
    con la más alta hasta el momento y almacena la más alta. Al final, retorna
    la suma más alta que haya registrado.
    '''
    listastr:str = input("Ingrese los números de la lista separados por espacio: ")
    lista:list = listastr.split()
    num1:int = 0
    num2:int = 0
    sumamax:int = 0

    try:
        for element in lista:
            num2 = int(element)
            if (num1+num2)>sumamax:
                sumamax = num1+num2
            num1 = int(element)
            print(f"Lista: {lista}\nLa mayor suma entre numeros consecutivos de tu lista es: {sumamax}")
            return
    except ValueError:
        print("Los datos ingresados no son válidos")
        mayor_suma()

if __name__ == "__main__":

    mayor_suma()