# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 23:17:56 2023
"""

import csv

STR_DIGIT_ARRAY = ["0","1","2","3","4","5","6","7","8","9"]
SPELLED_DIGIT_DICT_CORRESPONDANCE = {"one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}
SMALLER_SPELLED_DIGIT_SIZE = 3
SPELLED_DIGITS = SPELLED_DIGIT_DICT_CORRESPONDANCE.keys()
FIRST_INDEX = 0
FILEPATH = "Input.txt"

def GetLineList(filepath):
    """
    filepath est un chemin vers un fichier texte.
    A noter : le fichier texte sera encodé en utf-8.
    """
    
    lineList = []
    
    # on ouvre en lecture seule
    with open(filepath, "r", encoding="utf-8") as txt:
        
        for ligne in txt: # on parcourt les lignes du fichier texte
            lineList.append(ligne) # on ajoute la ligne
                    
    return lineList


def GetListOfNumbersFromLines(lines):
    
    listOfNumbers = []
    
    for line in lines:
        twoDigitsArray = GetFirstAndLastDigits(line)
        # on concatene les deux chiffres pour former un nombre entier
        wholeNumber = int(str(twoDigitsArray[0]) + str(twoDigitsArray[1]))
        
        listOfNumbers.append(wholeNumber)
    
    return listOfNumbers


def GetSumOfNumbersFromList(listOfNumbers):
    
    sumOfNumbers = 0
    
    for number in listOfNumbers:
        sumOfNumbers += number
        
    return sumOfNumbers


def GetFirstAndLastDigits(line):
    
    firstDigit = -1
    lastDigit = -1
    
    i = 0
    
    # tant que la ligne n'est pas lu en entiere - 2 car les deux dernieres lettres n'importent pas si la 3eme lettre en partant de la fin ne correspond a rien
    while i < len(line):
        
        # si c'est un chiffre
        if (line[i] in STR_DIGIT_ARRAY):
            
            # on regarde si on a pas deja un premier chiffre d'enregistrer
            if (firstDigit == -1):
                firstDigit = int(line[i]) # si ce n'est pas le cas, on le met en tant que premier chiffre
            lastDigit = int(line[i]) # on l'ajoute quoi qu'il arrive en dernier chiffre (car on itere a travers toute la ligne)
            
            i += 1
        else:
            
            # on fait une copie de tous les mots possibles correspondant a des digits
            possibleSpelledDigits = list(SPELLED_DIGITS)
            
            #print(possibleSpelledDigits)
            
            indexCorrespondence = 0 # il permet de comparer les lettres a un mot de currestSpelledDigits
            
            # le mot que l'on cree
            currentDetectedWord = ""
            
            wordFounded = False
            
            # tant que la liste de mot possible n'est pas vide et qu'on a pas deja trouve un mot a partir de lettre a l'indice "i"
            while len(possibleSpelledDigits) > 0 and wordFounded == False:
                
                # si la lettre ne correspond pas a la lettre du mot que l'on compare
                if (line[i + indexCorrespondence] != possibleSpelledDigits[FIRST_INDEX][indexCorrespondence]):
                    currentDetectedWord = "" # on reset le mot cree pour pouvoir le reconstruire
                    indexCorrespondence = 0 # on reset l'index de correspondance
                    del possibleSpelledDigits[FIRST_INDEX] # on retire le mot de la liste
                    
                else:
                    currentDetectedWord += str(line[i + indexCorrespondence]) # on ajoute la lettre au mot cree
                    
                    if (currentDetectedWord == possibleSpelledDigits[FIRST_INDEX]): # si le mot cree correspondant au mot de la liste
                        wordFounded = True # on a trouve un chiffre !
                    else:
                        indexCorrespondence += 1 # on incremente l'index correspondance
                    
            if (currentDetectedWord != ""): # si on a trouve un mot
            
                digit = SPELLED_DIGIT_DICT_CORRESPONDANCE[currentDetectedWord] # on trouve le chiffre correspondant au mot, digit est un entier
                
                # meme chose que pour le cas de line[i] en tant que chiffre
                if (firstDigit == -1):
                    firstDigit = digit
                lastDigit = digit
                
                i += 1 #indexCorrespondence # on ajoute la correspondance trouve, comme cela, on evite de regarder les lettres du mots trouves (gain de temps)
            else:
                i+= 1
    
    # on retourne un array de deux entiers
    return (firstDigit, lastDigit)
        
"""
Demarche d'utilisation:
    avoir un fichier "Input.txt" avec toutes les lignes de l'Input dans le meme dossier que ce fichier python.
    OU changer la constante FILEPATH pour rediriger vers le dossier des lignes de texte de L'input.

Puis run ce fichier python

Ecrire Compute() dans la console et regarder le resultat !
"""
    
def Compute():
    
    lines = GetLineList(FILEPATH)
    numbers = GetListOfNumbersFromLines(lines)
    answer = GetSumOfNumbersFromList(numbers)
    
    print(answer)