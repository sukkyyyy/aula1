peso = float(input("digite seu peso: "))
altura = float(input("digite sua altura: "))

imc = peso/(altura * altura)

print("seu Imc é ", imc)
if imc < 18.5:
    print("abaixo do peso")
elif imc < 25:
    print("peso normal")
elif imc < 30:
    print("sobrepeso")
else:
    print("obesidade")