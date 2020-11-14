import math
from datetime import datetime

ent = input("Entrada: ")
ent = ent.split(" ")

dt = datetime.now()
antes = dt.microsecond

lista = []

if int(ent[0]) >= 1 and int(ent[1]) <= 10 ** 4:
	quantPlacas = int(ent[0]) * int(ent[1])
	for c in range(1, 10):
		gamb = f"0.{c}"
		gamb = float(gamb)
		lista.append(str(math.ceil(quantPlacas * gamb)))
	print(" ".join(lista))
	
ps = datetime.now()
depois = ps.microsecond

print(f"Milissegundos: {(depois - antes) / 1000}")

# 40 minutos