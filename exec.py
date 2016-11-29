from recognizing import *
from casting import *

import time as T
a = ["um","dois","mais","igual"]#folders
path = "controid" #path to centroid folder

t = VoiceRecognizer(a,path)

t.read_files()

play = True
equation = []#por extenso.

while(play):

    audio_data = t.extract_params()

    print("Equação:", equation)
    T.sleep(2)

    word = t.compare(audio_data)
    if(word != None):
        if(word != "igual"):
            equation.append(word)#passar como lista direto
        else:
            play = False
    else:
        print("Palavra não identificada")

c = TextCalculator()

(op,x,y) = c.data_extract(equation)#passar como lista direto

print(c.calculator(op,x,y))
