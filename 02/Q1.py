#A2-Q1
#list_all stores all words
list_all=[]
#flg is a label. When equals 1, the program terminates.
flg=0
while flg==0:
    str_words=input('Enter some words:')
    list_words=str_words.split(' ')
    for words in list_words:
        if words in list_all:
            flg=1
        else:
            list_all.append(words)
else:
    list_all.sort()
    print(list_all)
