# Faça um consultor de notas de uma escola e por base no nome do aluno,
# Retorne a nota e diga se está aprovado, reprovado ou em recuperação!

print("==================")
print("CONSULTA DE NOTAS")
print("==================")

while True:
        nome = input("Digite o nome do aluno: ")
        try:
            pesquisar_aluno = float(input("Digite a nota do aluno: "))
            if pesquisar_aluno < 0 or pesquisar_aluno > 10.1:
                print("O número tem que ser maior que 0 e menor que 10, tente novamente!")
                continue
            elif pesquisar_aluno < 5.1:
                print(f'O aluno {nome} está reprovado por sua nota {pesquisar_aluno}!')
            elif pesquisar_aluno < 7.1:
                print(f'O aluno {nome} está em recuperação por sua nota {pesquisar_aluno}!')
            else:
                print(f'O aluno {nome} está aprovado por sua excelente nota {pesquisar_aluno}!')
        except ValueError:
            print('Digite um número válido!')
            continue
        
        while True:
            denovo = input("Deseja pesquisar de novo? S/N: ").strip().upper()
            if denovo in ["sim", "SIM", "S", "Si", "SI" "s"]:
                break
            elif denovo in ["Não", "Nao", "N", "No", "NO", "n"]:
                print("=============================================")
                print("OBRIGADO POR UTILIZAR A CONSULTORA DE NOTAS!")
                print("=============================================")
                exit()
            else:
                (print("Resposta inválida! Digite SIM ou NÃO!"))
                continue