
quantidade_de_alunos = int(input("Digite a quantidade de alunos: "))

# lista que armazenará a média de cada aluno
media_de_todos_os_alunos = []

# lista que armazenará as notas de cada aluno
notas_de_todos_os_alunos = []

for i in range(0, quantidade_de_alunos):
    num_aluno = i + 1

    # atenção que float é com ponto e não com vírgula
    nota1 = input(f"Digite a nota 1 do aluno {num_aluno}: ")
    nota2 = input(f"Digite a nota 2 do aluno {num_aluno}: ")
    nota3 = input(f"Digite a nota 3 do aluno {num_aluno}: ")
    notas_de_um_aluno = [float(nota1), float(nota2), float(nota3)]

    # inclui as notas de um aluno na lista de notas de todos os alunos
    notas_de_todos_os_alunos.append(notas_de_um_aluno)

    # inclui a média de um aluno na lista de média de todos os alnos
    media_de_todos_os_alunos.append(sum(notas_de_um_aluno) / 3)


mediatotal = sum(media_de_todos_os_alunos) / quantidade_de_alunos


print("\nOs alunos que estao acima da media e suas notas sao:")

for i, media in enumerate(media_de_todos_os_alunos):
    if media >= mediatotal:
        print(f"\nAluno {i + 1} está acima da média, com média: {media:.2f}")
        print(f"Suas notas são: {notas_de_todos_os_alunos[i][0]:.2f}, {notas_de_todos_os_alunos[i][1]:.2f} e {notas_de_todos_os_alunos[i][2]:.2f}")
