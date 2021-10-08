import random
import copy

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

def generate_individuals(n):
    individuals = []

    for i in range(0, n):
        individuals.append([random.randint(1, 8) for p in range(0, 8)])

    return individuals

def top(individuals, n):
    copy_individuals = copy.deepcopy(individuals)
    top_individuals = []

    if(n == 1):
        best = tournament(copy_individuals)
        return best

    best = tournament(copy_individuals)

    for i in range(0, n):
        if len(copy_individuals) == 0:
            top_individuals.append(best)
        else:
            best = tournament(copy_individuals)
            top_individuals.append(best)
            copy_individuals.remove(best)
    
    return top_individuals

def selecao(individuals, k):
    part = copy.deepcopy(individuals)

    while(len(part) != k):
        del part[random.randint(0, len(part)-1)]
    
    return top(part, 2)


def run_ga(g, n, k, m, e, graph=False):
    """
    Executa o algoritmo genético e retorna o indivíduo com o menor número de ataques entre rainhas
    :param g:int - numero de gerações
    :param n:int - numero de individuos
    :param k:int - numero de participantes do torneio
    :param m:float - probabilidade de mutação (entre 0 e 1, inclusive)
    :param e:bool - se vai haver elitismo
    :return:list - melhor individuo encontrado
    """
    max_fit = []
    min_fit = []
    avarage_fit = []
    n_individuals = []
    
    individuals = generate_individuals(n)
    new_individuals = []

    for i in range(0, g):
        new_individuals = []

        if e:
            new_individuals.append(top(individuals, 1))

        while(len(new_individuals) < n):
            p1, p2 = selecao(individuals, k)

            o1, o2 = crossover(p1, p2, random.randint(0, 7))
            o1 = mutate(o1, m)
            o2 = mutate(o2, m)

            new_individuals.append(o1)
            new_individuals.append(o2)
              
        individuals = new_individuals
        
        min_fit_local = evaluate(new_individuals[0])
        max_fit_local = min_fit_local
        avarage_fit_local = min_fit_local
                
        for ind in range(1, len(individuals)):
            fit = evaluate(new_individuals[ind])

            if(fit > max_fit_local):
                max_fit_local = fit

            if(fit < min_fit_local):
                min_fit_local = fit

            avarage_fit_local += fit

        max_fit.append(max_fit_local)
        min_fit.append(min_fit_local)
        avarage_fit.append(avarage_fit_local/len(individuals))   
    
    if graph:
        return top(individuals, 1), [max_fit, min_fit, avarage_fit]
    else:
        return top(individuals, 1)

def the_best():
    best = 10
    n_bests = 0
    list_bests = []

    while(n_bests != 5):
        g, n = random.randint(1,100), random.randint(1,100)
        if n >= 5:
            k = random.randint(2,5)
        else:
            k = random.randint(1,n)
        
        m, e = random.random(), True

        individuals = run_ga(g, n, k, m, e)
        best = evaluate(individuals)

        if(best == 0):
            list_bests.append([g, n, k, m, e])
            n_bests += 1
            print("Encontrei:", n_bests)

    max_zeros = -1
    i_max = -1

    for i in range(0, 5):
        atual = 0

        print("===> ", i)
        for j in range(0, 10):
            g, n, k, m, e = list_bests[i]
            individuals = run_ga(g, n, k, m, e)
            result = evaluate(individuals)   

            if(result == 0):
                atual += 1 
        
        if(atual > max_zeros):
            max_zeros = atual
            i_max = i
    
    return list_bests[i_max], max_zeros

'''
if __name__ == '__main__':
    parametros, acertos = the_best()

    g, n, k, m, e = parametros

    print("Fui escolhido com ", str(acertos/10)+"% de acertos")
    print(parametros)

    for i in range(0, 3):
        individuals = run_ga(g, n, k, m, e)
        best = evaluate(individuals)
        print(best, individuals)
'''