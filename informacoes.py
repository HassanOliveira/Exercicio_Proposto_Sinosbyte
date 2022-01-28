from aluno import Aluno


alunos = [
    {'codigo': 1001, 'nome': 'Hassan Oliveira', 'nota1': 9.6, 'nota2': 9.1},
    {'codigo': 1002, 'nome': 'Anderson Rodrigues', 'nota1': 8.3, 'nota2': 8.7},
    {'codigo': 1003, 'nome': 'Joana Osasco', 'nota1': 6.7, 'nota2': 7.5},
    {'codigo': 1004, 'nome': 'Gabriela Nunes', 'nota1': 9.8, 'nota2': 9.2},
    {'codigo': 1005, 'nome': 'João Vitor', 'nota1': 4.2, 'nota2': 6.3},
]

Lista_de_alunos = []

for aluno in alunos:
    Lista_de_alunos.append(Aluno(aluno['codigo'], aluno['nome'], aluno['nota1'], aluno['nota2']))

def solicitacao(codigo: int) -> aluno:
    for aluno in Lista_de_alunos:
        if codigo == aluno.codigo:
            return aluno
        else:
            codigo: int = int(input('Digite o código do aluno (1001 a 1005): '))
            return solicitacao(codigo)

codigo: int = int(input('Digite o código do aluno (1001 a 1005): '))
aluno = solicitacao(codigo)
print(aluno)





