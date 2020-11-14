#import time
voltas_placas=input().split(' ')
#inicio=time.time()
n,v=voltas_placas
n,v=int(n),int(v)
total_de_placas=n*v
lista_placas=[]


for j in range(10,91,10):
    if (total_de_placas*(j/100))%1==0:
        lista_placas.append(round(j/100*total_de_placas))
    else: 
        lista_placas.append(round(j/100*total_de_placas+0.5))
print(' '.join(map(str,lista_placas))) 


#fim=time.time()
#print(fim-inicio)