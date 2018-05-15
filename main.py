import nltk
import tkinter
import re
import decimal

from treeGenerator import generateTree
from createDictionary import getDataset
import word 


tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

#add space between word and special character
def specialCharacter(sentence):
    sentence = sentence.lower()
    sentence = re.sub('(?<=\w)([!?,.:;/\\<>"])', r' \1', sentence)
    return sentence.split()
 
def generateResults(input,message):
    result = "Rating : "
    count = 1

    if(input=='' or input==None):
        return
    
    sentences = tokenizer.tokenize(input.get("1.0",'end-1c'))
    
    for sentence in sentences:
        #Split the sentence into word
        wordList = nltk.pos_tag(specialCharacter(sentence),tagset='universal')
        words = []
    
        for i  in wordList:
            if ( i[0] in wordDataset):
                words.append(word.Word(i[0],wordDataset[i[0]],i[1]))
            else:
                words.append(word.Word(i[0],0,"X"))
        ans = generateTree(words)
        if(words[-1].word=="?"):
            ans = 0.00
        if(ans>10):
            ans = 10.00
        elif(ans<-10):
            ans = -10.00
        result += "\nSentence {} = {}".format(count , round(ans,2) )
        count += 1
    
    message.configure(text=result)

#Get the list of words and their polarity  
wordDataset = getDataset()

window =tkinter.Tk(className = 'Vichaar')
window.title("Vichaar")
window.geometry('800x500')

var = tkinter.StringVar()
label1 = tkinter.Message( window, text="Enter the sentence to be rated :",width=200,relief=tkinter.RAISED )
label1.place(x=5,y=3)

rating = tkinter.Message( window, text="Rating : ",width=200)
rating.place(x=0,y=65)

sentenceInputHolder = tkinter.Text(window,width=70,height=3)
sentenceInputHolder.place(x=200,y=2)

button = tkinter.Button(window, text ="Get Rating", command = lambda: generateResults(sentenceInputHolder,rating))
button.place(x=5,y=30)
window.mainloop()