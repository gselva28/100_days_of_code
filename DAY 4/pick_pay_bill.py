import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

nameAsCSV = input("Give me everybody's names, separated by a comma. ")
names = nameAsCSV.split(", ")

print(names)
