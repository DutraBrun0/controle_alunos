alunos = []


def pagina_inicial():
    while True:
        print('===== CADASTRO DE ALUNOS =====')
        print('Bem vindo ao cadastro de alunos.')
        print('''
                [1] - Cadastrar Aluno
                [2] - Listar Alunos
                [3] - Buscar Aluno
                [4] - Calcular Média da Turma
                [5] - Mostrar Aluno com maior média
                [6] - Sair
    ''')
        opcao = int(input('Oque deseja:'))

        if opcao == 1:
            cadastro_aluno()
        elif opcao == 2:
            listar_alunos()
        elif opcao == 3:
            buscar_aluno()
        elif opcao == 4:
            media_turma()
        elif opcao == 5:
            maior_media()

        elif opcao == 6:
            break

def cadastro_aluno():
    print('===== Cadatro de aluno =====')
    nome = str(input('Qual o nome do aluno:'))
    idade = int(input('Qual a idade do aluno:'))
    nota1 = float(input('nota 1:'))
    nota2 = float(input('nota 2:'))
    media = (nota1+nota2) /2
    aluno = {
        'Nome': nome,
        'Idade': idade,
        'Nota 1': nota1,
        'Nota 2': nota2,
        'Média': media
    }
    alunos.append(aluno)
    print('Aluno Cadastrado')
    print('='*20)

def listar_alunos():
    print('===== Lista de alunos =====')
    if not alunos:
        print('Nenhum aluno cadastrado')
    for aluno in alunos:
        print(f'o aluno {aluno["Nome"]} ,com {aluno["Idade"]} anos, tem as seguintes notas: {aluno["Nota 1"]} e {aluno["Nota 2"]}, com a média de {aluno["Média"]}')
    print('='*20)

def buscar_aluno():
    encontrado = False
    print('===== Busca de Alunos =====')
    busca = str(input('Digite o nome do aluno:'))
    for aluno in alunos:
        if aluno["Nome"] == busca:
            print(f'nome: {aluno["Nome"]} | idade: {aluno["Idade"]} | notas: {aluno["Nota 1"]} e {aluno["Nota 2"]} | com média {aluno["Média"]}')
            encontrado = True
    if encontrado == False:
        print('Busca Inválida')

def media_turma():
    if not alunos:
        print('não possui alunos')
        return
    soma = 0
    for aluno in alunos:
        soma += aluno["Média"]
    total = len(alunos)
    media = soma / total

    print(f'A média da turma é {media}')

def maior_media():
    if not alunos:
        print('Não possui alunos')
        return

    maior = 0
    aluno_maior =''
    for aluno in alunos:
        if maior == 0:
            maior = aluno["Média"]
            aluno_maior = aluno["Nome"]
        else:
            if maior < aluno["Média"]:
                maior = aluno["Média"]
                aluno_maior = aluno["Nome"]
    print(f'O {aluno_maior} tem a maior média da sala, com {maior} de Média')

pagina_inicial()