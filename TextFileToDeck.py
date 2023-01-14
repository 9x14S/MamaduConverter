#! python3 
#A program to be run on the command line in windows, takes a specially formatted text file or files, opens and parses it 
#and then makes Anki cards out of the text.
#I know the program sucks but it is only a test project while I learn Python.

import sys, re, genanki, random


rex = re.compile(r'\W-\W')
k = 0
xs =''
filesToUse = ''
list(filesToUse)


def prepareNotAdded():
    NotAdded = open('NotAdded.txt', 'w')
    NotAdded.write("Here will be printed the lines with wrong formatting and extra lines. \nAlso, there may be any phrases with \"-\" as that's the regex pattern. \nSorry about that. \n\n")
    NotAdded.close()
    NotAdded = open('NotAdded.txt', 'a')
    return NotAdded


def main():
    global k
    global filesToUse
    filesToUse = sys.argv[1:]
    try:
        if (filesToUse[0] == '-h'):
            global xs
            xs = '-h'
            return '-h'
        fileObj = open(filesToUse[0])
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
    contents = fileObj.read()
    contents = contents.split('\n')
    fileObj.close()
    NotAdded = prepareNotAdded()
    p = 0
    while k != len(contents)-1:
        wkindex = contents[k]
        if k >= len(contents)-p:
            break
        rexmatch = rex.search(wkindex)
        if (rexmatch != None):
            NotAdded.write(wkindex + '\n')
            del contents[k]
            p += 1
        if ('\t' not in contents[k]):
            NotAdded.write(wkindex + '\n')
            del contents[k]
            p += 1
        else:
            k += 1

    NotAdded.close()
    outtst = open('out.txt', 'w')
    outtst.write('\n'.join(contents))
    outtst.close()
    return filesToUse

    








if __name__ == '__main__':
    var = main()
    if type(var) != str:
        print('\nThe program ran successfully. \nThe following decks have been made: ')
        for i in var:
            print(i.strip('.txt') + '.apkg')
        xs = input('\nPress return to exit.')
        exit()
    else: 
        if xs != '-h':
            print(var)
            xs = input('Press return to exit or type \'-h\' then press return to print help. ')
    if xs == '-h':
        print('help. lol')
    else:
        exit()