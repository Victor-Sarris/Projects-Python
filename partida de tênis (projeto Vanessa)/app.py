# import de bibliotecas
from datetime import datetime # importação da biblioteca 

# Variáveis para armazenar os pontos dos jogadores
pontos_jogador1 = 0
pontos_jogador2 = 0

# Função para atualizar a pontuação
def atualizar_pontos(vencedor):
    global pontos_jogador1, pontos_jogador2
    if vencedor == 1:
        pontos_jogador1 += 3  # Vitória dá 3 pontos
        pontos_jogador2 += 1  # Derrota dá 1 ponto como consolação
    elif vencedor == 2:
        pontos_jogador2 += 3
        pontos_jogador1 += 1


# Função para exibir o placar em tempo real
def exibir_placar():
    print("\n=== PLACAR ATUAL ===")
    print(f"{jogador1}: {pontos_jogador1} pontos")
    print(f"{jogador2}: {pontos_jogador2} pontos")
    print("======================\n")

# CADASTRO DE JOGADORES
jogador1 = input("digite seu nome: ")
endereço = input("digite seu endereço: ") 
telefone = int(input("digite um telefone para contato: "))
dn = input("qual a sua data de nascimento? ")
id = int(input("qual a sua idade? "))
nivel_abilidade = int(input("Qual o seu nivel de abilidade? \n[1]Iniciante\n[2]Intermediário\n[3]Avançado\n:"))


if nivel_abilidade == 1 or nivel_abilidade == 2 or nivel_abilidade == 3:
       print("OK")
else:
      print("opção invalida")
numeroD=int(input("qual o numero de derrotas?"))
numeroV=int(input("qual o numero de vitorias? "))

# AGENDAMENTO DA QUADRA JOGADOR ------------------------------------------------------------------------

print("AGENDAMENTO DA QUADRA PARA JOGADOR")
def horario_quadra():# sobre o horario de agendamento
    while True: 
        horario_input = input("Digite o horário para agendamento ")
        try: # para gerar erro se didgitar errado 
            horario = datetime.strptime(horario_input, "%H:%M")
            return horario
        except ValueError:# é como se fosse o senão do try , senão estiver de acordo com try vai gerar o print de erro do except
            print("Você inseriu um horário com formato inválido. Tente novamente!")

   # colocar a data somente a partir de 2024
def data_agendamento():
    while True:
        dt_agendamento_input = input("Digite a data para agendamento (formato DD/MM/AAAA):")
        try:
            dt_agendamento = datetime.strptime(dt_agendamento_input, "%d/%m/%Y") # determine = Converte a string para um objeto de data. # strptime = converte em um abjeto que possa ser usado para manipulação
            
            # Verifica se o ano da data é maior ou igual a 2024
            if dt_agendamento.year >= 2024 or dt_agendamento.day >= 10: #year é usado para acessar o ano do obejeto de tipo determine 
                return dt_agendamento
            else:
                print("Verifique a data, e tente novamente!")
        except ValueError:
            print("Você digitou o formato da data errado. Tente novamente!")

# Contador de agendamentos
agendamentos_feitos = 0 # minimo de limite 
max_agendamentos = 6  # Limite de 6 agendamentos maximo 


# Loop para agendar até 6 quadras
while agendamentos_feitos < max_agendamentos:
    print(f"Agendamento {agendamentos_feitos + 1} de {max_agendamentos}")

    # Captura o horário de agendamento
    horario = horario_quadra()
    
    # Captura e valida a data de agendamento a partir de 2024
    dt_agendamento = data_agendamento()
    
    QD = int(input("Qual quadra deseja agendar: \n[1] Quadra\n[2] Quadra\n[3] Quadra\n[4] Quadra\n[5] Quadra\n[6] Quadra\n"))


    if 1 <= QD <= 6:
        print("Agendamento realizado com sucesso!")
        agendamentos_feitos += 1  # Incrementa o número de agendamentos feitos
    else:
        print("Opção inválida. Tente novamente.")
        continue  # Retorna ao início do loop sem contar como agendamento

    # Pergunta se o usuário deseja continuar ou parar
    if agendamentos_feitos < max_agendamentos:
        continuar2 = input("Deseja continuar o agendamento? [S/N]: ").strip().lower()
        if continuar2 != 's':
            print("Agendamento encerrado.")
            break

