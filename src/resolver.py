#!/usr/bin/env python

def find_value_left_letter(conditions1, conditions2, fact, letter_value, conditions_list):
    if conditions1 == fact:
        print(conditions2, "pour ", fact)
        for condition in conditions2:
            print(condition)
            if condition.isupper():
                if letter_value[condition] == "true":
                    print(condition, "true")
                else:
                    print("on va chercher : ", condition)
                    find_letter_in_condition(conditions_list, condition, letter_value)

def find_letter_in_condition(conditions_list, fact, letter_value):
    print("On cherche pour la lettre : ", fact)
    for conditions in conditions_list:
        if len(conditions[-1]) == 1:
            find_value_left_letter(conditions[-1][0], conditions[-2], fact, letter_value, conditions_list)
        else:
            for condition1 in conditions[-1]:
                find_value_left_letter(condition1, conditions[-2], fact, letter_value, conditions_list)

def find_solution(letter_value, facts_list, conditions_list, answers_list):
    for fact in facts_list:
        if letter_value[fact] != "true":
            print("find the solution !", fact)
            find_letter_in_condition(conditions_list, fact, letter_value)
