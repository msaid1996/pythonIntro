print("-------------------------------- DEF FUNCTION ---------------------------------------------------------")

def add(num1, num2):
    return num1 + num2

print(add(2,2))



print("--------------------------------LAMBDA FUNCTION-----------------------------------------------")
print("*** use Lambda Function: similar to def but is a quicker, shorter written code ***")

addition = lambda num1, num2: num1 + num2               #similar to def function, but summarises it - quicker & shorter to use than def funct
print(addition(2,2))



print("------------------------------- EXERCISES: Lambda --------------------------------------------")

values = [234.0, 555.0, 674.00, 78.00]
#bonus = lambda x: x * 1.1, values                            # returns summary: (<function <lambda> at 0x000001D07921E1F0>, [234.0, 555.0, 674.0, 78.0])
#bonus = map(lambda x: x * 1.1, values)                      #returns the 'map': <map object at 0x000001B26ACDAEE0>
bonus = list(map(lambda x: x * 1.1, values))                 #returns the list of the map above: [257.40000000000003, 610.5, 741.4000000000001, 85.80000000000001]

print(bonus)

print("-------------------------")

print("**** ALTERNATIVE METHOD: the exercise above can be RE-WRITTEN to 2nd method w. FOR LOOP. e.g.: ****")
list = []

for i in values:
    list.append(i*1.1)
print(list)