v = int(input('Voutas: '))
n = int(input('Placas: '))

if(1 <= v & n <= (10**4)):

    quantPlacas = ""
    mult = v*n

    for i in range(9):
        
        quantPlacas += str(round((mult*((i+1)*0.1))+.4999)) + "  "


    print(quantPlacas)

else:
    print('Os parametros não são validos  ')