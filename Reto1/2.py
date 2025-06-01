def verificación_palindromo(palabra:str)->None:
    '''
    La función pide una palabra e itera por cada una de las letras
    (de izquierda a derecha) y la compara con las letras en sentido
    contrario (derecha a izquierda), si alguna letra llega a ser diferente,
    imprime que la palabra no es palindroma y viceversa.
    '''
    n:int = 0
    for i in range(len(palabra)):
        if palabra[i] != palabra[(-(i + 1))]:
            print(f"La palabra {palabra} no es palindroma")
            return None
        
    print(f"La palabra {palabra} es palindroma")
    return None

if __name__ == "__main__":
    palabra:str = input("Ingrese la palabra que quiere analizar: ")
    verificación_palindromo(palabra)