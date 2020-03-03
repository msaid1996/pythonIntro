import mod1         #import the code from mod1.py
                    #mod1.py:
                        #code: print("this is mod1's name = " + __name__)
                        #returns: this is mod1's name = mod1
                        #where __name__ is where it's from.
                            # as its imported from mod1 --> __name__ =mod1

print("mod2's name is " + __name__)         #prints the __name__ = main [is now the main file in this py.file]