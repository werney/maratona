
while True:
    V, N = input().split(" ")
    V = int(V); N = int(N) 
    if((1 <= V <= 10000) and (1 <= N <= 10000)):
        break
    print ("VALORES OU VALOR INVÁLIDO(s), FORA DO INTERVALO PERMITIDO (1>= V, N >= 10000)")


NT = V * N
texto = ""

for i in range(1,10):
    P = NT  * (i/10)
    if(round(P) > P):
        P = round(P)
    if(round(P) < P):
        P = round(P)+1
    P = int(P)
    texto += str(P)+" "

print (texto)

