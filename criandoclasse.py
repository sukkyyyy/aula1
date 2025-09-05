#Classe chamada Pessoa
class Pessoa:
    nome= ""
    idade= 0
    cidade= 0
    profissão= 0

#Primeira Pessoa
p1 = Pessoa()
p1.nome = "Leandrinha"
p1.idade = 17
p1.cidade = "Osasco"
p1.profissão = "Mendingo"

#Segunda Pessoa
p2 = Pessoa()
p2.nome = "Gabriel Oliveira"
p2.idade = 16
p2.cidade = "Xique-Xique"
p2.profissão = "Job"

#Tercera Pessoa
p3 = Pessoa()
p3.nome = "Matheus Pizzo"
p3.idade = 8
p3.cidade = "Favela Da Rocinha"
p3.profissão = "Magnata Do Regresso"

#Quarta Pessoa
p4 = Pessoa()
p4.nome = "Luan"
p4.idade = 16
p4.cidade = "Manaus"
p4.profissão = "Pedreiro"

#Quinta Pessoa
p5 = Pessoa()
p5.nome = "Morais"
p5.idade = 16
p5.cidade = "Favela De Dharavi"
p5.profissão = "Aviãozinho"

#Imprimindo dados
print("Pessoa 1: ", p1.nome, "-", p1.idade, "anos")
print("Pessoa 2: ", p2.nome, "-", p2.idade, "anos")
print("Pessoa 3: ", p3.nome, "-", p3.idade, "anos")
print("Pessoa 4: ", p4.nome, "-", p4.idade, "anos")
print("Pessoa 5: ", p5.nome, "-", p5.idade, "anos")