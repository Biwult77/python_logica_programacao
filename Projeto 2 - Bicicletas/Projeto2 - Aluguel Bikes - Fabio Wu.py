lista = [
        [1, 'Caloi', 'Branca', 'disponível', 'nenhum', 0, 'nenhum'],
        [2, 'Caloi', 'Amarela', 'disponível', 'nenhum', 0, 'nenhum'], 
        [3, 'Caloi', 'Azul', 'disponível', 'nenhum', 0, 'nenhum'], 
        [4, 'Caloi', 'Vermelha', 'disponível', 'nenhum', 0, 'nenhum'], 
        [5, 'Caloi', 'Preta', 'disponível', 'nenhum', 0, 'nenhum'], 
        [6, 'BMC', 'Branca', 'disponível', 'nenhum', 0, 'nenhum'], 
        [7, 'BMC', 'Amarela', 'disponível', 'nenhum', 0, 'nenhum'], 
        [8, 'BMC', 'Azul', 'disponível', 'nenhum', 0, 'nenhum'], 
        [9, 'BMC', 'Vermelha', 'disponível', 'nenhum', 0, 'nenhum'], 
        [10, 'BMC', 'Preta', 'disponível', 'nenhum', 0, 'nenhum'], 
        [11, 'Sense', 'Branca', 'disponível', 'nenhum', 0, 'nenhum'], 
        [12, 'Sense', 'Amarela', 'disponível', 'nenhum', 0, 'nenhum'], 
        [13, 'Sense', 'Azul', 'disponível', 'nenhum', 0, 'nenhum'], 
        [14, 'Sense', 'Vermelha', 'disponível', 'nenhum', 0, 'nenhum'], 
        [15, 'Sense', 'Preta', 'disponível', 'nenhum', 0, 'nenhum'], 
        [16, 'Audax', 'Branca', 'disponível', 'nenhum', 0, 'nenhum'], 
        [17, 'Audax', 'Amarela', 'disponível', 'nenhum', 0, 'nenhum'], 
        [18, 'Audax', 'Azul', 'disponível', 'nenhum', 0, 'nenhum'], 
        [19, 'Audax', 'Vermelha', 'disponível', 'nenhum', 0, 'nenhum'], 
        [20, 'Audax', 'Preta', 'disponível', 'nenhum', 0, 'nenhum'], 
        [21, 'Soul', 'Branca', 'disponível', 'nenhum', 0, 'nenhum'], 
        [22, 'Soul', 'Amarela', 'disponível', 'nenhum', 0, 'nenhum'], 
        [23, 'Soul', 'Azul', 'disponível', 'nenhum', 0, 'nenhum'], 
        [24, 'Soul', 'Vermelha', 'disponível', 'nenhum', 0, 'nenhum'], 
        [25, 'Soul', 'Preta', 'disponível', 'nenhum', 0, 'nenhum']
        ]
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        
    def ver_lista(self):
        lista_disponiveis = []
        for n in lista:
            if n[3] == 'disponível':
                lista_disponiveis.append(n)
        print(f'{nome}, temos {len(lista_disponiveis)} bicicletas disponíveis para locação:')
        for i in lista_disponiveis:
            print(f'{i[0]:02d} | {i[1]:>8s} - {i[2]:<10s} | Status: {i[3]:<12s}')
        
    def ver_alugadas(self):
        lista_alugadas = []
        for n in lista:
            if n[3] == 'indisponível':
                lista_alugadas.append(n)
        print(f'{nome}, temos {len(lista_alugadas)} bicicletas alugadas aguardando devolução:')
        for i in lista_alugadas:
            print(f'{i[0]:02d} | {i[1]:>8s} - {i[2]:<10s} | Status: {i[3]:<12s} | Tempo: {i[5]} {i[4]:<14s} | Cliente: {i[6]}')

    def alugar_por_hora(self, horas, bike, quantidade):
        while lista[bike-1][3] == 'indisponível':
            bike = int(input('Bicicleta indisponível para locação. Escolha outra bike:'))
    
        self.horas = horas
        self.bike = int(bike)
        self.quantidade = int(quantidade)
        if self.quantidade >= 3:
            locacao = self.horas * 5 * self.quantidade * 0.7
        else:
            locacao = self.horas * 5 * self.quantidade
        print(f'O valor por {self.horas} hora(s) de locação é de R$ {locacao:.2f}')
        lista[bike-1][3] = 'indisponível'
        lista[bike-1][4] = 'hora(s)'
        lista[bike-1][5] = self.horas
        lista[bike-1][6] = nome

    def alugar_por_dia(self, dias, bike, quantidade):
        while lista[bike-1][3] == 'indisponível':
            bike = int(input('Bicicleta indisponível para locação. Escolha outra bike:'))
        self.dias = dias
        self.bike = int(bike)
        self.quantidade = int(quantidade)
        if self.quantidade >= 3:
            locacao = self.dias * 25 * self.quantidade * 0.7
        else:
            locacao = self.dias * 25 * self.quantidade
        print(f'O valor por {self.dias} dia(s) de locação é de R$ {locacao:.2f}')
        lista[bike-1][3] = 'indisponível'
        lista[bike-1][4] = 'dia(s)'
        lista[bike-1][5] = self.dias
        lista[bike-1][6] = nome
    
    def alugar_por_semana(self, semanas, bike, quantidade):
        while lista[bike-1][3] == 'indisponível':
            bike = int(input('Bicicleta indisponível para locação. Escolha outra bike:'))
        
        self.semanas = semanas
        self.bike = int(bike)
        self.quantidade = int(quantidade)
        if self.quantidade >= 3:
            locacao = self.semanas * 100 * self.quantidade * 0.7
        else:
            locacao = self.semanas * 100 * self.quantidade
        print(f'O valor por {self.semanas} semana(s) de locação é de R$ {locacao:.2f}')
        lista[bike-1][3] = 'indisponível'
        lista[bike-1][4] = 'semana(s)'
        lista[bike-1][5] = self.semanas
        lista[bike-1][6] = nome

    def devolver_bike(self, bike):
        self.bike = int(bike)
        lista[bike-1][3] = 'disponível'
        lista[bike-1][4] = 'nenhum'
        lista[bike-1][5] = 0
        lista[bike-1][6] = 'nenhum'
        print('--------------------------------------------------')
        for i in lista:
            print(f'{i[0]:02d} | {i[1]:>8s} - {i[2]:<10s} | Status: {i[3]:.10s} | Cliente: {i[6]}')

