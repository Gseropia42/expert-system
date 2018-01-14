#!/usr/bin/env python
import sys

from functions import read_a_line, print_results
from resolver import *



#MAIN
print("Bienvenue dans ExSy !")

filetext = sys.argv[1:]
if not filetext or len(filetext) > 1:
    print ("Erreur ! Merci de ne passer qu'un seul paramètre à ExSy")
    sys.exit(0)

print("J'analyse votre fichier !")

with open(filetext[0], 'r') as file:
    line = file.readline()
    while line:
        if (not read_a_line(line)):
            success = 0
            sys.exit(0)
        line = file.readline()
print_results()
# resolve