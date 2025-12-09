import random

countries = {"England": "London",
             "France" : "Paris",
             "Spain"  : "Madrid"}

nums_set = {1, 4, 3, 2, 4}

print(nums_set)

nums_set.add(5)

print(nums_set)

nums_set.remove(3)

print(nums_set)

str_set = {"Bob", "John", "Mary", "Alex", "Tod"}

print(str_set)

list1 = [2,4,6,1,5]
nums_set.update(list1)

print(nums_set)

##nums_set.clear()
##
##print(nums_set)

print("--")

setA = {1,2,3,4}
setB = {2,4,6,8}
setC = {1,2}

print(setA.union(setB))
print(setA.intersection(setB))
print(setA.difference(setB))
print(setB.difference(setA))
print(setA.symmetric_difference(setB))  # A' Union B'

if setC.issubset(setA) == True:
    print("Set C is subset of Set A")

