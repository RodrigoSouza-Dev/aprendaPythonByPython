# Definição da classe Pessoa
class Pessoa:
    # Método construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Método de instância
    def saudacao(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

    # Método de instância com parâmetro
    def aumentar_idade(self, anos):
        self.idade += anos

# Criação de objetos (instâncias da classe Pessoa)
pessoa1 = Pessoa("João", 25)
pessoa2 = Pessoa("Maria", 30)

# Acessando atributos e chamando métodos

# Acessando atributos
print(pessoa1.nome)  # Saída: João
print(pessoa2.idade) # Saída: 30

# Chamando métodos
pessoa1.saudacao()  # Saída: Olá, meu nome é João e eu tenho 25 anos.
pessoa2.saudacao()  # Saída: Olá, meu nome é Maria e eu tenho 30 anos.

# Chamando método com parâmetro
pessoa1.aumentar_idade(5)
print(pessoa1.idade)  # Saída: 30

# Herança

# Definição da classe Aluno que herda da classe Pessoa
class Aluno(Pessoa):
    # Método construtor
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)  # Chama o construtor da classe base
        self.matricula = matricula

    # Método de instância sobrescrito
    def saudacao(self):
        print(f"Olá, eu sou o(a) aluno(a) {self.nome}, tenho {self.idade} anos e minha matrícula é {self.matricula}.")

# Criação de objeto da classe Aluno
aluno1 = Aluno("Lucas", 20, "2021001")

# Chamando o método saudacao sobrescrito
aluno1.saudacao()  # Saída: Olá, eu sou o(a) aluno(a) Lucas, tenho 20 anos e minha matrícula é 2021001.
