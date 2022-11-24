#Proj 4: Worldle 
#Description: A program to read a text file and use a specified amount of words to make a word cloud
#Lien Har
#11/2/2020

from graphics import * #import  from graphics
from random import * #import from random 
from time import sleep #import sleep



def remove_ch(words): #function to remove puntuation from the string 'words'

    char="'!?.,{}[];:-$&\|/'" #punctuation
    
#for loop: checks every character in words, gets rid of it if it is punctuation:
    for ch in words: 
        if ch in char:
            words=words.replace(ch,'') #ch--> nothing
    

    return words #send words back to main ()



def getFreq(item): #function to get second part of tuple (the frequency)
    return item[1] #return to ranking()



def ranking(freq): #function to sort number of word occurences 
    freq_list=list(freq.items()) #convert string to list
    
#sort list by highest to lowest by key, use returned value from getFreq:
    freq_list.sort(key=getFreq, reverse=True) #key=second part of tuple
    print(freq_list)
    
    return freq_list #return to main



def remove_stopwords(wordlist): 
    stopwords=['a','able','about','across','after','all','almost','also','am','among',
             'an','and','any','are','as','at','be','because','been','but','by','can',
             'cannot','could','dear','did','do','does','either','else','ever','every',
             'for','from','get','got','had','has','have','he','her','hers','him','his',
             'how','however','i','if','in','into','is','it','its','just','least','let',
             'like','likely','may','me','might','most','must','my','neither','no','nor',
           'not','of','off','often','on','only','or','other','our','own','rather','said',
             'say','says','she','should','since','so','some','than','that','the','their',
             'them','then','there','these','they','this','tis','to','too','twas','us',
             'wants','was','we','were','what','when','where','which','while','who',
             'whom','why','will','with','would','yet','you','your']
    
#Create a new list for words that are not stopwords:    
    newlist=[] 
    for word in wordlist: #for every word in the string
        if not word in stopwords: #check if not stopwords
            newlist.append(word) #add to list if not

    return newlist #send back to userinput()



listOverlap=[] #for overlap()
def overlap(pt): #function to minimize overlap

    
#for loop to check if random point is near other random points in listOverlap list:
    for word in listOverlap: #check every word (that is on a point) in the list
          
        if word.getX() -15 <= pt.getX() <= word.getX() +15: #x value can't be this close
            if word.getY() -10 <= pt.getY() <= word.getY() +10: #y value can't be this close

                
                return True #it is too close (overlapping)
            
    listOverlap.append(pt) #add valid point to list
    return False #It is far enough from the other points, send back to window() to draw



def window(sort): #Draws the text in the window to make the wordle with help from drawtext ()
    
    win = GraphWin("Wordcloud", 600, 600) #window

    win.setCoords(0,0,100,100) #(to help with overlapping)
    #(lines of pixels are more spaced out, so the words are also)

#draw opening message:
    Title=Text(Point(50,50), "ⓦⓔⓛⓒⓞⓜⓔ to the Wordcloud!\nPress anywhere to continue!") 
    Title.setSize(30)
    Title.draw(win)

#wait for mouse click, undraw:
    win.getMouse()
    Title.undraw()
    
    pt=Point(randrange(10,90),randrange(10,90)) #random point for first word drawn
    
    size=0 #for for loop

#for loop with text size accumulator:    
    for word in sort:
        while overlap(pt): #while point overlaps, get new random point in overlap():
            pt=Point(randrange(10,90),randrange(10,90))

#decrease text size in the order of appearance in the list      
        text=Text(pt,word[0]) #get first part of tuple(word) and random point
        text_size=50-size #decrease size
        size+=4 #increase increment for decrease
        drawtext(win, text, text_size) #call drawtext()
        
        

def userinput(): #convert user input text into a list without stopwords and punctuation

    win = GraphWin("input", 600, 600) #create window

    image=Image(Point(300,300), 'OIP.gif') #create fun background image
    image.draw(win)

    myRect=Rectangle(Point(100,270), Point(500, 330)) #create red box on image
    myRect.setFill("red")
    myRect.draw(win)

#draw text on top of image and red box:
    opening=Text(Point(300,300),"Welcome! Let's make a wordcloud!\nWhat file do you want to make a word cloud of?\n(enter and then click)")
    opening.setTextColor('white')
    opening.setStyle('bold')
    opening.draw(win)
    
#draw user input box:    
    userinputbox=Entry(Point(300,350), 50)
    userinputbox.draw(win)

    win.getMouse() #wait for click
    
    inputted=userinputbox.getText() #get inputted text from inputbox

#processing text file:   
    file=open(inputted, 'r', encoding='utf-8') #open textfile

    words=file.read().lower() #read and make lowercase (text now a string)
    
    words=remove_ch(words) #remove the punctuation
    
    wordlist = words.split() #split string into a list (convert)
    
    wordlist = remove_stopwords(wordlist) #send list to remove_stopwords() and rename variable again as wordlist
    
    file.close() #close file
    win.close() #close window
    return wordlist #return opened and converted file to main
    

    
def drawtext(win, text, text_size): #Function to draw text

#randomly chooses color and sets size:
    r=randrange(0, 225) #red random
    g=randrange(0, 225) #green
    b=randrange(0, 225) #blue
    text.setTextColor(color_rgb(r, g, b))
    text.setSize(text_size)

#sets font:
    faces=['helvetica', 'courier', 'times roman', 'arial'] #fonts
    face=choice(faces) #randomizes fonts


    text.setFace(face) #set font
    text.draw(win) #draw text



def main():
    
    wordlist=userinput() #gets value from userinput() and sets it as variable wordlist

#convert into dictionary:   
    freq = {} #empty dictionary
    print(wordlist)

#for loop to check if word is in dictionary and if so, increase count
    for word in wordlist: #check all words
        if word in freq: #if already in dictionary increase by 1:
            freq[word]=freq[word] + 1
        else:   #if not in dictionary, add it:
            freq[word]= 1

        
    print(freq) 

    sort=ranking(freq) #send dictionary to ranking()

    window(sort) #send the sorted list to window()
    
    
main()
