def verificar_primos(lista:list)->list:
    '''
    Esta función recibe una lista de números y analiza si son primos,
    dividiendolos por los enteros anteriores a la mitad (+1) del número
    si alguno de estos numeros lo divide exactamente, este se elimina
    de la copia de la lista y luego retorna esta lista (con los numeros primos)
    '''

    primos:list = lista.copy()
    try:
        for i in lista:
            if int(i)==1 or int(i)==2 or int(i)==3: continue
            for n in range(2,(int(i)//2)+1):
                if int(i)%n == 0:
                    primos.remove(i)
                    break
        return primos
    except ValueError:
        print("Algún dato ingresado no es un número.")

if __name__ == "__main__":
    numeros = input("Ingrese los números separados por espacios: ").split()
    print(verificar_primos(numeros))