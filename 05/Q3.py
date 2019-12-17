#A5-Q3
import math
#definition of class Complex
class Complex():
    #constructor function
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
    #overload the adding operation    
    def __add__(self,no):
        R=self.real+no.real
        I=self.imaginary+no.imaginary
        return Complex(R,I)
    #overload the subtracting operation   
    def __sub__(self,no):
        R=self.real-no.real
        I=self.imaginary-no.imaginary
        return Complex(R,I)
    #overload the multiplication operation
    def __mul__(self,no):
        a=self.real
        b=self.imaginary
        c=no.real
        d=no.imaginary
        R=(a*c)-(b*d)
        I=(b*c)+(a*d)
        return Complex(R,I)
    #overload the division operation
    def __truediv__(self,no):
        a=self.real
        b=self.imaginary
        c=no.real
        d=no.imaginary
        t=pow(c,2)+pow(d,2)
        if t!=0:
            R=(a*c+b*d)/t
            I=(b*c-a*d)/t
        else:
            print("Can not do the division operation")
        return Complex(R,I)
    #mode function
    def mod(self):
        a=self.real
        b=self.imaginary
        return pow(pow(a,2)+pow(b,2),0.5)
    #format
    def __str__(self):
        if self.imaginary==0:
            result="%.2f+0.00i"%(self.real)
        elif self.real==0:
            if self.imaginary>=0:
                result="0.00+%.2fi"%(self.imaginary)
            else:
                result="0.00-%.2fi"%(abs(self.imaginary))
        elif self.imaginary>0:
            result="%.2f+%.2fi"%(self.real,self.imaginary)
        else:
            result="%.2f-%.2fi"%(self.real,abs(self.imaginary))
        return result
#in main, adding, subtracting, multiplication and division between two complex number  
if __name__=='__main__':
    try:
        s1=input('Enter a complex number(separated by spaces):')
        s2=input('Enter another complex number(separated by spaces):')
        r1=float(s1.split(' ')[0])
        i1=float(s1.split(' ')[1])
        r2=float(s2.split(' ')[0])
        i2=float(s2.split(' ')[1])
        C=Complex(r1,i1)
        D=Complex(r2,i2)
        print(C+D)
        print(C-D)
        print(C*D)
        print(C/D)
        print('Mod of C is:%.2f'%(C.mod()))
        print('Mod of D is:%.2f'%(D.mod()))
    except:
        print('Wrong input!')
