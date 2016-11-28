from recognizing import *
from casting import *

import time as T
a = []#folders
path = "" #path to centroid folder

t = VoiceRecognizer(a,path)

t.read_files()

play = True
equation = "" #por extenso.

while(play):

    audio_data = t.extract_params()

    print("Equação:", equation)
    T.sleep(2)

    word = t.compare(audio_data)
    if(word != None):
        if(word != "igual"):
            equation += word+" "
        else:
            play = False
            equation=equation[:-1]
    else:
        print("Palavra não identificada")

c = TextCalculator()

(op,x,y) = c.data_extract(equation)

print(c.calculator(op,x,y))
