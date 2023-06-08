#FUNCIONES BASICAS 2
# 1. Cuenta regresiva:
def countdown(n):
    result = list(range(n, -1, -1))
    print(result)
    return result
countdown(5)
countdown(10)
countdown(20)

print("__________________")

# 2. Imprimir y devolver:
def imprimir_y_devolver(lista):
    print(lista[0])
    return lista[1]
resultado = imprimir_y_devolver([5,15])
print("Numero devuelto: " , resultado)
resultado = imprimir_y_devolver([52,10])
print("Numero devuelto: " , resultado)


print("__________________")

# 3. Primero más longitud:
def primero_mas_longitud(lista):
    result = lista[0] + len(lista)
    print(result)
    return result
primero_mas_longitud([1,2,3,4,5])
primero_mas_longitud([2,3,4,5,6])

print("__________________")

# 4. Valores mayores que el segundo:
def valores_mayores_que_el_segundo(lista):
    if len(lista) < 2:
        print(False)
        return False

    nueva_lista = [x for x in lista if x > lista[1]] #aqui utilizo técnica de comprensión de listas, en donde se crea la variable x la cual itera la lista inicial para revisar si se cumple la condición y si se cumple, entonces forma parte de la nueva_lista
    print(len(nueva_lista), nueva_lista)
    return nueva_lista
valores_mayores_que_el_segundo([5,2,3,2,1,4])
valores_mayores_que_el_segundo([150,20,32,22,11,45])
valores_mayores_que_el_segundo([5])

print("__________________")

# 5. Esta longitud, ese valor: 
def length_and_value(size, value):
    result = [value] * size
    print(result)
    return result
length_and_value(4,7)
length_and_value(14,27)