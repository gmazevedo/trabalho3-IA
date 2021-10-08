import random

def evaluate(individual):
    """
    Recebe um indivíduo (lista de inteiros) e retorna o número de ataques
    entre rainhas na configuração especificada pelo indivíduo.
    Por exemplo, no individuo [2,2,4,8,1,6,3,4], o número de ataques é 9.

    :param individual:list
    :return:int numero de ataques entre rainhas no individuo recebido
    """

    number_attacks = 0

    for i in range(7):
        column = i + 1
        while column <= 7:
            if (individual[column] == individual[i] + column - i) or (
                individual[column] == individual[i] - column + i) or (
                individual[column] == individual[i]):
                number_attacks += 1
            column += 1

    return number_attacks


def tournament(participants):
    """
    Recebe uma lista com vários indivíduos e retorna o melhor deles, com relação
    ao numero de conflitos
    :param participants:list - lista de individuos
    :return:list melhor individuo da lista recebida
    """
    best_participant = participants[0]

    for participant in participants:
        if evaluate(participant) < evaluate(best_participant):
            best_participant = participant

    return best_participant


def crossover(parent1, parent2, index):
    """
    Realiza o crossover de um ponto: recebe dois indivíduos e o ponto de
    cruzamento (indice) a partir do qual os genes serão trocados. Retorna os
    dois indivíduos com o material genético trocado.
    Por exemplo, a chamada: crossover([2,4,7,4,8,5,5,2], [3,2,7,5,2,4,1,1], 3)
    deve retornar [2,4,7,5,2,4,1,1], [3,2,7,4,8,5,5,2].
    A ordem dos dois indivíduos retornados não é importante
    (o retorno [3,2,7,4,8,5,5,2], [2,4,7,5,2,4,1,1] também está correto).
    :param parent1:list
    :param parent2:list
    :param index:int
    :return:list,list
    """

    # interchanging the genes
    for i in range(index, len(parent1)):
        parent1[i], parent2[i] = parent2[i], parent1[i]
    
    return parent1, parent2


def mutate(individual, m):
    """
    Recebe um indivíduo e a probabilidade de mutação (m).
    Caso random() < m, sorteia uma posição aleatória do indivíduo e
    coloca nela um número aleatório entre 1 e 8 (inclusive).
    :param individual:list
    :param m:int - probabilidade de mutacao
    :return:list - individuo apos mutacao (ou intacto, caso a prob. de mutacao nao seja satisfeita)
    """

    new_individual = individual

    if(random.random() < m):
        posi = random.randint(0,7)
        val = random.randint(1,8)

        new_individual[posi] = val

    return new_individual


def run_ga(g, n, k, m, e):
    """
    Executa o algoritmo genético e retorna o indivíduo com o menor número de ataques entre rainhas
    :param g:int - numero de gerações
    :param n:int - numero de individuos
    :param k:int - numero de participantes do torneio
    :param m:float - probabilidade de mutação (entre 0 e 1, inclusive)
    :param e:bool - se vai haver elitismo
    :return:list - melhor individuo encontrado
    """
    raise NotImplementedError  # substituir pelo seu codigo


crossover([2,4,7,4,8,5,5,2],[3,2,7,5,2,4,1,1],3)