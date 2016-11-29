#<p align='center'>COE363 - Telecomunicações - UFRJ 2016.2</p>
<p align='center'>VoiceCalculator - Calculadora comandado por voz</p>

Trabalho desenvolvido por: [Marcos Aurélio](https://github.com/Maasouza) e [Anna Gabrielle](https://github.com/AnnaGabrielle)<br>
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
    
    * Gravação  

            Modulo base do trabalho  
            Contém a classe VoiceRecorder que contem as funções necessarias para a gravação dos audios 
    
    * Treinamento  

            Derivado do modulo de gravação  
            Ele é responsavel por gravar os audios, retirar os parametros e calcular os centroides
            Gera arquivos contendos os centroides que serão lidos pelo modulo de reconhecimento  
    
    * Reconhecimento  

            Modulo que recebe os arquivos gerados pelo modulo de treinamento  
            Ele é responsavel por gravar e comparar os audios de entradas com os do treinamento  
            No final de sua execução gerar uma string que será tratada no modulo Traduto  

    * Tradutor  

            Modulo genérico
            Responsavel por receber uma string e converter para funções
            No nosso caso transforma string em operações numéricas  
            
4. Instruções  
  
   * Clone o repositorio ou realize o download  
   
   * Tenha os itens citados no topico 2 instalados  
   
   * Crie um arquivo como este exemplo para realizar o treinamento  
   
         ```python
         from training import *
         palavras = ["lista","de","palavras"]
         num_gravacoes = 4
         pasta_destino = "caminho/para/pasta/que/vai/conter/os/arquivos/"
         treinamento = VoiceTrainer(palavras,num_gravacoes,pasta_destino)
         ```
         
   * Crie um arquivo como este de exemplo para executar o reconhecimento

         ```python
         from recognizing import *
         palavras = ["lista","de","palavras"]
         pasta_dados = "pasta/que/contem/os/arquivos/gerados/no/treino"
         reconhecedor = VoiceRocognizer(palavras,pasta_dados)
         continua = True
         frase = ""
         while(continua):
            dados = reconhecedor.extract_params()
            palavra = reconhecedor.compare(dados)
            if(palavra satisfaz condição de parada):
               continua = False
            frase.append(palavra)
         tradutor = casting()
         tradutor.execute(frase)
         ```




