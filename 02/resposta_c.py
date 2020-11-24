N = int(input("N: "))

if(2 <= N <= (10**18) ):
    if(0 == (N/2)):
        print(2)
    else:
        print(4)
else:
    print("O número digitado deve pertencer ao INTERVALO{x E N|2>= x >= 10^18}")