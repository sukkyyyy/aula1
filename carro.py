# def cria funções (ou metodos dentro da classe)
class Carro:
    marca = ""
    modelo = ""
    ano = 0
    cor = ""

    def buzinar(self):
        print("BI-BI-FO-FOMM")
    def ligar(self):
        print("O Carro Foi Roubado...")
        #
        #
        #
        #

c1 = Carro()
c1.marca = "Nissan"
c1.modelo = "Nissan GT3"
c1.ano = 2006
c1.cor = "Azul"

print("Carro: ", c1.marca, "-", c1.modelo, "ano", c1.ano, "cor", c1.cor)
c1.ligar()
c1.buzinar()