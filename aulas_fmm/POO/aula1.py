"""
Primeira aula de Progrmação Orientada Objeto
Classe == estrutura, modelo pra ter os objetos, nunca um objeto existe sem uma classe 
uma classe pode dar origem a varios objetos 
Atributo == caracteristicas == variavel / exemplo: altura 
Metodos == açoes de uma classe / exemplo: andar , comer , dormir 
Objeto == nao existe sem a classe, são instancias das classes 
Varios objetos formam um programa


Abstrair == Definir a classe == quais atributos os objetos 
quais sao os métodos sao necessarios 

"""
class Carro:
    cor = 'sem cor'
    marca = 'sem marca'
    modelo = 'sem modelo'
    ano = 2025 
    kmRodados = 0
    
    def detalhes(self):
        print('\n*** Dados do Carro ***')
        print('Cor:', self.cor)
        print('Marca:', self.marca)
        print('Modelo:', self.modelo)
        print('Ano:', self.ano)
        print('Km rodados:', self.kmRodados)

    def adicionarKmRodados(self, km):
        self.kmRodados = self.kmRodados + km

c1 = Carro()
c1.cor = 'Vermelho'
c1.marca = 'Honda'
c1.modelo = 'HR-V'
c1.ano = 2025
c1.detalhes()

c2 = Carro()
c2.cor = 'Prata'
c2.marca = 'VolksWagen'
c2.modelo = 'Voyage'
c2.ano = 2024
c2.kmRodados = 3000
c2.detalhes()

Carro.detalhes(c1)
Carro.detalhes(c2)


c1.adicionarKmRodados(450)
c1.detalhes()

