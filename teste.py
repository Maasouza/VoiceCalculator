from trainning import *
palavras = ["igual"]
num_gravacoes = 5
pasta_destino = "centroid"
treinamento = VoiceTrainer(palavras,num_gravacoes,pasta_destino)
treinamento.generate_centroid_files()