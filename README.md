# G30_Programacao-Dinamica_PA-26.1
Número da Lista: 30<br>
Conteúdo da Disciplina: Programação Dinâmica<br>
## Alunos
|Matrícula | Aluno |
| -- | -- |
| 20/0032364  |  Vitor Gabriel Gonçalves Dias |
| 22/1008632  |  Eduardo de Almeida Ferreira |
## Sobre
O **RotaDF** é uma aplicação desktop que calcula a menor rota (em custo de deslocamento) entre Regiões Administrativas (RAs) do Distrito Federal, utilizando o algoritmo de **Bellman-Ford (versão iterativa)**.

O grafo utilizado representa 28 das principais Regiões Administrativas do DF, onde cada aresta tem um peso que combina tempo de deslocamento e tarifa de transporte. Alguns trechos possuem peso negativo, simulando descontos de integração tarifária ou faixas exclusivas (como corredores de BRT), o que torna esses trajetos mais "baratos" mesmo sendo geograficamente mais longos. Por esse motivo, o projeto usa Bellman-Ford em vez de Dijkstra, já que o Dijkstra não suporta arestas com peso negativo.

O projeto é dividido em camadas com responsabilidades bem definidas:
- **`data`**: dados brutos do grafo do DF.
- **`domain`**: implementação pura do algoritmo de Bellman-Ford, sem nenhuma dependência de interface.
- **`services`**: camada que conecta os dados do grafo ao algoritmo e prepara os resultados para a interface.
- **`ui`**: interface gráfica feita em Tkinter, organizada em abas.

A aplicação possui três funcionalidades principais, organizadas em abas:
1. **Calculadora de Rota** — o usuário escolhe uma região de origem e uma de destino, e a aplicação exibe o custo total do trajeto e o caminho percorrido, tanto em texto quanto em uma visualização gráfica.
2. **Grafo Completo** — exibe todas as 28 Regiões Administrativas e as conexões entre elas, destacando visualmente os trechos com peso negativo (descontos).
3. **Tabela de Distâncias** — a partir de uma região de origem escolhida, lista o custo até todas as demais regiões, ordenadas da mais barata para a mais cara.

## Screenshots
Adicione 3 ou mais screenshots do projeto em funcionamento.

## Instalação
Linguagem: Python 3.10+<br>
Framework: Não há framework externo — a interface utiliza apenas a biblioteca **Tkinter**, que já vem integrada na instalação padrão do Python.<br>

### Pré-requisitos
- Python 3.10 ou superior instalado.
- Tkinter disponível na instalação do Python:
  - No Windows e macOS, o Tkinter já vem incluso por padrão na instalação do Python.
  - No Linux, caso não esteja instalado, é necessário instalar o pacote do sistema:
    ```bash
    sudo apt install python3-tk
    ```

### Passo a passo para rodar o projeto

1. Clone o repositório e entre na pasta do projeto:
   ```bash
   git clone https://github.com/projeto-de-algoritmos-2026/G30_PD_PA-26.1.git
   ```

2. Crie o ambiente virtual:
   ```bash
   python3 -m venv .venv
   ```

3. Ative o ambiente virtual:
   - Linux/macOS:
     ```bash
     source .venv/bin/activate
     ```
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```

   > É importante ativar o ambiente virtual antes de executar o projeto, para manter o ambiente de desenvolvimento isolado das demais instalações de Python da máquina. Como o projeto não utiliza nenhuma biblioteca externa além do Tkinter (que já vem com o Python), não há necessidade de instalar dependências adicionais nem de um arquivo `requirements.txt`.

4. Execute a aplicação:
   ```bash
   python main.py
   ```

## Uso
Após executar `python main.py`, a janela principal do RotaDF é aberta com três abas disponíveis no topo:

1. **Calculadora de Rota**
   - Selecione a Região Administrativa de **Origem** no primeiro seletor.
   - Selecione a Região Administrativa de **Destino** no segundo seletor.
   - Clique em **Calcular rota**.
   - O custo total do trajeto e a quantidade de trechos percorridos aparecem em destaque, e o caminho é desenhado visualmente, mostrando cada região percorrida em sequência.

2. **Grafo Completo**
   - Apenas abra a aba para visualizar todas as Regiões Administrativas do grafo e as conexões entre elas.
   - Trechos com peso negativo (descontos/faixas exclusivas) aparecem destacados em uma cor diferente.

3. **Tabela de Distâncias**
   - Selecione uma Região Administrativa de **Origem**.
   - Clique em **Gerar tabela**.
   - Uma tabela é exibida com o custo da origem escolhida até todas as demais regiões do DF, ordenada da mais barata para a mais cara. Regiões inalcançáveis a partir da origem são indicadas como tal.

