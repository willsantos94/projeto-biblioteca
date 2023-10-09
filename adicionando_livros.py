import csv

dados = [
    [input('Digite o nome do livro: '), 
    input('Digite quem é o autor deste livro: '),
    input('Digite qual a editora deste livro: '),
    input('Digite quantas páginas tem este livro: ')]
]

nome_arquivo = 'acervo_biblioteca.csv'

with open(nome_arquivo, 'a', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    for linha in dados:
        escritor_csv.writerow(linha)

while True:
    resposta = input("Deseja adicionar outro livro? (sim/nao)? ").strip().lower()
    
    if resposta == "sim":
        print("Continuando...")
        dados = [
            [input('Digite o nome do livro: '),
             input('Digite quem é o autor deste livro: '),
             input('Digite qual a editora deste livro: '), 
             input('Digite quantas páginas tem este livro: ')]
        ]
        nome_arquivo = 'acervo_biblioteca.csv'

        with open(nome_arquivo, 'a', newline='') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
            for linha in dados:
                escritor_csv.writerow(linha)

    elif resposta == "nao":
        print("Encerrando o programa.")
        print(f'Dados foram salvos em {nome_arquivo}.')
        break  
    else:
        print("Resposta inválida. Por favor, responda com 'sim' ou 'nao'.")
    


