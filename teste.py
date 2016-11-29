from trainning import *
palavras = ["um","dois","mais","igual"]
num_gravacoes = 3
pasta_destino = "centroid"
treinamento = VoiceTrainer(palavras,num_gravacoes,pasta_destino)
treinamento.generate_centroid_files()