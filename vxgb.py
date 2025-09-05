a = float(input("digite o valor de a: "))
b = float(input("digite o valor de b: "))
c = float(input("digite o valor de c: "))

# calculo de delta
delta = b**2 - 4*a*c

# saida do valor de delta
print(f"delta = {delta}")

# varificação das raizes
if delta > 0:
    print("a equação tem duas raizes reais,")
elif delta == 0:
    print("a equação tem uma raiz real, ")
else:
    print("a equação não possui raizes reais, ")