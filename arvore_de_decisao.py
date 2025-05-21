import math
import pandas as pd

# Cálculo da entropia para um conjunto de dados
def entropia(data_frame, classes, atributo_classe):
    soma = 0
    qtd_total = len(data_frame[atributo_classe])
    for classe in classes:
        qtd_classe = len(data_frame[data_frame[atributo_classe] == classe])
        p_i = qtd_classe / qtd_total
        if p_i == 0:
            log = 0
        else:
            log = math.log2(p_i)
        item = p_i * log
        soma += item
    return -1 * soma

# Cálculo do ganho de informação para um atributo
def ganho(data_frame, atributo, atributo_classe):
    values = data_frame[atributo].unique()
    classes = data_frame[atributo_classe].unique()
    qtd_total = len(data_frame[atributo])
    soma = 0
    for value in values:
        sub_set = data_frame[data_frame[atributo] == value]
        qtd_value = len(sub_set)
        p_v = qtd_value / qtd_total
        entropia_subset = entropia(sub_set, classes, atributo_classe)
        soma += p_v * entropia_subset

    return entropia(data_frame, classes, atributo_classe) - soma

# Função para construir a árvore de decisão recursivamente
def construir_arvore(data_frame, atributos, atributo_classe, nivel=0):
    classes = data_frame[atributo_classe].unique()

    # Caso 1: todas as instâncias são da mesma classe (nó folha)
    if len(classes) == 1:
        return classes[0]

    # Caso 2: não há mais atributos para dividir (escolhe a classe mais comum)
    if len(atributos) == 0:
        return data_frame[atributo_classe].mode()[0]

    # Escolhe o atributo com maior ganho de informação
    ganhos = {atrib: ganho(data_frame, atrib, atributo_classe) for atrib in atributos}
    melhor_atributo = max(ganhos, key=ganhos.get)

    arvore = {melhor_atributo: {}}

    # Para cada valor do atributo, cria um ramo da árvore
    for valor in data_frame[melhor_atributo].unique():
        sub_data = data_frame[data_frame[melhor_atributo] == valor]

        if sub_data.empty:
            arvore[melhor_atributo][valor] = data_frame[atributo_classe].mode()[0]
        else:
            novos_atributos = [a for a in atributos if a != melhor_atributo]
            arvore[melhor_atributo][valor] = construir_arvore(sub_data, novos_atributos, atributo_classe, nivel + 1)

    return arvore

# Criando o DataFrame
dados = {
    'Gênero': ['F', 'M', 'F', 'M', 'F', 'M', 'M', 'F', 'M', 'F'],
    'Idade': [22, 35, 28, 40, 23, 30, 36, 27, 50, 24],
    'Escolaridade': [
        'Médio', 'Superior completo', 'Superior incompleto', 'Superior completo',
        'Médio', 'Médio', 'Pós-graduação', 'Superior completo',
        'Pós-graduação', 'Superior incompleto'
    ],
    'Estado Civil': [
        'Solteiro', 'Casado', 'Solteiro', 'Divorciado', 'Solteiro',
        'Casado', 'Casado', 'Solteiro', 'Divorciado', 'Solteiro'
    ],
    'Renda (R$)': [2500, 4000, 3200, 4100, 2700, 3000, 4200, 2900, 4500, 2600],
    'Comprou': ['Não', 'Sim', 'Sim', 'Sim', 'Não', 'Não', 'Sim', 'Não', 'Sim', 'Não']
}

df = pd.DataFrame(dados)

# Preparando atributos
atributos = [col for col in df.columns if col != 'Comprou']

# Construindo a árvore
arvore = construir_arvore(df, atributos, 'Comprou')

# Exibindo a árvore final
from pprint import pprint
pprint(arvore)