print(f"Você realizou {agendamentos_feitos} agendamentos .")


# JOGADOR 2 --------------------------------------------------------------

jogador2 = str(input('digite o nome do segundo jogador: '))
endereço2 = str(input('digite seu endereço: '))  
telefone2 = int(input('digite um telefone para contato: '))
dn2 = input('qual a sua data de nascimento? ')
id2 = int(input("qual a sua idade? "))
nivel_abilidade2 = int(input("Qual o seu nivel de abilidade? \n[1]Iniciante\n[2]Intermediário\n[3]Avançado\n"))


if nivel_abilidade2 == 1 or nivel_abilidade2 == 2 or nivel_abilidade2 == 3:
       print('OK')
else:
      print('opção invalida!')
numeroD2 = int(input("qual o numero de derrotas? "))
numeroV2 = int(input("qual o numero de vitorias? "))
print("")
print("")



#AGENDAMENTO DA QUADRA  jogador2 -----------------------------------------------------------
print("AGENDAMENTO DA QUADRA PARA JOGADOR 2")
def horario_quadra2():# sobre o horario de agendamento
    while True: 
        horario_input2 = input("Digite o horário para agendamento ")
        try: # para gerar erro se didgitar errado 
            horario = datetime.strptime(horario_input2, "%H:%M")
            return horario
        except ValueError:# é como se fosse o senão do try , senão estiver de acordo com try vai gerar o print de erro do except
            print("Você digitou o formato do horário errado. Tente novamente.")

   # colocar a data somente a partir de 2024
def data_agendamento():
    while True:
        dt_agendamento2_input = input("Digite a data para agendamento (formato DD/MM/AAAA):")
        try:
            dt_agendamento2 = datetime.strptime(dt_agendamento2_input, "%d/%m/%Y") # determine = Converte a string para um objeto de data. # strptime = converte em um abjeto que possa ser usado para manipulação
            
            # Verifica se o ano da data é maior ou igual a 2024
            if dt_agendamento2.year >= 2024 or dt_agendamento2.day >= 10: #year é usado para acessar o ano do obejeto de tipo determine 
                return dt_agendamento2
            else:
                print("Verifique a data, e tente novamente!")
        except ValueError:
            print('Você digitou o formato da data errado. Tente novamente.')



# Contador de agendamentos
agendamentos_feitos2 = 0 # minimo de limite 
max_agendamentos2 = 6  # Limite de 6 agendamentos maximo 

# Loop para agendar até 6 quadras
while agendamentos_feitos2 < max_agendamentos2:
    print(f"Agendamento {agendamentos_feitos2 + 1} de {max_agendamentos2}")

    # Captura o horário de agendamento
    horario = horario_quadra2()
    
    # Captura e valida a data de agendamento a partir de 2024
    dt_agendamento = data_agendamento()
    
    QD2 = int(input("Qual quadra deseja agendar: \n[1] Quadra\n[2] Quadra\n[3] Quadra\n[4] Quadra\n[5] Quadra\n[6] Quadra\n"))
    
    if 1 <= QD2 <= 6:
        print("Agendamento realizado com sucesso!")
        agendamentos_feitos2 += 1  # Incrementa o número de agendamentos feitos
    else:
        print("Opção inválida. Tente novamente.")
        continue  # Retorna ao início do loop sem contar como agendamento

    # Pergunta se o usuário deseja continuar ou parar
    if agendamentos_feitos2 < max_agendamentos2:
        continuar2 = input("Deseja continuar o agendamento? [S/N]: ").strip().lower()
        if continuar2 != 's':
            print("Agendamento encerrado.")
            break

print(f"Você realizou {agendamentos_feitos2} agendamentos .")


# Simulação de uma partida
print("\n=== INÍCIO DA PARTIDA ===")

continuar = 's'
while continuar == 's':
    # Simular quem venceu a partida
    vencedor = int(input("Quem venceu a partida? [1] Jogador 1, [2] Jogador 2: "))

    # Atualizar a pontuação
    atualizar_pontos(vencedor)

    # Exibir o placar em tempo real após a atualização
    exibir_placar()

    # Perguntar se deseja continuar
    continuar = input("Deseja jogar outra partida? [S/N]: ").strip().lower()

    if continuar == 'não':
        break

print("Fim do jogo!")