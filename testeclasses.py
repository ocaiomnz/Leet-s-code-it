class estudante:
    nome =  ''
    matricula = ''
    creditos = 0
    def addcrd (self, ponto):
        self.creditos= int(self.creditos + ponto)
    def novonome (self, nomenovo):
        self.nome = nomenovo

aluno1 = estudante()
aluno1.novonome('Caio B')
aluno1.novonome('CAIO BAIBAI')
aluno2=  estudante()
aluno1.addcrd(78)
print(aluno1.nome)
print(aluno1.creditos)