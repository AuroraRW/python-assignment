#A5-Q1
#defination of class C1
class C1():
    #constructor function of C1
    def __init__(self,x):
        self.LX=[]
        if type(x)!=type([]):
            print("Wrong input!")
            return
        if x!=[]:
            for t in x:
                self.LX.append(t)
                
    #function of M1, print the list           
    def M1(self):
        if self.LX!=['']:
            print(self.LX)
        else:
            print("LX is empty!")
            
    #overload for '+'        
    def __add__(self,other):
        tempall=[]
        if self.LX!=[''] and other.LX!=['']:
            #find the common word
            for t in other.LX:
                if t in self.LX:
                    tempall.append(t)
        if tempall==[]:
            return 'There is no common elements!'
        else:
            print('The common elements between the two lists are:')
            return tempall
        
#in main, input the strings and convert to list     
if __name__=='__main__':
    try:
        s1=input("Enter several string (separated by spaces):")
        L1=s1.split(' ')
        v1=C1(L1)
        v1.M1()
        s2=input("Enter other strings (separated by spaces):")
        L2=s2.split(' ')
        v2=C1(L2)
        v2.M1()
        print(v1+v2)
    except:
        print("Wrong input!")
