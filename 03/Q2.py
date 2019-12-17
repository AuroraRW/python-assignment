#A3-Q2
try:
    n=int(input("Enter the number of the items:"))  
    dic={}
    for i in range(0,n):
        s=input("Enter the item's name and price, seprated by space:")
        s=s.lower()
        
        #delete spaces between the name and the price
        w=s.find(' ')
        list=[]
        list.append(s[0:w])
        list.append(s[w:len(s)])
        t=list[1].find(' ')
        list[1]=list[1].lstrip()
        
        #list[0]is the item's name, list[1]is the price
        list[1]=float(list[1])
        
        #see if there is this item in the list already
        if dic.get(list[0],0)==0:
            dic[list[0]]=list[1]
        else:
            #net price
            dic[list[0]]=dic[list[0]]+list[1]
    for x,y in dic.items():
        print(x,'',y)
except:
    print("Wrong input!!")
