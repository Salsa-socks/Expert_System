# bnkosi
# Jan 2020
# Objective: The goal of this project is to make an expert system for propositional calculus
# Summary: Build a list of all possible True False values in a Truth Table

# The program must accept one parameter, which is the input file. It will contain a list of rules, then a list of initial facts, then a list of queries. For each of these queries, the program must, given the facts and rules given, tell if the query is true, false, or undetermined.
# By default, all facts are false, and can only be made true by the initial facts statement, or by application of a rule. A fact can only be undetermined if the ruleset is ambiguous, 
# Key idea: A Truth table is essentially a list of binary variables

var_list = ['a','b','c','d']
line = []
num_of_rows = len(var_list) ** 2
widest_num = len(str(bin(num_of_rows - 1)[2:]))

for i in reversed(range(num_of_rows)):
    current_bin = bin(i)[2:].zfill(widest_num)
    for letter in str(current_bin):
        if letter == '0':
            line.append('False')
        elif letter == '1':
            line.append('True')

print(line)         