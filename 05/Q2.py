#A5-Q2
#definition of class C1
class C1():
    #constructor function
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

#definition of class C2
class C2(C1):
    #compare two lists and get the larger one
    def F1(self,y):
        if type(y)!=type([]):
            print('Wrong')
            return
        else:
            if self.LX>y:
                #print('The larger one is')
                return self.LX
            else:
                #print('The larger one is')
                return y        
    #choose the largest list 
    def M1(self,LL):
        if type(LL)!=type([]):
            print('Wrong input!')
            return
        else:
            temp=LL[0]
            for t in LL:
                if type(t)!=type([]):
                    print('Wrong type of element')
                    return
                else:
                    if t>temp:
                        temp=t
        return temp
#in main, input the strings and convert to list
if __name__=='__main__':
    try:
        s1=input("Enter several strings (separated by spaces):")
        L1=s1.split(' ')
        print('List 1 is:',L1)
        s2=input("Enter other strings (separated by spaces):")
        L2=s2.split(' ')
        print('List 2 is:',L2)
        s3=input("Enter more strings (enter 'stop' to stop):")
        L3=s3.split(' ')
        print('List 3 is:',L3)
        LL=[L1,L2,L3]
        print('List of lists is:', LL)
        ins=C2(L1)
        ins.F1(L2)
        print('The larger one between list 1 and list 2 is:',ins.F1(L2))
        ins2=C2(L2)
        print(ins+ins2)
        print('The largest one is', ins.M1(LL))
    except:
        print("Wrong input!")
