
class TextCalculator():

    def operation_cast(self,argument):
        switcher = {
            "mais"     : 0,
            "menos"    : 1,
            "dividido" : 2,
            "vezes"    : 3,
            "elevado"  : 4,
        }
        return switcher.get(argument, None)

    def number_cast(self,argument):
        switcher = {
            "zero"   : "0",
            "um"     : "1",
            "dois"   : "2",
            "tres"   : "3",
            "quatro" : "4",
            "cinco"  : "5",
            "seis"   : "6",
            "sete"   : "7",
            "oito"   : "8",
            "nove"   : "9",
        }

        return switcher.get(argument, "")

    def data_extract(self,text):
        """retorna uma lista contendo (operação,x,y)"""
        words = text.split(" ")

        op = None
        x = ""
        y = ""

        for word in words:
            if (op == None):
                if(word == "mais" or word == "menos" or word == "dividido" or word == "vezes" or word =="elevado"):
                    op = self.operation_cast(word)
                else:
                    x+=self.number_cast(word)
            else:
                y += self.number_cast(word)

        return op,int(x),int(y)


    def calculator(self,op, x, y):
        if(x== None or y == None or op == None):
            print("Numero ou operação invalida")
            return None

        if   (op == 0):
            return (x + y)
        elif (op == 1):
            return (x - y)
        elif (op == 2):
            return (x / y)
        elif (op == 3):
            return (x * y)
        elif (op == 4):
            return (x**y)



