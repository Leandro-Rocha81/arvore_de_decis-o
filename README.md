# 🧠 Árvore de Decisão com Cálculo de Entropia e Ganho de Informação

Este projeto implementa uma árvore de decisão **do zero em Python**, utilizando os conceitos fundamentais de **entropia** e **ganho de informação**, com o objetivo de classificar dados categóricos e numéricos discretizados. Nenhuma biblioteca externa de machine learning é utilizada para a construção da árvore.

## 📌 Descrição

A árvore de decisão é construída a partir de um conjunto de dados fictício que contém informações sobre pessoas (como gênero, idade, escolaridade, estado civil e renda) e a variável-alvo "Comprou", indicando se compraram ou não um produto. O algoritmo seleciona, a cada nível, o atributo com maior ganho de informação para fazer a divisão dos dados, até que todos os exemplos sejam classificados ou não haja mais atributos para dividir.

## 🧮 Técnicas aplicadas

- **Entropia de Shannon**: mede a incerteza dos dados.
- **Ganho de Informação**: avalia a redução da entropia ao dividir os dados por um determinado atributo.
- **Recursividade**: a árvore é construída de forma recursiva até os critérios de parada.

## 🗂️ Estrutura dos dados

Os dados simulam um cenário simples de marketing, com as seguintes colunas:

- `Gênero`
- `Idade`
- `Escolaridade`
- `Estado Civil`
- `Renda (R$)`
- `Comprou` (variável alvo)

> ⚠️ Nota: O atributo "Idade" e "Renda" são tratados como categóricos neste exemplo (valores exatos), e não foram discretizados.

## ▶️ Como executar

1. **Clone o repositório:**

```bash
git clone https://github.com/Leandro-Rocha81/arvore_de_decis-o.git
cd arvore_de_decisao
```

2. **Instale as dependências:**

```bash
pip install -r requirementes.txt
```

3. **Execute o código:**

```bash
python main.py
```

4. **Saída esperada:**
A árvore de decisão será exibida no terminal, representada como um dicionário aninhado.

## 📂 Arquivos

- `main.py`: implementação completa da árvore de decisão.
- `explicacao_arvore_decisao.pdf`: arquivo com a explicação técnica
- `README.md`: este arquivo, com instruções e descrição do projeto.
- `.gitignore`: arquivos que o Git deve ignorar
- `requirementes.txt`: arquivo de texto usado em projetos Python para listar todos os pacotes (bibliotecas) que o projeto precisa para funcionar corretamente.

## 💡 Exemplo de saída

```python
{'Idade': {22: 'Não',
           23: 'Não',
           24: 'Não',
           27: 'Não',
           28: 'Sim',
           30: 'Não',
           35: 'Sim',
           36: 'Sim',
           40: 'Sim',
           50: 'Sim'}}
```

## 🚀 Possíveis melhorias

- Discretização automática de atributos numéricos (como idade e renda).
- Visualização gráfica da árvore com bibliotecas como `graphviz`.
- Validação do modelo com dados de teste.
- Suporte a dados com atributos contínuos.

## 🧑‍💻 Autor

- **Leandro** — projeto acadêmico de aprendizado de Mineração de Dados