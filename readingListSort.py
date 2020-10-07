#!/usr/bin/env python3

# readinglistsort.py: A simple Python app that allows you to quickly sort a long reading list so that the books you're most interested in end up on top. To make this work, replace the variable 'readingListFile' with the location of your reading list text file.

import random
from pathlib import Path
import pyautogui

# replace with the location of your reading list text file
readingListFile = '/path/to/your/readinglist.txt'

# open the reading list file
p = open(readingListFile, 'r')
readingList = p.read()
readingList = list(readingList.splitlines())

# display the first alert box
pyautogui.alert(text='Choose which book you\'d rather read right now. Close the window to stop and display the book you should read next.')

# sets the chosenBook variable default
rounds = 0

# main loop
while True:
    # this if statement ensures that the book at the top of the list is regularly being tested
    if rounds % 5 == 0:
        book1 = readingList[0]
    else:
        book1 = random.choice(readingList)
    book2 = random.choice([i for i in readingList if i != book1]) # makes sure book2 never equals book1
    index1 = readingList.index(book1)
    index2 = readingList.index(book2)
    chosenBook = pyautogui.confirm(text=book1 + '\n\n' + ' VS.' + '\n\n' + book2, title='Your Next Book', buttons=['Book 1', 'Book 2'])
    
    try:
        if chosenBook == 'Book 1':
            rounds += 1
            # moves Book 1 index above Book 2 in the list unless it is already above
            if index1 < index2:
                continue
            elif index1 > index2 and index2 > 0:
                newindex = index2-1
                readingList.insert(newindex, readingList.pop(index1))
            elif index1 > index2 and index2 == 0:
                newindex = 0
                readingList.insert(newindex, readingList.pop(index1))
        elif chosenBook == 'Book 2':
            rounds += 1
            # moves Book 2 index above Book 1 in the list unless it is already above
            if index2 < index1:
                continue
            elif index2 > index1 and index1 > 0:
                newindex = index1-1
                readingList.insert(newindex, readingList.pop(index2))
            elif index2 > index1 and index1 == 0:
                newindex = 0
                readingList.insert(newindex, readingList.pop(index2))
        else:
            pyautogui.alert(text=str(readingList[0]), title='Read this first:', button='OK')
            break
    
    except ValueError:
        pyautogui.alert(text=str(readingList[0]), title='Read this first:', button='OK')
        # converts the list back to string
        def listToPrettyString(list):
            return str(list).replace("[","").replace("]","").replace("'","").replace(', ','\n')
        # saves the new list to the reading list file
        newList = listToPrettyString(readingList)
        p = open(readingListFile, 'w')
        p.write(newList)
        p.close()
        break