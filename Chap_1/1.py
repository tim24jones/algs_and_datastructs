class Fraction:
    def __init__(self,top,bottom):
        self.num=top
        self.den=bottom
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    def getNum(self):
        return self.num
    def getDen(self):
        return self.den
n=Fraction(1,6)
print(Fraction(2,3))
print(n.getDen())
print(n.getNum())