# Inicializa as variáveis para armazenar o maior e o menor valor
primeiro_numero = True  # Variável para verificar se é o primeiro número digitado
maior = 0  # Variável para armazenar o maior número digitado
menor = 0  # Variável para armazenar o menor número digitado

# Solicita ao usuário que digite o primeiro número
numero = int(input("Digite um número inteiro (0 para terminar): "))  # Lê o primeiro número digitado pelo usuário

# Laço while para continuar lendo números até que o usuário digite zero
while numero != 0:  # Continua o laço enquanto o número digitado não for zero
    if primeiro_numero:  # Verifica se é o primeiro número digitado
        # Se for o primeiro número, inicializa maior e menor com o valor digitado
        maior = numero  # Define o maior número como o primeiro número digitado
        menor = numero  # Define o menor número como o primeiro número digitado
        primeiro_numero = False  # Define que o primeiro número já foi digitado
    else:
        # Atualiza o maior e o menor valor
        if numero > maior:  # Verifica se o número digitado é maior que o maior número atual
            maior = numero  # Atualiza o maior número
        if numero < menor:  # Verifica se o número digitado é menor que o menor número atual
            menor = numero  # Atualiza o menor número

    # Solicita o próximo número
    numero = int(input("Digite um número inteiro (0 para terminar): "))  # Lê o próximo número digitado pelo usuário

# Verifica se algum número foi digitado
if primeiro_numero == False:  # Verifica se pelo menos um número foi digitado
    print("O maior número digitado foi:", maior)  # Imprime o maior número digitado
    print("O menor número digitado foi:", menor)  # Imprime o menor número digitado
else:
    print("Nenhum número foi digitado.")  # Imprime uma mensagem se nenhum número foi digitado
