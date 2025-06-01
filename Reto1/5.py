def mismos_char(lista:list):
    '''
    Esta función recibe una lista de strings e itera en esta con 2 ciclos for
    anidados, omitiendo los indices iguales y elementos con número de letras
    distintos. Luego itera en cada elemento y analiza si cada letra está en la
    otra palabra analizada, si es verdadero, elimina la letra que coincide de
    una copia de la lista y repite el proceso. Si todas las letras coincidieron,
    almacena estas dos palabras en una lista
    '''

    lista_anagramas = []
    copia_lista = lista.copy()

    for i in range(len(lista)):

        for e in range(len(lista)):

            if i==e or len(lista[i])!=len(lista[e]): continue

            for c in lista[i]:
                if c in copia_lista[e]:
                    copia_lista[e] = lista[e].replace(c, "", 1)
                    anagrama = True
                else:
                    anagrama = False
                    break

            if anagrama==True:
                lista_anagramas += [lista[i], lista[e]]
    
    lista_anagramas = list(set(lista_anagramas))
    # Se convierte la lista en un conjunto y luego en una lista de
    # nuevo para eliminar cualquier palabra repetida.

    return lista_anagramas

if __name__ == "__main__":
    lista=input("Ingrese las palabras separadas por espacios: ").split()
    print(mismos_char(lista))