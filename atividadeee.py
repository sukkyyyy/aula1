nota1 = float(input("Digite sua primeira nota: ")) 
nota2 = float(input("Digite sua segunta nota: ")) 
nota3 = float(input("Digite sua terceira nota: ")) 
nota4 = float(input("Digite sua quarta nota: ")) 

media = (nota1 + nota2 + nota3 + nota4)/4 

print("Minha média final é ", media) 

if media >= 5: 
    print("Aprovado(a)") 
else:
    print("Reprovado(a)")