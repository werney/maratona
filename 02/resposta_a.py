from itertools import product
#import time

binario = [0, 1] #Combinação binaria
lista = []  #lista que recebe as combinações
tamanho=int(input()) #Tentativas e tamanho das combinações
#inicio=time.time()
combinacao = product(binario, repeat=tamanho) #combinações possiveis de serem feitas

for i in combinacao:
    lista.append(i) #implementando a lista

cont=0
cont2=0
zero=0
qtd_0=[]

for j in range(2**tamanho): #definindo a quantidade de 0's em cada combinação, mas poderia ser a quantidade de 1's 
    for k in lista[cont2]:
        if k==0:
            zero+=1
    cont2+=1
    qtd_0.append(zero)
    zero=0 #É zerado para que a próxima combinação seja contabilizada novamente
    cont+=1

lista_auxiliar=(sorted(qtd_0))
maior=lista_auxiliar[-1]
quantidade_usada=[] #definindo a quantidade de combinações usadas
cont=0

for l in range(maior+1):
    quantidade_usada.append(qtd_0.count(l)) #aqui é definido a quantidade de vezes que N 0's foram utilizados, se for um numero par, então todos esses N 0's foram usado, se for impar, um 0 não foi usado. 
quantidade_nao_usada=0

for m in quantidade_usada:
    if m%2!=0: #Atravez da quantidade de N 0's usada é definido quantas não foram usadas
        quantidade_nao_usada+=1

print(quantidade_nao_usada)
#fim=time.time()
#print(fim-inicio)