class Loja:
    def __init__(self, nome):
        self.nome = nome
        
    def calcular_valor(self, cliente, tempo = 0):
        self.cliente = cliente
        alugadas_por_cliente = []
        tipo_por_cliente = []
        self.tempo = tempo
        self.tipo = None
        for n in lista:
            if n[6] == cliente:
                alugadas_por_cliente.append(n)
        lista_por_cliente = len(alugadas_por_cliente)
        print(f'{nome}, {cliente} tem {lista_por_cliente} bicicleta(s) alugada(s).')
        print(f'Veja a lista abaixo:')
        for i in alugadas_por_cliente:
            print(f'{i[0]:02d} | {i[1]:>8s} - {i[2]:<10s} | Status: {i[3]:<12s} | Tempo: {i[5]} {i[4]:<9s} | Cliente: {i[6]}')
        print('Selecione o tipo de locação que deseja calcular o valor, entre as opções abaixo:')
        print('1. hora(s)')
        print('2. dia(s)')
        print('3. semana(s)')
        opcao = int(input('Digite o número da sua opção: '))
        if opcao == 1:
            tipo = 'hora(s)'
        elif opcao == 2:
            tipo = 'dia(s)'
        elif opcao == 3:
            tipo = 'semana(s)'
        else:
            print('Opção inválida!')
            opcao = int(input('Digite o número da sua opção: '))

        for x in alugadas_por_cliente:
            if x[4] == tipo:
                tipo_por_cliente.append(n)
                tempo = x[5]
                qtd_por_cliente = len(tipo_por_cliente)
                if tipo == 'hora(s)':
                    if qtd_por_cliente < 3:
                        total = tempo * qtd_por_cliente * 5
                    else:
                        total = tempo * qtd_por_cliente * 5 * 0.7
                elif tipo == 'dia(s)':
                    if qtd_por_cliente < 3:
                        total = tempo * qtd_por_cliente * 25
                    else:
                        total = tempo * qtd_por_cliente * 25 * 0.7
                else:
                    if qtd_por_cliente < 3:
                        total = tempo * qtd_por_cliente * 100
                    else:
                        total = tempo * qtd_por_cliente * 100 * 0.7
        print(total)
        print(f'{nome}, o cliente {cliente} deve {total:.2f} reais por {qtd_por_cliente} bicicletas alugadas por {tempo} {tipo}')


    def mostrar_estoque(self):
        print(f'{nome}, temos {len(lista)} bicicletas no estoque:')
        for i in lista:
                print(f'{i[0]:02d} | {i[1]:>8s} - {i[2]:<10s} | Status: {i[3]:<12s} | Tempo: {i[5]} {i[4]:<9s} | Cliente: {i[6]}')

