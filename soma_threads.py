import threading

# Função que calcula a soma de uma parte da lista
def soma_parcial(numeros, resultado, indice):
    """
    Esta função será executada por uma thread.
    Ela calcula a soma da sublista 'numeros' e armazena o resultado
    na lista 'resultado' no índice correspondente.
    """
    resultado[indice] = sum(numeros)

def soma_com_threads(lista):
    """
    Função principal que divide a lista ao meio e cria duas threads
    para calcular a soma de cada parte separadamente.
    """

    meio = len(lista) // 2  # Divide a lista em duas partes
    parte1 = lista[:meio]
    parte2 = lista[meio:]

    resultado = [0, 0]  # Lista para armazenar o resultado de cada thread

    # Criação das threads, passando cada parte e o índice do resultado
    t1 = threading.Thread(target=soma_parcial, args=(parte1, resultado, 0))
    t2 = threading.Thread(target=soma_parcial, args=(parte2, resultado, 1))

    # Inicia as threads
    t1.start()
    t2.start()

    # Aguarda as threads terminarem
    t1.join()
    t2.join()

    # Soma total é a soma dos resultados parciais
    soma_total = sum(resultado)
    return soma_total

# Casos de teste
listas_teste = [
    [1, 2, 3, 4, 5, 6],  # Soma esperada: 21
    list(range(1, 101)), # Soma esperada: 5050
    [10, 20, 30],        # Soma esperada: 60
]

for i, lista in enumerate(listas_teste):
    print(f"Teste {i+1}: Lista = {lista}")
    resultado = soma_com_threads(lista)
    print(f"Soma total: {resultado}\n")

