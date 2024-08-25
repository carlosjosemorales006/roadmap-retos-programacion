
#01 OPERADORES Y ESTRUCTURAS DE CONTROL

# Aritmeticos

suma = 5 + 5
resta = 5 - 5
multiplicacion = 5 * 5
division = 5 / 5
division_entera = 5 // 5
potencia = 5 ** 5
residuo = 5 % 5

print (f'''
       ----------------------------------------
       RESULTADO DE LAS OPERACIONES ARITMETICAS
       ----------------------------------------
       SUMA: {suma}
       RESTA: {resta}
       MULTIPLICACION: {multiplicacion}
       DIVISION: {division}
       DIVISION ENTERA: {division_entera}
       POTENCIA: {potencia}
       RESIDUO: {residuo}
       ----------------------------------------
       ''')


# OPERADORES LOGICOS

y = True and True # Solo es verdadero si ambos son verdaderos
o = False or False # Solo es falso si todos son falsos

# OPERADORES DE COMPARACION

mayorque = 5 > 3
mayor_o_igual_que = 5 >= 3
menorque = 5 < 3
menor_o_igual_que = 5 <= 5
igualdad = True == False # compara si ambos valores son iguales
desigualdad = True != False # compara si los valores no son iguales

# OPERACION DE ASIGNACION 

asignacion = 'El signo igual se utiliza para asignar valor'

# OPERACION DE IDENTIDAD

lista = [1,2,3]
lista2 = lista
identidad = lista is lista2
print('------------------------------------------------------------------------------')
print(f'identidad es igual: {identidad}, porque ambas hacen referencia al mismo objeto')

# OPERADORES DE PERTENENCIA 

frutas = ['uva','fresa','mango']
print
pertenecia = 'fresa' in frutas
print('------------------------------------------------------------------------------')
print(f'Pertenecia es igual a {pertenecia}, porque la fruta se encuentra en la lista')
print('-----------------------------------------------------------------------------------')

# operadore de bit

bit1 = 5
bit2 = 3
bits = ~bit2
bits = bit1 >> 1
print(f'AND bit a bit: {bit1 & bit2}')
print(f'OR bit a bit: {bit1 | bit2}')
print(f'XOR bit a bit: {bit1 ^ bit2}')
print(f'NOT bit a bit {bits}')
print(f'Desplazamiento de bit {bits}')

colores = ['rojo','azul','verde','negro']

contador = 4

while contador > 0:
    
    for x in colores:
        if x == 'verde':
           print('el verde es mi color favoritos')
        elif x == 'negro':
            try:
                colores[3]='rosa'
                print(f'El negro fue sustituido por {colores[3]}')
                continue
            except:
                print('No puede cambiar el valor')
        
        print(x)
        contador -= 1
         
         
#Crea un programa que imprima por consola todos los números comprendidos
 #* entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 #*

for x in range(10,56):
   if x == 16:
       continue
   elif x % 3 == 0:
       continue
   elif x % 2 != 0:
       continue
   else:
        print(x)






