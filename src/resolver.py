#!/usr/bin/env python

def find_letter_in_condition(conditions_list, fact, letter_value):
    print("On cherche pour la lettre : ", fact)
    for conditions in conditions_list:
        if len(conditions[-1]) == 1:
            if conditions[-1][0] == fact:
                print(conditions[-2], "pour ", fact)
                for condition in conditions[-2]:
                    if condition.isupper():
                        if letter_value[condition] == "true":
                            print(condition, "true")
                        else:
                            find_letter_in_condition(conditions_list, condition, letter_value)
                    #print(condition[-1][0], len(condition[-1]))
        else:
            for condition1 in conditions[-1]:
                if (condition1 == fact):
                    print(conditions[-2], "pour ", fact)
                    for condition in conditions[-2]:
                        if condition.isupper():
                            print(condition)
                            if letter_value[condition] == "true":
                                print(condition, ": true")
                            else:
                                find_letter_in_condition(conditions_list, condition, letter_value)

def find_solution(letter_value, facts_list, conditions_list, answers_list):
    for fact in facts_list:
        if letter_value[fact] != "true":
            print("find the solution !", fact)
            find_letter_in_condition(conditions_list, fact, letter_value)
