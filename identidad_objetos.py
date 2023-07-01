#Comparacion del uso de operador == o el operador is en POO

#El operador == copara el contenido de 2 objetos (contenido igual)
# no necesariamente son el mismo objeto (pueden apuntar a objetos distintos)

#Operador is revisa si dos objetos son ig0uales (Objetos son identicos)
#Ambos deben estar apuntando a la misma direccion de memoria para ser iguales

#Ejemplo de una Lista
lista_a = [1,2,3]
lista_b = lista_a

# En este caso tanto la lista a y b tienen el mismo contenido (== es TRue)
# y  tmabien apuntan a la misma referencia (is regresa True)
print(f'Lista a y b tienen el mismo contenido?: {lista_a == lista_b}')
print(f'Lista a y b apunta al mismo objeto?: {lista_a is lista_b}')

#Sin embargo, si creamos un nuevo objeto
lista_c = list(lista_a)
# en  este caso la lista a tienen el mismo contenido que c ( == es TRue)
#pero ... la lista c apunta a un objeto distinto en memoria (is as False)

print(f'Lista a y c tienen el mismo contenido?: {lista_a == lista_c}')
print(f'Lista a y b tienen el mismo contenido?: {lista_a == lista_b}')
