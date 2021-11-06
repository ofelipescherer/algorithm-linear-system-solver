import numpy as np
import os

#Pegando uma matriz da pasta 'matrix'
file = os.path.join('./', 'matrix', 'matrix_1.txt')

#Criando as duas matrizes que serão usadas para resolver
main_matrix = []
second_matrix = []

#Abrindo o arquivo e passando linha por linha
f = open(file, "r")
for i in f:
    #Eh necessario criar um outro array com numeros formatados, porque no split, pode vir um caractere '\n'
    formated_line = []
    line = i.split(',')
    for j in line:
        #Removendo o '\n' quando existir e transformando as strings para numeros
        formated_line.append(float(j.replace('\n',"")))
    
    #Pegando o ultimo valor de cada linha e adicionando a uma matriz separada
    last_number = formated_line[len(formated_line)-1]
    second_matrix.append(last_number)
    formated_line.pop()
    
    #Juntando as linhas em apenas uma matriz
    main_matrix.append(formated_line)
    
#Mostrando como as matriz ficaram depois de lidas
print(f'Matriz a: {main_matrix}')
print(f'Matriz b: {second_matrix}')

#Usando o numpy para resolver o sistema linear 
#Para garantir o calculo, usaremos o metodo de pseudo-inversao de Moore-Penrose de matriz

#Passo 1 (Opcional): Garantir a transformação para um array pelo numpy
#Passo 2: Usar a funcao linalg.pinv na primeira matriz (Ela calcula automaticamente a pseudo-inversao da matriz)
#Passo 3: Fazer a multiplicacao da matriz a com a matriz b. Para isso podemos usar a funcao dot() do numpy
a = np.array(main_matrix)
b = np.array(second_matrix)
    
x = np.linalg.pinv(a).dot(b)

#Mostrando os resultados
print('\nResultados:')
for index,value in enumerate(x):
    print(f'x{index+1}: {round(value, 2)}')