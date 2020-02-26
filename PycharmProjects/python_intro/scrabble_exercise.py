ask = input("what is your word?  ")

point = ["a","e","i","o","u","L", "n","r", "s", "t"]
dgpoint= ["d", "g"]
bcpoint = ["b", "c", "m", "p"]
fhpoint = ["f", "h", "v", "w", "y"]
kpoint = ["k"]
jpoint = ["j", "x"]
qpoint = ["q", "z"]

count = 0
for i in ask:
    if i in point:
        count += 1
    if i in dgpoint:
        count += 2
    if i in bcpoint:
        count += 3
    if i in fhpoint:
        count += 4
    if i in kpoint:
        count += 5
    if i in jpoint:
        count += 8
    if i in qpoint:
        count += 10
print(count)

