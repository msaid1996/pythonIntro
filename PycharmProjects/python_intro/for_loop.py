print("--------------------------LIST----------------------")
list = [1,2,3,4,5,6]
for num in list:
    if num == 3:
        print("three")
    elif num>3:
        print("more than three")
    else:
        print("too soon")

print("--------------------LIST WITHIN LIST-----------------")
list_num = [[1, 2, 3], [4, 5, 6]]
for i in list_num:
    print(i)                #returns the sublist [1,2,3] then [4,5,6]
    for num in i:
        print(num)          #returns the each item in the sub list: 1,2,3 then 4,5,6

print("--------------------LIST WITHIN LIST 2-----------------")
list_num = [[1, 2, 3], [4, 5, 6]]
for i in list_num:
    print(i)                #returns the sublist [1,2,3] then [4,5,6]
    for num in i:
        print(num+3)


print("-----------------DICTIONARY----------------------------------")
print("----1---")
dict_data = {1: {"name": "Jon", "money": 2500},
             2: {"name": "mike", "money": 45900},
             3: {"name": "brandon", "money": 12}
}

for x in dict_data:
    print(x)            #print the keys only: 1,2,3

for x in dict_data.values():
    print(x)            #prints the values for each key of 1,2,3

for x in dict_data.values():
    print(x)
    for item in x:
        print(item)     #prints the keys within the dict: name & money

for x in dict_data.values():
    print(x)
    for item in x.values():
        print(item)     #prints the keys within the dict: john, 2500 then mike 45900 then brandon,12

print("--------------------EXERCISE-----------------")

for i in range(1,50):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)

print("----------------------------FOR & INPUT---------------------------")
a=input("What is your first range?  ")
b=input("What is your last range?  ")
new_A=int(a)
new_B=int(b)

for x in range(new_A,new_B):
    if x % 3 == 0 and x % 5 == 0:
        print("fizzbuzz")
    elif x % 3 == 0:
        print("fizz")
    elif x % 5 == 0:
        print("buzz")
    else:
        print(x)
