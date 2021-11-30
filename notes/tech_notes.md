# Technical Notes for Eleanor's Adventor

## Text Parser
In the sample program 'Title', I currently have two word lists, a YES list and a NO list.

```python
    yesList = ['YEA', 'YES', 'Y', 'Yea', 'Yes', 'yea', 'yes', 'y']
    noList = ['NAH', 'NO', 'N', 'Nah', 'No', 'n', 'nah', 'no']
```
When the program asks for an input, it then checks the answer against the 2 lists. If the answer is in the Yes list, it does the yes action, no list it does the no action, and if the answer is not in a list it throws an error.

```python
    if ans in yesList:
        clearConsole()
        print("THE ADVENTURE BEGINS!")
    elif ans in noList:
        clearConsole()
        print("Tommorow I'll be all the things I tried to be today.")
    else:
        drawTitleScreen("I'm sorry, I do not understand {}.".format(ans))
```
Currently, if a more complex answer is provided, like `> Yes I am Ready`, the system will throw an error. 

I need to find a way to logically parse the input and determine if the the phrase is an affirmitive or a negative.

 ## Map Creation

 ## Economy

 ## Iventory
 Key items from adventures should be made available to use in other adventures. Items should be broken into several catagories, Some that can be used only in an adventure, and some that will stay in the "toy chest" and can be used in other adventures.