print('--------------------------------------------------')
print('----------------- MENU DE OPÇÕES -----------------')
print('--------------------------------------------------')
print('1. Ver bicicletas disponíveis')
print('2. Alugar bicicletas por hora')
print('3. Alugar bicicletas por dia')
print('4. Alugar bicicletas por semana')
print('5. Calcular valor final da locação')
print('6. Mostrar estoque de bicicletas')
print('7. Devolver bicicleta')
print('0. Sair')
print('--------------------------------------------------')

nome = input('Informe seu nome: ')
opcao = int(input('Escolha uma das opções acima: '))

while opcao != 0:
    if opcao == 1:
        Loja1 = Loja(nome)
        Cliente.ver_lista(nome)
        
    elif opcao == 2:
        quantidade = int(input('Informe quantas bicicletas você irá alugar: '))
        horas = int(input('Informe quantas horas de locação: '))
        for elemento in range(quantidade):
            bike = int(input('Selecione número da bicicleta a ser alugada: '))
            Cliente1 = Cliente(nome)
            Cliente1.alugar_por_hora(horas, bike, quantidade)

    elif opcao == 3:
        quantidade = int(input('Informe quantas bicicletas você irá alugar: '))
        dias = int(input('Informe quantos dias de locação: '))
        for elemento in range(quantidade):
            bike = int(input('Selecione número da bicicleta a ser alugada: '))
            Cliente1 = Cliente(nome)
            Cliente1.alugar_por_dia(dias, bike, quantidade)

    elif opcao == 4:
        quantidade = int(input('Informe quantas bicicletas você irá alugar: '))
        semanas = int(input('Informe quantas semanas de locação: '))
        for elemento in range(quantidade):
            bike = int(input('Selecione número da bicicleta a ser alugada: '))
            Cliente1 = Cliente(nome)
            Cliente1.alugar_por_semana(semanas, bike, quantidade)
                    
    elif opcao == 5:
        Loja1 = Loja(nome)
        #Cliente.ver_alugadas(nome)
        cliente = input('Informe o nome do cliente: ')
        Loja1.calcular_valor(cliente)

    elif opcao == 6:
        Cliente1 = Loja(nome)
        Loja.mostrar_estoque(nome)

    elif opcao == 7:
        Cliente1 = Cliente(nome)
        Cliente.ver_alugadas(nome)
        bike = int(input('Selecione número da bicicleta a ser devolvida: '))
        Cliente1 = Cliente(nome)
        Cliente1.devolver_bike(bike)

    else:
        print('Opção Inválida!')
    
    print('--------------------------------------------------')
    print('----------------- MENU DE OPÇÕES -----------------')
    print('--------------------------------------------------')
    print('1. Ver bicicletas disponíveis')
    print('2. Alugar bicicletas por hora')
    print('3. Alugar bicicletas por dia')
    print('4. Alugar bicicletas por semana')
    print('5. Calcular valor final da locação')
    print('6. Mostrar estoque de bicicletas')
    print('7. Devolver bicicleta')
    print('0. Sair')
    print('--------------------------------------------------')
    nome = input('Informe seu nome: ')
    opcao = int(input('Escolha uma das opções acima: '))
    
    
print('--------------------------------------------------')
print('------------- Obrigado e até breve! --------------')
print('--------------------------------------------------')
