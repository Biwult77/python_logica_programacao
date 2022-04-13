matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0],
]

'''
matrix = [
    [1, 0],
	[1, 0],
	[0, 0],
	[1, 1],
	[1, 0],
]
matrix = [
    [1, 0, 0, 1, 1],
    [1, 0, 1, 1, 0],
]
'''


def mede_rio(matrix, i, j):
    tamanho = 1
    if j+1 < len(matrix[i]) and matrix[i][j+1] == 1:
        matrix[i][j+1] = -1
        tamanho += mede_rio(matrix, i, j+1)
    elif j-1>=0 and matrix[i][j-1] == 1:
        matrix[i][j-1] = -1
        tamanho += mede_rio(matrix, i, j-1)
    elif i+1 < len(matrix) and matrix[i+1][j] == 1:
        matrix[i+1][j] = -1
        tamanho += mede_rio(matrix, i+1, j)
    elif i-1 >=0 and matrix[i-1][j] == 1:
        matrix[i-1][j] = -1
        tamanho += mede_rio(matrix, i-1, j)
    return tamanho

def conta_rios(matrix):
    tamanho_rios = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (matrix[i][j]) == 1:
                matrix[i][j] = -1
                tamanho_rios.append(mede_rio(matrix, i, j))
                print(f'Nova nascente de rio em {i};{j} de tamanho {tamanho_rios[-1]}')
    tamanho_rios.sort()
    return tamanho_rios

print(conta_rios(matrix))