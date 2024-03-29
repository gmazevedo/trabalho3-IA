import numpy as np

#Constantes
X = 0
Y = 1

def h(theta_0, theta_1, xi):
    return theta_0 + theta_1*xi


def compute_mse(theta_0, theta_1, data):
    """
    Calcula o erro quadratico medio
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :return: float - o erro quadratico medio
    """
    mse = 0
    somatorio = 0
    n = 0

    for i in data:
        h0 = h(theta_0, theta_1, data[n][X])
        somatorio += pow(h0 - data[n][Y], 2) 
        n += 1
    
    mse = (1/n)*somatorio

    return mse


def step_gradient(theta_0, theta_1, data, alpha):
    """
    Executa uma atualização por descida do gradiente  e retorna os valores atualizados de theta_0 e theta_1.
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :return: float,float - os novos valores de theta_0 e theta_1, respectivamente
    """    
    #Calculando o novo theta 0
    somatorio = 0
    n = 0

    for i in data:
        h0 = h(theta_0, theta_1, data[n][X])
        somatorio += h0 - data[n][Y]
        n += 1
    
    d_theta_0 = (2/n)*somatorio
    new_theta_0 = theta_0 - alpha*d_theta_0

    #Calculando o novo theta 1
    somatorio = 0

    for i in range(0, n):
        h0 = h(theta_0, theta_1, data[i][X])
        somatorio += (h0 - data[i][Y])*data[i][X]

    d_theta_1 = (2/n)*somatorio
    new_theta_1 = theta_1 - alpha*d_theta_1

    return new_theta_0, new_theta_1


def fit(data, theta_0, theta_1, alpha, num_iterations):
    """
    Para cada época/iteração, executa uma atualização por descida de
    gradiente e registra os valores atualizados de theta_0 e theta_1.
    Ao final, retorna duas listas, uma com os theta_0 e outra com os theta_1
    obtidos ao longo da execução (o último valor das listas deve
    corresponder à última época/iteração).

    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :param num_iterations: int - numero de épocas/iterações para executar a descida de gradiente
    :return: list,list - uma lista com os theta_0 e outra com os theta_1 obtidos ao longo da execução
    """
    theta_0_list = [theta_0]
    theta_1_list = [theta_1]

    for i in range(num_iterations):
        theta_0, theta_1 = step_gradient(theta_0, theta_1, data, alpha)
        theta_0_list.append(theta_0)
        theta_1_list.append(theta_1)

    return theta_0_list, theta_1_list


