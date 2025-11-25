# Visualizador de Labirintos com DFS

## Alunos

| Matrícula  | Nome                                      |
| ---------- | ----------------------------------------- |
| 21/1031083 | Julia Vitória Freire Silva                |
| 20/0038028 | Guilherme Evangelista Ferreira dos Santos |

---

## Descrição do projeto

Este projeto implementa uma **visualização interativa de resolução de labirintos** utilizando o algoritmo **Depth-First Search (DFS)**. A aplicação, desenvolvida em **Python com Pygame**, permite:

* **Gerar labirintos aleatórios** com obstáculos e paredes.
* **Visualizar o passo a passo** da resolução do labirinto utilizando DFS.
* **Exibir animações e cores distintas** para indicar o progresso da busca, como o caminho percorrido, os obstáculos e a solução.
* **Mostrar o tempo de execução** da busca.
* **Alternar entre diferentes tipos de labirintos**, incluindo cenários mais desafiadores, como labirintos impossíveis de resolver.

O algoritmo utilizado é o **DFS (Depth-First Search)**, que explora o labirinto a partir de um ponto inicial até encontrar o objetivo ou explorar todas as possibilidades.

---

## Guia de instalação

### Dependências do projeto

* **Python 3.8+**
* **Pygame** (>= 2.0.0)

Para instalar o Pygame:

```bash
pip install pygame
````

---

## Como executar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/EDAII/Visualizador_de_Labirintos_com_DFS.git
```

2. Execute o arquivo principal:

```bash
python main.py
```

            

---

## Visualização e Indicadores

* **Cores dos células** representam o estado de cada posição no labirinto:

  * **Branco**: célula livre.
  * **Preto**: célula com obstáculo.
  * **Azul**: célula sendo explorada pela busca DFS.
  * **Verde**: célula já visitada (parte do caminho percorrido).
  * **Vermelho**: célula de destino.
  * **Amarelo**: célula inicial.

Além disso, são exibidas informações na tela:

* Status da execução: **"Explorando..."** ou **"Finalizado"**.
* Tempo de execução da busca.
* Contagem de células visitadas.


---

## 🎥 Vídeo de Apresentação

Neste vídeo, é feita uma demonstração completa da aplicação, explicando o funcionamento do algoritmo DFS na resolução de labirintos.

[Assista no YouTube](https://youtu.be/6XKPSsUPCi0)

---

## Conclusões

* O projeto permite **visualizar** como o algoritmo DFS explora diferentes caminhos dentro de um labirinto.
* A **visualização interativa** ajuda a entender as fases de exploração, incluindo a descoberta de caminhos e retrocedimento.
* A ferramenta é útil para **ensino de algoritmos de busca** em grafos, proporcionando uma maneira prática e visual de observar o comportamento do DFS.
* Labirintos gerados aleatoriamente, bem como a possibilidade de testar cenários **impossíveis**, tornam a experiência mais dinâmica e exploratória.


