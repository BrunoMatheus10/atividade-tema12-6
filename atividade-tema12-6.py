# Inicializa as variáveis para armazenar o maior e o menor valor
primeiro_numero = True  # Variável para verificar se é o primeiro número digitado
maior = 0
menor = 0

# Solicita ao usuário que digite o primeiro número
numero = int(input("Digite um número inteiro (0 para terminar): "))

# Laço while para continuar lendo números até que o usuário digite zero
while numero != 0:
    if primeiro_numero:
        # Se for o primeiro número, inicializa maior e menor com o valor digitado
        maior = numero
        menor = numero
        primeiro_numero = False
    else:
        # Atualiza o maior e o menor valor
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    # Solicita o próximo número
    numero = int(input("Digite um número inteiro (0 para terminar): "))

# Verifica se algum número foi digitado
if not primeiro_numero:
    print("O maior número digitado foi:", maior)
    print("O menor número digitado foi:", menor)
else:
    print("Nenhum número foi digitado.")
