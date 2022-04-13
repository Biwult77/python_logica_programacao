import json
import os.path
import sys

def obter_dados():
    '''
    Essa função carrega os dados dos produtos e retorna uma lista de dicionários, onde cada dicionário representa um produto.
    NÃO MODIFIQUE essa função.
    '''
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados

def listar_categorias(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista contendo todas as categorias dos diferentes produtos.
    Cuidado para não retornar categorias repetidas.    
    '''
    
    lista_categorias = []
    for categorias in dados:
        if categorias['categoria'] not in lista_categorias:
            lista_categorias.append(categorias['categoria'])
    lista_categorias.sort()
    print(lista_categorias)
    return lista_categorias

dados = obter_dados()

def listar_por_categoria(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar uma lista contendo todos os produtos pertencentes à categoria dada.
    '''
    
    lista_geral = []
    for produto in dados:
        if produto['categoria'] == categoria:
            lista_geral.append({produto['id'],produto['preco']})
    print(lista_geral)
    print('A categoria', categoria, 'contém', len(lista_geral), 'produto(s)')
    return lista_geral

dados = obter_dados()

def produto_mais_caro(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
        
    maior = 0
    mais_caro = {}
    for elemento in dados:
        if elemento['categoria'] == categoria:
            elemento['preco'] = float(elemento['preco'])
            if (elemento['preco']) > maior:
                produto_mais_caro = []
                produto_mais_caro.append({elemento['id'], elemento['preco']})
                maior = elemento['preco']
    mais_caro.update(produto_mais_caro)
    print('O produto mais caro da categoria', categoria, 'é', mais_caro)
    return mais_caro

dados = obter_dados()

def produto_mais_barato(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    menor = 1000000
    mais_barato = {}
    for elemento in dados:
        if elemento['categoria'] == categoria:
            elemento['preco'] = float(elemento['preco'])
            if (elemento['preco']) < menor:
                produto_mais_barato = []
                produto_mais_barato.append({elemento['id'], elemento['preco']})
                menor = elemento['preco']
    mais_barato.update(produto_mais_barato)
    print('O produto mais bararto da categoria', categoria, 'é', mais_barato)
    return mais_barato

dados = obter_dados()

def top_10_caros(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    '''
    lista = [None]*10
    lista_precos = []
    for elementos in dados:
        lista_precos.append(float(elementos['preco']))
    lista_precos.sort(reverse=True)
    lista_10_maiores = lista_precos[:10]
    for produto in dados:
        if float(produto['preco']) in lista_10_maiores:
            indice = lista_10_maiores.index(float(produto['preco']))
            lista[indice] = produto
    return lista

dados = obter_dados()

def top_10_baratos(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    '''
    lista = [None]*10
    lista_precos = []
    for elementos in dados:
        lista_precos.append(float(elementos['preco']))
    lista_precos.sort()
    lista_10_menores = lista_precos[:10]
    for produto in dados:
        if float(produto['preco']) in lista_10_menores:
            indice = lista_10_menores.index(float(produto['preco']))
            lista[indice] = produto
    return lista

dados = obter_dados()

def menu(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá, em loop, realizar as seguintes ações:
    - Exibir as seguintes opções:
        1. Listar categorias
        2. Listar produtos de uma categoria
        3. Produto mais caro por categoria
        4. Produto mais barato por categoria
        5. Top 10 produtos mais caros
        6. Top 10 produtos mais baratos
        0. Sair
    - Ler a opção do usuário.
    - No caso de opção inválida, imprima uma mensagem de erro.
    - No caso das opções 2, 3 ou 4, pedir para o usuário digitar a categoria desejada.
    - Chamar a função adequada para tratar o pedido do usuário e salvar seu retorno.
    - Imprimir o retorno salvo. 
    O loop encerra quando a opção do usuário for 0.
    '''
    print('----------------------------------------')
    print('------------ MENU DE OPÇÕES ------------')
    print('----------------------------------------')
    print('1. Listar categorias')
    print('2. Listar produtos de uma categoria')
    print('3. Produto mais caro por categoria')
    print('4. Produto mais barato por categoria')
    print('5. Top 10 produtos mais caros')
    print('6. Top 10 produtos mais baratos')
    print('0. Sair')
    
    opcao = int(input('Escolha uma das opçóes acima: '))

    while opcao != 0:
        if opcao == 1:
            print(listar_categorias(dados))

        elif opcao == 2:
            categoria = input('Digite a categoria: ')
            listar_por_categoria(dados, categoria)

        elif opcao == 3:
            categoria = input('Digite a categoria: ')
            produto_mais_caro(dados, categoria)

        elif opcao == 4:
            categoria = input('Digite a categoria: ')
            produto_mais_barato(dados, categoria)
                        
        elif opcao == 5:
            top_10_caros(dados)
            print('Os 10 produtos mais caros são:')
            print(top_10_caros(dados))
            
        elif opcao == 6:
            top_10_baratos(dados)
            print('Os 10 produtos mais baratos são:')
            print(top_10_baratos(dados))

        else:
            print('Opção Inválida!')
        
        print('----------------------------------------')
        print('------------ MENU DE OPÇÕES ------------')
        print('----------------------------------------')
        print('1. Listar categorias')
        print('2. Listar produtos de uma categoria')
        print('3. Produto mais caro por categoria')
        print('4. Produto mais barato por categoria')
        print('5. Top 10 produtos mais caros')
        print('6. Top 10 produtos mais baratos')
        print('0. Sair')
        opcao = int(input('Escolha uma das opções acima: '))
        
        
    print('--------------------------------------')
    print('------ Obrigado e até breve! ---------')
    print('--------------------------------------')
...
dados = obter_dados()

# Programa Principal - não modificar!
d = obter_dados()
menu(d)



