#SET - similar to dictionary - RANDOM ITEM ORDER EACH TIME

animals = {"dog", "honey badger", "guinea pig"}

print(animals)      #not in the same order as orginal - keeps changing the order

#ADD NEW ANIMALS
animals.add("goat")
print(animals)      #updated set

#REMOVE ANIMAL
animals.discard("dog")
print(animals)      #updated set


#------FROZEN SET : list within a touple(list x be modified)
# = prevent the random order of items each time you run

animals = frozenset(["dog", "honey badger", "guinea pig"])
print(animals)

