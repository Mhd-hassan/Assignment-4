# Python Loop Manipulation Technique
# Python Else with While loop-1
i=0
while i<5:
    i+=1
    print("i : ",i)
else:
    print("Else block is executed.")
"""
Output of Else with While Loop:
i :  1
i :  2
i :  3
i :  4
i :  5
Else block is executed.
"""
# Python Else with For Loop-2
l=[1,2,3,4,5]
for a in l:
    print(a)
else:
    print("Else block ie executed.")
"""
Output of Else with For Loop:
1
2
3
4
5
Else block ie executed.
"""
# Python Break Statement in For Loop-3
for letter in "Hello":
    if letter=='e' or letter=='o':
        break
print("Current letter is : ",letter)
"""
Output of Break statement in For Loop:
Current letter is :  e
"""
# Python Pass Statement in For Loop-4
for letter in "Hello":
    pass
print("Last later is : ",letter)
"""
Output of Pass Statement in For Loop:
Last later is :  o
"""
# Python Continue Statement in For Loop-5
for letter in "Hello":
    if letter=='e' or letter=='o':
        continue
    print("Current letter is : ",letter)
"""
Output of Continue Statement in For Loop:
Current letter is :  H
Current letter is :  l
Current letter is :  l
"""
# Python Break Statement in While Loop-6
i=1
while i<=10:
    print(i)
    if i==7:
        break
    i+=1
"""
Output of Break Statement in While Loop:
1
2
3
4
5
6
7
"""
"""
Entire Python Program output:
i :  1
i :  2
i :  3
i :  4
i :  5
Else block is executed.
1
2
3
4
5
Else block ie executed.
Current letter is :  e
Last later is :  o
Current letter is :  H
Current letter is :  l
Current letter is :  l
1
2
3
4
5
6
7
"""