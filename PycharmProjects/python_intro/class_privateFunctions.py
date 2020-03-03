class Example:
    statement = "Found here"

#assign
x=Example()
#print
print(x.statement)

##change the inner code
print("*****change inner code*****")
x.statement = "Change the inner code"
print(x.statement)



########

print("**************2: with method function***********")
class Example:
    statement = "Found here"

    def set_access(self, value):
        self.statement = value
        return self.statement
#assign
x=Example()

#print out
print(x.statement)
x.set_access("new changes")
print(x.statement)

########

print("**************3: with method function w PRIVATE __ ***********")
class Example:
    __statement = "Found here"

    def set_access(self, value):
        self._statement = value
        return self._statement
#assign
x=Example()

#print out
print(x.__statement)                #IT'S PRIVATE --- cannot be seen (has ATTRIBUTE ERROR)
x._set_access("new changes")
print(x.__statement)


