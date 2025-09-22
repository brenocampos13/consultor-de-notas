# Escreva um consultor de notas que peça o nome e a nota do aluno;
# E retorne se eles está aprovado, em recuperação ou se foi rejeitado!

print("==================")
print("CONSULTOR DE NOTAS!")
print("==================")

while True:
        nome = input("Digite o nome do aluno: ")
        try:
            procuraAluno = float(input("Digite a nota do aluno: "))
            if procuraAluno < 0 or procuraAluno > 10.1:
                print("O número precisa ser maior que 0 ou menor que 10, tente Novamente!")
                continue
            elif procuraAluno < 5.1:
                print(f'O aluno {nome} foi REPROVADO pela sua nota {procuraAluno}!')
            elif procuraAluno < 7.1:
                print(f'O aluno {nome} está em RECUPERAÇÃO pela sua nota {procuraAluno}!')
            else:
                print(f'O aluno {nome} foi APROVADO pela sua nota {procuraAluno}!')
        except ValueError:
            print('Digite um número válido!')
            continue
        
        while True:
            tenteNovamente = input("Gostaria de consultar de novo? S/N: ").strip().upper()
            if tenteNovamente in ["Sim", "SIM", "S", "s"]:
                break
            elif tenteNovamente in ["Não", "NÃO", "N", "n"]:
                print("=============================================")
                print("OBRIGADO POR UTILIZAR O CONSULTOR DE NOTAS!")
                print("=============================================")
                exit()
            else:
                (print("Resposta inválida! Digite Sim ou Não!"))
                continue