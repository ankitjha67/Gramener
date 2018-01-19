L1=['a','b','c']                           # List 1
L2=['b','d']                               # List 2
for i in L1:                               # For loop to find same element in both Lists
    if i in L2:
        print("Common Elements", i)        # Print the common element

L1=['a','b','c']                           # List 1
L2=['b','d']                               # List 2
for j in L1:                               # For loop to find elements in L1 and not in L2
    if j not in L2:
        print("Elements present in L1 and not in L2", j)