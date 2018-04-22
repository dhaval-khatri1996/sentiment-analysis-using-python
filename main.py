import nltk
import tkinter

from treeGenerator import generateTree
from createDictionary import getDataset
import word 


tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

def handlePunctuation(sentence):
    return (sentence.replace(",", " ,").
            replace(".", " .").
            replace("!"," !").
            replace("?"," ?").
            replace(":"," ").
            replace(";"," ").
            replace("/"," ")).lower().split()

#Get the list of words and their polarity   

def generateResults(input,message):
    result = "Rating : "
    count = 1

    if(input=='' or input==None):
        return
    
    sentences = tokenizer.tokenize(input.get("1.0",'end-1c'))
    
    for sentence in sentences:
        #Split the sentence into word
        wordList = nltk.pos_tag(handlePunctuation(sentence),tagset='universal' )
        words=[]
    
        for i  in wordList:
            print(i)
            if ( i[0] in wordDataset):
                words.append(word.Word(i[0],wordDataset[i[0]],i[1]))
            else:
                words.append(word.Word(i[0],0,"X"))
        ans = generateTree(words)
        if(ans>10):
            ans=10
        elif(ans<-10):
            ans=-10
        result += "\nSentence{} = {}".format(count , ans )
        count+=1
    
    message.configure(text=result)

wordDataset = getDataset()

window =tkinter.Tk(className = 'Vichar')
window.title("Vichar")
window.geometry('800x500')
var = tkinter.StringVar()
label1 = tkinter.Message( window, text="Enter the sentence to be rated :",width=200,relief=tkinter.RAISED )
label1.place(x=5,y=3)
rating = tkinter.Message( window, text="Rating : ",width=100)
rating.place(x=0,y=55)
sentenceInputHolder = tkinter.Text(window,width=70,height=3)
sentenceInputHolder.place(x=200,y=2)
button = tkinter.Button(window, text ="Get Rating", command = lambda: generateResults(sentenceInputHolder,rating))
button.place(x=5,y=30)
window.mainloop()