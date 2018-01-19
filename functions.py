#!/usr/bin/env python

#tableaux pour stocker les reponses initiales, les conditions,et les réponses
answers_list = []
conditions_list = []
facts_list = []


# Verifie si une valeur est vraie ou pas, la fonction n'est évidemmeent pas fini,
# la ca vérifie juste danns le tableau
def check_true(val):
    if (val == 1):
        return 1
    print(facts_list)
    if (val in facts_list):
        return 1
    return 0

#Check si un fait est correct ou pas
def check_result(val1, val2 = None, operand = None):
    print(val1)
    print(operand)
    print(val2)
    if (not operand):
        print("pouet")
    if (operand == '+' and check_true(val1) and check_true(val2)):
        return 1
    if (operand == '|' and (check_true(val1) or check_true(val2))):
        return 1
    if (operand == '^' and check_true(val1) != check_true(val2)):
        return 1
    if (not operand and check_true(val1)):
        print("were in")
        print(val1)
        return 1
    return 0

#parse les conditions
def stockconditions(original_line):
    global conditions_list
    condition = original_line.split("\n")[0]

    condition_block = condition.split("=>")
    if (len(condition_block) != 2):
        return 0
    line_list = [list(condition_block[0]), condition_block[1]]
    conditions_list.append(line_list)
    return 1


##Stocke les faits
def stockfacts(line):
    global facts_list
    if (len(facts_list)):
        print("Erreur : Les faits sont déclarées 2 fois")
        return 0
    for letter in line:
        if (letter == '?'):
            continue
        if (letter == "#" or letter == '\n'):
            return 1
        if (not letter.isupper()):
            print("Erreur : Les faits ne doivent contenir que des lettres majuscules")
            return 0
        if (letter in facts_list):
            print("Erreur : Une valeur des faits a été déclarée 2 fois")
            return 0
        facts_list.append(letter)
    return 1

## Stocke les réponses auxquelle ont doit repondre
def stockanswers(line):
    global answers_list
    if (len(answers_list)):
        print("Erreur : Les réponses ont déja été déclarées")
        return 0
    for letter in line:
        if (letter == '='):
            continue
        if (letter == '#' or letter == '\n'):
            return 1
        if (not letter.isupper()):
            print("Erreur : Les réponses ne doivent contenir que des lettres majuscules")
            return 0
        if (letter in answers_list):
            print("erreur : Une valeur des réponses a été déclarée 2 fois")
            return 0
        answers_list.append(letter)
    return 1

#Lit une ligne d'un fichier et remplit les données de facon correcte
def read_a_line(original_line):
    line = original_line.replace(" ", "")
    if (len(line) < 2):
        return 1
    if (line[0] == '#'):
        return 1
    if (line[0] == '?'):
        return stockfacts(line)
    if (line[0] == '='):
        return stockanswers(line)
    return stockconditions(line)

#pas fini ofc, la ca rint que le tableau pour l'instant
def print_results():
    print ("Réponse : \n")
    print (answers_list)
    print ("\nFact : \n")
    print (facts_list)
    print ("\nLes conditions : \n")
    for condition in conditions_list:
        print(condition)
