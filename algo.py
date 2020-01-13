# Objective: The goal of this project is to make an expert system for propositional calculus
# Summary: Build a list of all possible True False values in a Truth Table

# The program must accept one parameter, which is the input file. It will contain a list of rules, then a list of initial facts, then a list of queries. For each of these queries, the program must, given the facts and rules given, tell if the query is true, false, or undetermined.
# By default, all facts are false, and can only be made true by the initial facts statement, or by application of a rule. A fact can only be undetermined if the ruleset is ambiguous, 
# Key idea: A Truth table is essentially a list of binary variables