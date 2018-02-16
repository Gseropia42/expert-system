#!/usr/bin/env python
# coding=utf-8

from functions import check_result


def len_array(array):
    length = 0
    for index in array:
        if index != '!' and index != '(' and index != ')':
            length += 1
    return length


def replace_exclamation_point(array):
    length = 0
    for index in array:
        if index == '!':
            array[length + 1] = 'true' if array[length + 1] == 'false' else 'false'
            del array[length]
        length += 1
    return array


def move_parentheses(array, debut_1, debut_2, fin):
    print ("debut move_parentheses : ", array, debut_1, debut_2, fin)
    if debut_2 == -1:
        del array[debut_1]
        del array[fin - 1]
        debut_1 -= 1
        fin -= 1
        while debut_1 < fin:
            array.insert(0, array.pop(debut_1))
            print ("here1 ", array, debut_1, fin)
            debut_1 += 1
    else:
        del array[debut_2]
        del array[fin - 1]
        debut_1 += 1
        debut_2 -= 1
        fin -= 1
        print (array)
        while debut_2 < fin:
            array.insert(debut_1, array.pop(debut_2))
            print ("here2 ", array, debut_1, debut_2, fin)
            debut_2 += 1
    print (array)
    return array


def replace_and_move_parentheses(array):
    print ("debut replace parentheses : ", array)
    while '(' in array or ')' in array:
        save_index_debut_1 = -1
        save_index_debut_2 = -1
        save_index_fin = -1
        length = 0
        for index in array:
            if index == '(':
                if save_index_debut_1 == -1:
                    save_index_debut_1 = length
                elif save_index_debut_2 == -1:
                    save_index_debut_2 = length
                else:
                    save_index_debut_1 = save_index_debut_2
                    save_index_debut_2 = length
            if index == ')' and save_index_fin == -1:
                save_index_fin = length
            length += 1
        if save_index_debut_1 == 0 and save_index_debut_2 == -1:
            del array[save_index_fin]
            del array[0]
            print (array)
            return array
        array = move_parentheses(array, save_index_debut_1, save_index_debut_2, save_index_fin)
    return array

#E + (F + (G + (H + I)))
#E + (F + (H + I + G))
#E + (H + I + G + F)
#H + I + G + F + E

def find_value_letter(conditions2, letter_value, conditions_list):
    element_value = []
    index = 0
    for condition in conditions2:
        print(condition)
        if condition.isupper():
            if letter_value[condition] == "true":
                print(element_value, " append true")
                element_value.append("true")
            else:
                value = find_letter_in_condition(conditions_list, condition, letter_value)
                print("retour1 : ", value, " = ", condition)  # true or false de la lettre on cherche la suivante.
                print(element_value, " append ", value)
                element_value.append(value)
        else:
            print(element_value, " append ", condition)
            element_value.append(condition)
        index += 1
    if len(element_value) == 0:
        print(element_value, " append false")
        element_value.append("false")
    return element_value


def find_letter_in_condition(conditions_list, fact, letter_value):
    print("On cherche pour la lettre : ", fact)
    save_len = 0
    save_index = 0
    index = 0
    find = "false"
    for conditions in conditions_list:
        if len(conditions[-1]) == 1:
            if conditions[-1][0] == fact:
                # print(len_array(conditions[0]), save_len, index, save_index)
                if len_array(conditions[0]) < save_len or save_len == 0:
                    # print("in1")
                    find = "true"
                    save_index = index
                    save_len = len(conditions[0])
        else:
            for condition1 in conditions[-1]:
                if condition1 == fact:
                    # print(len_array(conditions[0]), len_array(conditions[-1]), save_len, index, save_index)
                    if (len_array(conditions[0]) + len_array(conditions[-1]) - 1) < save_len or save_len == 0:
                        # print("in")
                        find = "true"
                        save_index = index
                        save_len = (len_array(conditions[0]) + len_array(conditions[-1]) - 1)
        index += 1
    if find == "false":
        return "false"
    print("la taille est de : ", save_len, "et l'index est : ", save_index, conditions_list[save_index])
    if len(conditions_list[save_index][-1]) == 1:
        print(conditions_list[save_index][-2], "pour ", fact)
        value = find_value_letter(conditions_list[save_index][-2], letter_value, conditions_list)
        print (value)
        if len(value) != len_array(value):
            print ("replace_exclamation_point")
            value = replace_exclamation_point(value)
        if len(value) != len_array(value):
            print ("replace and move parentheses")
            value = replace_and_move_parentheses(value)
        while len(value) > 3:
            value[0] = check_result(value[0], value[2], value[1])
            print(value)
            del value[2]
            del value[1]
            print(value)
        if len(value) == 1:
            print ("value[0] : ", value[0])
            letter_value[fact] = value[0]
        else:
            print("retour2 : ", value[0], value[1], value[2], " = ", fact)
            letter_value[fact] = check_result(value[0], value[2], value[1])
        print("fact : ", fact, "value : ", letter_value[fact])
        print(letter_value)
        return letter_value[fact]
    else:
        find = "false"
        for condition1 in conditions_list[save_index][-1]:
            if condition1 == fact:
                find = "true"
                # Si on trouve notre bonheur ici, il faudra aussi calculer les autres pour savoir le résultat éxact
                print(conditions_list[save_index][-2], "pour ", fact)
                value = find_value_letter(conditions_list[save_index][-2], letter_value, conditions_list)
                print("retour3 : ", value[0], value[1], value[2], " = ", fact)
                letter_value[fact] = check_result(value[0], value[2], value[1])
                print("fact : ", fact, "value : ", letter_value[fact])
                print(letter_value)
                return letter_value[fact]
        if find == "true":
            index = 0
            for condition1 in conditions_list[save_index][-1]:
                if condition1 != fact:
                    value = find_value_letter(condition1, letter_value, conditions_list)
                    # Si on a A + B + C on va faire A + B et supprimer + B remplacer A par le résultat (true or false) on aura true/false + C
                    if len(value) != len_array(value):
                        print ("replace_exclamation_point")
                        value = replace_exclamation_point(value)
                    if len(value) != len_array(value):
                        print ("replace and move parentheses")
                        value = replace_and_move_parentheses(value)
                    while len(value) > 3:
                        value[0] = check_result(value[0], value[2], value[1])
                        del value[2]
                        del value[1]
                    # Et ici nous allons fait true/false + C
                    letter_value[condition1] = check_result(value[0], value[2], value[1])
                    conditions_list[save_index][-1][index] = letter_value[condition1]
                    # faire le calcul global pour finir
                index += 1
    return "false"


def find_solution(letter_value, facts_list, conditions_list):
    for fact in facts_list:
        if letter_value[fact] != "true":
            print("find the solution !", fact)
            result = find_letter_in_condition(conditions_list, fact, letter_value)
            print ("result : ", result)
