###################################################
# DATA STRUCTES
###################################################

###############################
# NUMBERS

# numbers: integer
x = 46
type(x)

# numbers: float
x = 10.3
type(x)

# numbers: complex
x = 2j+1
type(x)

####################################
# STRINGS

long_str = """Data acquisition systems make it possible 
for users to access the database, as well as recover information 
for processing and analysis."""

name = "Hilal"
name[0]
name[0:2]

"data" in long_str


###################
# STRING METHODS

name = "hilal"
type(name)
type(len)

len(name)
len('Data acquisition systems make it possible for users to access the database')
#How can we identify if the structure we are using is a method or a function?
#If a function is defined within a class structure, it is called a method.
#If a function is defined within a class structure, it is called a method.

#upper() & lower() method
"data".upper()
"DATA".lower()

#replace method
hi = "data acquisition system"
hi.replace("a", "e")

#split method
"data acquisition system".split()

#capitalize method
"data".capitalize()

#############################################
#LIST
# repalceable, in order, inclusive

notes = [1, 2, 3, 4]
type(notes)
names = ["a", "b", "c", "d"]
not_nam = [1, 2, 3, "a", "b", True, [1, 2, 3]]

not_nam[0]
not_nam[5]
not_nam[6]
not_nam[6][1]

notes[0] = 10

#append method: listeye ekleme yapar
notes
notes.append(100)

#pop method: indexe göre siler
notes.pop(0)

#insert method: indexe ekler
notes.insert(2, 5)   #Out[35]: [2, 3, 5, 4, 100]

########################################
#TUPLE
# uncgangeable, in order, inclusive

t = ("hilal", "data", 1, 2)
type(t)
t[0]
t[0:3]

t[0] = 99 #TypeError: 'tuple' object does not support item assignment
t = list(t)
t[0] = 99
t = tuple(t)


########################################
#SET
# replaceable, out of order + unique, inclusive

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

# set1'de olup set2'de olmayanlar
set1.difference(set2)
set1 - set2

# set2'de olup set1'de olmayanlar
set2.difference(set1)
set2 - set1

# symmetric_difference(): elements that are not common between two sets
set1.symmetric_difference(set2)
set2.symmetric_difference(set1)

#intersection(): intersection of two sets
set1.intersection(set2)
set2.intersection(set1)
set1 & set2

# union(): union of two sets
set1.union(set2)
set2.union(set1)

# isdisjoint(): Is the intersection of two sets empty?
# If there is an is statement at the beginning of the methods used,
# a return of true or false is expected.
set1 = set([7, 8, 9])
set2 = set([5, 6, 7, 8, 9, 10])

set1.isdisjoint(set2) #False

# issubset(): Is one set a subset of another set?
set1.issubset(set2) #True
set2.issubset(set1) #False