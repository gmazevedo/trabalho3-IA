# Inteligência Artificial - Trabalho 3
Este trabalho envolve a implementação de um algoritmo genético para o problema das 8 rainhas. Neste problema, o objetivo final é encontrar configurações do tabuleiro sem ataques entre rainhas. Matematicamente, deseja-se minimizar o número de ataques entre rainhas.

## Integrantes do grupo
- Gessica Franciéle Mendonça Azevedo - 302865  - Turma A
- Rafael Oleques Nunes - 309114 - Turma B
- Tatiane Sequerra Stivelman - 243681  - Turma B

## Implementação - Valores de parâmetros

#### 8 Rainhas:
Valores dos parâmetros do algoritmo genético (g, n, k, m, e) que resultem na execução que encontra uma configuração o menor número de ataques que foi possível obter:
- g = 69
- n = 60
- k = 5
- m = 0.6263436754373918
- e = True

Por meio destes parâmetros conseguimos 0 ataques em 80% dos testes que fizemos. Abaixo podemos ver o gráfico de execução de um desses casos.

![Alt text](./ga.png?raw=true "Gráfico de execução GA")

#### Alegrete:
Valores iniciais de theta_0, theta_1, valores de alpha e num_iterations que resultem na melhor execução da sua regressão linear:
- num_iterations = 73
- alpha = 0.0001
- theta_0 = 0
- theta_1 = 0

Melhor erro quadrático médio obtido: 2.415831513816925

Resultado:

![Alt text](./rl.png?raw=true "Gráfico de execução RL")
