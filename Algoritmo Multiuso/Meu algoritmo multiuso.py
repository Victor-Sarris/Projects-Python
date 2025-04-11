# nome do usuário 
nome = input("Insira o nome do(a) usuário: ")
# funções do algoritimo
print(f'Bem vindo(a) {nome}! Você está executando o algoritimo de multi-uso. O que você quer fazer agora?')
# funções do algoritimo 
print("Para entrar na biblioeteca PYTHON do W3schools, digiite: \"W3\". Para usar a calculadora, digite: \"CALCULADORA\". Para usar o separador silábico digite: \"SEPARADOR\". Para ver a hora digite \"RELOGIO\".")
funçao = input("Digite aqui: ")
# condição para executar determinado algoritimo
while True:
    if funçao.upper() == 'CALCULADORA':
        while True:
            n1 = float(input("Insira um número qualquer; "))
            operador = input("Insira um operador lógico {+, -, , / ou *}.")
            n2 = float(input("Insira um número qualquer: "))
        
            # condição de operadores lógicos dentro de uma calculadora
            if operador == '+':
                soma = n1 + n2
                print(f'O resultado da soma é: {soma}')
            elif operador =='-':
                subtraçao = n1 - n2
                print(f'O resultado da subtração é {subtraçao}')
            elif operador =='*':
                multiplicaçao = n1*n2
                print(f'O resultado da multiplicação é {multiplicaçao}')
            elif operador =='/':
                divisao = n1/n2
                print(f'O resultado da divisão é {divisao}')
            elif operador == '**':
                potenciaçao = n1**n2
                print(f'O resultado da potenciação é {potenciaçao}')
            continuar = input("Aperte ENTER para continuar ou digite (not) para cancelar a operação: ")
            if continuar == 'not' or continuar == 'NOT':
                print("Algoritimo encerrado!!")
                break
    elif funçao.upper() == 'RELOGIO': # o algoritimo multi-uso vai assumir a função de um relógio
        
        # variavel
        pararelogio = ""
        # importar uma biblioteca de tempo
        import time 
        
        # repetição com While
        print(f'O relogio está sendo executado!')
        print(f'Digite "End" para parar o programa.')
        
        while True:
            #hora atual
            hora_atual = time.localtime(1)
            # hora formatada
            hora_formatada = time.strftime("%H:%M")
            #pausa de 1 segundo
            time.sleep(60)
            print(hora_formatada)

            if pararelogio.upper() == 'END':
                break

    
    elif funçao.upper() == 'SEPARADOR':
    
        palavra = input(f'Insira a palavra que você, {nome}, quer separar silábicamente: ')
        
        for letra in palavra: 
            print(letra)
    elif funçao.upper() == 'W3':

        # importar biblioteca "WebBrowser"
        import webbrowser
        
        # link que será aberto no navegador
        # o link redireciona ao W3SCHOOLS
        url = 'https://www.w3schools.com/python/default.asp'

        # funçao que irá abrir o navegador
        webbrowser.open(url)

        print(f'Abrindo o browser!')

        break
    else:
        continuar = input("Função inválida, aperte ENTER para recomeçar, ou (NOT) para cancelar a operação: ")
        if continuar.upper() == 'NOT':
            print("Algoritimo encerrado!!")
            break