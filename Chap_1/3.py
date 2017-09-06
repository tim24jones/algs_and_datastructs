def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n
class Fraction:
    def __init__(self,top,bottom):
        divisor=gcd(top,bottom)
        self.num=top//divisor
        self.den=bottom//divisor
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    def getNum(self):
        return self.num
    def getDen(self):
        return self.den
    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum,newden)
    def __sub__(self,otherfraction):
        newnum=self.num*otherfraction.den-self.den*otherfraction.num
        newden=self.den*otherfraction.den
        return Fraction(newnum,newden)
    def __mult__(self,otherfraction):
        newnum=self.num*otherfraction.num
        newden=self.den*otherfraction.den
        return Fraction(newnum,newden)
    def __truediv__(self,otherfraction):
        newnum=self.num*otherfraction.den
        newden=self.den*otherfraction.num
        return Fraction(newnum,newden)
n=Fraction(2,8)
r=Fraction(2,6)
print(n.getDen())
print(n+r)