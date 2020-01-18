# Objective: The goal of this project is to make an expert system for propositional calculus
# Summary: Build a list of all possible True False values in a Truth Table

# The program must accept one parameter, which is the input file. It will contain a list of rules, then a list of initial facts, then a list of queries. For each of these queries, the program must, given the facts and rules given, tell if the query is true, false, or undetermined.
# By default, all facts are false, and can only be made true by the initial facts statement, or by application of a rule. A fact can only be undetermined if the ruleset is ambiguous, 
# Key idea: A Truth table is essentially a list of binary variables
# 
# Operations:
#     ! : NOT
#     + : AND
#     | : OR
#     ^ : XOR
#     => : IMPLIES
#     <=> : IF AND ONLY IF

import string
from read_file import readfile
from process_lines import process_lines, set_initial_facts, process_rules, work_out_rules, answer_q
from values import rules, queries, inital_facts, facts, implications, bi_implications


file_text = readfile()
# print(file_text)
file_text = file_text.split('\n')
# print(file_text)
# Process the lines into arrays.
process_lines(file_text)
# print("Rules", rules)
# print("Queries", queries)
# print("initial facts", inital_facts)
# Set the intial facts in to true
set_initial_facts()
# print(facts)
process_rules(rules)
print("implications", implications)
print("bi_implications", bi_implications)

# workout the  rules.
work_out_rules()
print("Facts", facts)

print("Workout the values again")
work_out_rules()
print('\n\nFacts', facts)

# print("Workout the values again")
# work_out_rules()
# print('\n\nFacts', facts)



print(queries)
# answer queries
answer_q()