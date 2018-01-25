#!/usr/bin/env python

from functions import check_result


def find_value_left_letter(conditions2, letter_value, conditions_list):
    element_value = []
    for condition in conditions2:
        print(condition)
        if condition.isupper():
            if letter_value[condition] == "true":
                print(element_value, " append true")
                element_value.append("true")
            else:
                print("on va chercher : ", condition)
                value = find_letter_in_condition(conditions_list, condition, letter_value)
                print("retour1 : ", value, " = ", condition)  # true or false de la lettre on cherche la suivante.
                print(element_value, " append ", value)
                element_value.append(value)
        else:
            print(element_value, " append ", condition)
            element_value.append(condition)
    if len(element_value) == 0:
        print(element_value, " append false")
        element_value.append("false")
    return element_value


def find_letter_in_condition(conditions_list, fact, letter_value):
    print("On cherche pour la lettre : ", fact)
    for conditions in conditions_list:
        if len(conditions[-1]) == 1:
            if conditions[-1][0] == fact:
                print(conditions[-2], "pour ", fact)
                value = find_value_left_letter(conditions[-2], letter_value, conditions_list)
                # check la taille de value pour faire des boucles dessus
                if len(value) > 3:
                    while len(value) > 3:
                        value[0] = check_result(value[0], value[2], value[1])
                        del value[1:2]
                print("retour2 : ", value[0], value[1], value[2], " = ", fact)
                result = check_result(value[0], value[2], value[1])
                letter_value[fact] = result
                print("fact : ", fact, "value : ", letter_value[fact])
                print(letter_value)
                return result
        else:
            for condition1 in conditions[-1]:
                if condition1 == fact:
                    print(conditions[-2], "pour ", fact)
                    value = find_value_left_letter(conditions[-2], letter_value, conditions_list)
                    print("retour3 : ", value[0], value[1], value[2], " = ", fact)
                    result = check_result(value[0], value[2], value[1])
                    letter_value[fact] = result
                    print("fact : ", fact, "value : ", letter_value[fact])
                    return result
    return "false"


def find_solution(letter_value, facts_list, conditions_list, answers_list):
    for fact in facts_list:
        if letter_value[fact] != "true":
            print("find the solution !", fact)
            result = find_letter_in_condition(conditions_list, fact, letter_value)
            print ("result : ", result)
