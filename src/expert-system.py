#!/usr/bin/env python
import sys

from functions import read_a_line, print_results, print_results_facts, letter_value, answers_list, conditions_list, \
    facts_list
from resolver import find_solution

# MAIN
print("Bienvenue dans ExSy !")

filetext = sys.argv[1:]
if not filetext or len(filetext) > 1:
    print("Erreur Merci de ne passer qu'un seul parametre a ExSy")
    sys.exit(0)

print("J'analyse votre fichier !")

with open(filetext[0], 'r') as file:
    line = file.readline()
    while line:
        if not read_a_line(line):
            success = 0
            sys.exit(0)
        line = file.readline()
print_results()
print("\n")
find_solution(letter_value, facts_list, conditions_list)
print_results_facts()
# resolve
