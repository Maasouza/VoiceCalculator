#<p align='center'>COE363 - Telecomunicações - UFRJ 2016.2</p>
<p align='center'>VoiceCalculator - Calculadora comandado por voz</p>

Trabalho desenvolvido por: [Marcos Aurélio](https://github.com/Maasouza),[Anna Gabrielle](https://github.com/AnnaGabrielle)<br>
Para a disciplina do Profº. Fernando Gil

1. Tecnologias
    * Python  
2. Bibliotecas utilizadas
    <ul>
      <li>[Scipy](https://www.scipy.org/) - Biblioteca que fornece algumas funções matemáticas.</li>
      <li>[PyAudio](https://people.csail.mit.edu/hubert/pyaudio/) - Biblioteca utilizada para gravação dos áudios</li>
      <li>[FastDTW](https://pypi.python.org/pypi/fastdtw/0.3.0) - Biblioteca que fornece o algoritmo DTW para calcular a distancia entres os áudios</li>
      <li>[Python Speech Features](https://github.com/jameslyons/python_speech_features) - Biblioteca utilizada para retirada dos MFCCs</li>
    </ul>

3. Modulos

  - [ ] Algoritmo de força bruta
  - [ ] Algoritmo backtracking
  - [ ] Algoritmo branch and bound
  - [ ] Algoritmo utilizando a heurística XXXX
  - [X] Função para gerar um grafo aleatório

3. Instruções
    * [Download](https://github.com/Maasouza/MinVertexCover/archive/master.zip)

    * Clone

            git clone https://github.com/maasouza/minvertexcover.git

    * Para rodar o algoritmo

            cd minvertexcover/src
            make
            ./main --path ../path/to/graph.dat --type [BF|BT|BB|HT]

    * Para gerar um grafo

            cd minvertexcover/data
            make
            ./new --v nVertices --d densidade --path ../path/to/new_graph.dat

    * Visualizar o grafo

            O grafo pode ser visualizado localmente.
            Basta abrir o arquivo index.html (Firefox only).
            Exemplo https://maasouza.github.io/MinVertexCover/site/





