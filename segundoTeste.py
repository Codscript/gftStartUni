'''
Considerando os conceitos de Orientação a Objetos, crie uma classe abstrata Pai de nome Pessoa, contendo os atributos (nome, rg)

Crie uma Classe Filha chamada Funcionario, contendo os atributos (salario_inicial, percentual e salario_total) encapsulados, com seus respectivos seletores (getters) e modificadores (setters).

Criar uma classe principal que instancie o objeto Funcionario com as regras abaixo:
Um funcionário de uma empresa recebe aumento salarial anualmente.Sabe - se que:
Esse funcionário foi contratado em 2016, com salário inicial de R$ 1.000,00. Em 2017, ele recebeu aumento de 1,5 % sobre seu salário inicial.
A partir de 2018(inclusive), os aumentos salariais sempre corresponderam ao dobro do percentual do ano anterior.
Faça um programa que informe o Nome, RG e o salário em 2020 desse funcionário.


'''
class Pessoa:
    def __init__(self, nome, rg):
        self.nome = nome
        self.idade = idade


    def falar(self):
        print(f'{self.nome} está falando.')


class Funcionário(Pessoa):
    def comprar(self, produto):
        print(f'{self.nome} está comprando {produto}.')


class Aluno(Pessoa):
    def estudar(self, assunto):
        print(f'{self.nome} está estudando {assunto}.')