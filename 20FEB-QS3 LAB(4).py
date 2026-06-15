#qs3
# Write a Python program to perform the following operations on sets:

# a) Check whether one set is a subset of another set.

# b) Check whether two sets are disjoint.

# c) Remove all elements from a set.

# d) Find the common elements present in three different sets.

# e) Remove duplicate words from a given sentence using sets.

set1={22,33,4,5,6,7,56,78}
set2={22,23,4,5,12,34,76,69}

print(set1.issubset(set2))
print(set2.issubset(set1))
print(set1.isdisjoint(set2))
set1.clear()
print(set1)

sentence=input("enter the sentence with appropriate spaces")
words=[x for x in sentence.split()]
words=set(words)
print(*words) 