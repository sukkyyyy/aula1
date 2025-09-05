# -*- coding: UTF-8 -*-

class Perfil(object):
    """Classe padrão para perfis de usuários"""

    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0  # atributo privado

    def imprimir(self):
        print(f"Nome: {self.nome}, Telefone: {self.telefone}, Empresa: {self.empresa}")

    def curtir(self):
        """Incrementa as curtidas em +1"""
        self.__curtidas += 1

    def obter_curtidas(self):
        """Retorna o número de curtidas"""
        return self.__curtidas


# ====== Testes ======
if __name__ == "__main__":
    perfil = Perfil("Flávio Almeida", "não informado", "Caelum")

    # Curtindo o perfil 3 vezes
    perfil.curtir()
    perfil.curtir()
    perfil.curtir()

    # Exibindo os dados do perfil e as curtidas
    perfil.imprimir()
    print("Curtidas:", perfil.obter_curtidas())  # Saída esperada: Curtidas: 3
