# entrada: massa e volume 
massa = float(input("digite a massa do valor (em kg):" ))
volume = float(input("digite o volume do material (em m³):"))

# processamento: calculo da densidade
densidade = massa / volume

#saida: classificação com base na densidade
if densidade >5:
    print("material muito denso")
elif 2 <= densidade<= 5:
    print("material com densidade media")
else:
    print("material com pouca densidade")