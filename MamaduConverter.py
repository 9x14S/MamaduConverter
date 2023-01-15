#! python3 
#A program to be run on the command line in windows, takes a specially formatted text file or files, opens and parses it 
#and then makes Anki cards out of the text.
#I know the program sucks but it is only a test project while I learn Python.

import sys, re, genanki, random

#Here I initialize the required variables, lists and RegEx pattern.
#This might need some extra cleaning.
rex = re.compile(r'\W-\W')
k = 0
forIteration = 0
deck =''
cardNum = 1
interfaceOption =''
filesToUse = []
deck = []

#This function prepares the file where badly formatted strings will be added.
def prepareNotAdded(file):
    if '.txt' not in file:
        file = file + '.txt'
    NotAdded = open('NotAdded-'+file, 'w')
    NotAdded.write("Here will be printed the lines with wrong formatting and extra lines. \nAlso, there may be any phrases with \"-\" as that's the regex pattern. \nSorry about that. \n\n")
    NotAdded.close()
    NotAdded = open('NotAdded-'+file, 'a')
    return NotAdded

#This function adds the curated data of a file to a deck, and then returns it.
def addCard(data, deck):
    whileLoopCounter = 0
    cardNum = 1
    while whileLoopCounter != len(data)-1:
        my_model = genanki.Model(random.randrange(1 << 30, 1 << 31), 'Simple Model', fields=[{'name':'Question'}, {'name':'Answer'}], templates=[{'name':'Card ' + str(cardNum),'qfmt':'{{Question}}', 'afmt':'{{FrontSide}}<hr id="answer">{{Answer}}', }])
        if data[whileLoopCounter] == '':
            break
        splitDataList = data[whileLoopCounter].split('\t')
        del data[whileLoopCounter]
        splitListCounter = 0
        while splitListCounter < len(splitDataList)-1:
            if splitDataList[splitListCounter] == '':
                del splitDataList[splitListCounter]
            else:
                splitListCounter += 1
        if len(splitDataList) == 1:
            del data[whileLoopCounter]
            whileLoopCounter += 1
            continue
        data.insert(whileLoopCounter, splitDataList)
        cardNum += 1
        my_note = genanki.Note(model=my_model, fields=[data[whileLoopCounter][0], data[whileLoopCounter][1]])
        deck.add_note(my_note)
        whileLoopCounter += 1
    return deck

#This is the main function, it curates the files, checks whether the help flag has been invoked and then calls the other
#functions. It returns a string if an error occurred and a list of the files provided if everything went well.
def main():
    global forIteration
    global deck
    global k
    global filesToUse

    #This part checks for if there are any files provided or if the help flag (-h) if present.
    filesToUse = sys.argv[1:]
    try:
        if (filesToUse[0] == '-h'):
            global interfaceOption
            interfaceOption = '-h'
            return '-h'
        print("Going to convert to Anki decks the following files: ", end='')
    except IndexError:
        return '\nThis program works by running it in the Windows CMD and providing the path or name of one or more .txt files. \nPlease, try again.'

    while k != len(filesToUse):
        print(filesToUse[k], end='')
        if len(filesToUse) >= 2:
            print(', ', end='')
        else:
            break
    print('\n\nNow converting...')

    #This loop calls the addCard function for each file provided, creating a deck from the data and an NotAdded text file.
    for numberOfFiles in filesToUse:
        my_deck = genanki.Deck(random.randrange(1 << 30, 1 << 31), 'Sourced from: ' + filesToUse[forIteration])
        try:
            fileObj = open(filesToUse[forIteration])
        except IndexError:
            return '\nThis program works by running it in the Windows CMD and providing the path or name of one or more .txt files. \nThis message appeared because one or more of the files couldn\'t be opened. \nPlease, try again.'
        contents = fileObj.read()
        contents = contents.split('\n')
        fileObj.close()
        NotAdded = prepareNotAdded(filesToUse[forIteration])
        p = 1
        while k != len(contents)-p:
            wkindex = contents[k]
            rexmatch = rex.search(wkindex)
            if (rexmatch != None) or ('\t' not in contents[k]):
                NotAdded.write(wkindex + '\n')
                del contents[k]
                p += 1
            else:
                k += 1
        deck.append(addCard(contents, my_deck))
        forIteration += 1
    NotAdded.close()
    return filesToUse

#This part checks whether this program has been used as a module. It is not my intent for this program to be used as a module so
#this will make it not run if it happens to be imported.
#Also, it prints 
if __name__ == '__main__':
    var = main()
    #If the type of var is String, then an error has happened or help has been demanded. If not then it has run successfully.
    if type(var) != str:
        print('\nThe program ran successfully. \nThe following decks have been made: ')
        for i in var:
            nameOfFile = i.strip('.txt') + '.apkg'
            genanki.Package(deck).write_to_file(nameOfFile)
            print(nameOfFile)
        interfaceOption = input('\nAlso a text file has been made with the badly formatted data of each file. \nPress return to exit.')
        exit()
    else: 
        #If var happens to be a String, this checks whether it was an error or the help flag was provided.
        if interfaceOption != '-h':
            print(var)
            interfaceOption = input('Press return to exit or type \'-h\' then press return to print help. ')
    if interfaceOption == '-h':
        print('Made by 9x14S as a personal learning project. This was made for xlDrake to make German Flashcards. \n\
            Feel free to use it any way you want. \n\nRun it by typing in the Windows CMD \'py TextFileToDeck.py\' changing the name if your \
                program is named something else. \nThen provide one or more text files formatted so that the question comes \
                    before the answer, are separated from each other by tabs and no dashes are present anywhere.\n  \
                        If you need extra help comment on the repo, I might help you even if I\'m a novice. ')
    else:
        exit()