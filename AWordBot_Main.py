"""
AWordBot_Main.py : Given a word, gets the meaning, synonyms and antonyms for the word
"""
import PySimpleGUI as sg
from Utilities import get_meaning,get_synonyms,get_antonyms

greeting = "Hi, I am a Word Bot. I can help you with words \n \n"

layout = [
    [sg.Image("Title.png" ,  size = (800,150) , background_color = "white")],
    [sg.InputText("",font = ("Simplified Arabic",14), pad = (160,15), size=(50, 1), key='input', enable_events=True)],
    [sg.Button("Meaning", font=("Simplified Arabic Fixed", 14), bind_return_key=True, key='meaning' , pad = ((175,10) , (10,30))),
     sg.Button("Synonyms",font=("Simplified Arabic Fixed", 14), key='synonym', pad = ((10,10) , (10,30))),
     sg.Button("Antonyms",font=("Simplified Arabic Fixed", 14), key='antonym', pad = ((10,10) , (10,30))),
     sg.Button("Clear", font=("Simplified Arabic Fixed", 14), key='clear', pad = ((10,10) , (10,30)))
    ],
    [sg.Multiline(greeting, font=("Simplified Arabic Fixed", 13), size=(70, 15), key='output' , pad = ((30,0),(0,0)))],
    [sg.Image("Creator.png" ,  size = (800,150) , background_color = "white")]
]

def display_meaning(word):
    """
    Displays the word and the meaning of the word
    :param word: string, input word
    """
    meaning = get_meaning(word)
    if meaning:
        window['output'].print( word.capitalize(),"meaning",meaning + "\n")
    else:
        display_error("Word is not found in corpus")


def display_error(message):
    """
    Displays an error message in the output window
    :param message: string, the error message to be displayed
    """
    window['output'].print("ERROR: " + message,"\n", text_color='red')


def display_antonym(word):
    """
    Displays the antonym of the word
    :param word: string, input word
    """
    antonym = {}
    antonym = list(get_antonyms(word))
    if antonym:
        window['output'].print( "Antonym of",word.capitalize()+ ": "+str(antonym[0]) + "\n")
    else:
        display_error("No Antonyms are available")


def display_synonyms(word):
    """
    Displays the synonyms of the word
    :param word: string, input word
    """
    synonyms = {}
    synonyms = list(get_synonyms(word))
    synonyms = ",".join(synonyms)
    if synonyms:
        window['output'].print( "Synonyms of",word.capitalize()+ ": "+synonyms + "\n")
    else:
        display_error("No Synonyms are available")


if __name__ == '__main__':
    window = sg.Window('Word Bot', layout , size = (800 , 700) , background_color = "white")

    while True:
        event, values = window.Read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'meaning':
            display_meaning(values['input'])
        elif event == 'antonym':
            display_antonym(values['input'])
        elif event == 'synonym':
            display_synonyms(values['input'])
        elif event == 'clear':
            window.FindElement('output').Update(greeting)
    window.Close()
