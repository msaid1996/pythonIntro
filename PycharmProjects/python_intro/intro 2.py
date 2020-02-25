#------------------------------------------LISTS []
shopping_list = ["nutella", "oranges", "mickie's of scotland", "tofu", "bourbon biscuits", "oranges"]

#replace 1st item [0]
print(shopping_list)
shopping_list[0]='bigger nuttella'

print(shopping_list)    #update the item position 0

#add new item to list
shopping_list.append("carrots")
print(shopping_list)    #update list

#length of list - counts the items in the list
print(len(shopping_list))

print("-----------------remove")
#remove()
new_list = ["nutella", "oranges", "mickie's of scotland", "tofu", "bourbon biscuits", "oranges"]
print(new_list.remove("oranges"))         #1st item of object to be removed from the list
print(new_list)

print("-----------------pop")
#pop()
a_list = ["nutella", "oranges", "mickie's of scotland", "tofu", "bourbon biscuits", "oranges"]
print(a_list.pop(2))        #removes position 2 item
print(a_list)               #updates new list w/o above

print('-----------')
new_shopping_list = ["nutella", "oranges", "mickie's of scotland", "tofu", "bourbon biscuits", "oranges",
                     56, 45.3, "one", "5"]
print(new_shopping_list)

#------------------------------------------TUPLES ()
#similar to list - but items in list x be modified

print('------------------------------------------------------------')

newlist = ["nutella", "oranges", "mickie's of scotland", "tofu", "bourbon biscuits", "oranges",
                     56, 45.3, "one", "5"]          #list
essentials = ("milk", "biscuit", "tea", "milk")             #touple

print(essentials.count("milk"))


