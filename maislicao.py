# Entrada: base e altura do triângulo
base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))

# Processamento: cálculo da área
area = (base * altura) / 2

# Saída: classificação do triângulo
if area > 100:
    print("Triângulo grande")
elif 50 <= area <= 100:
    print("Triângulo médio")
else:
    print("Triângulo pequeno")
