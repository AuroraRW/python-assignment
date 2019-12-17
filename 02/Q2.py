#A2-Q2
# define a function to comput how many times a word appears in a sentence
def Q2(sentence, word):
    list_s=sentence.split(' ')
    count=0
    for w in list_s:
        if word==w:
            count=count+1
    return count
