#__name__
#__main__

print("this is mod1's name = " + __name__)     #gives you the name of the file being run
                                               # as it's original file, __name__ = __main__

if __name__ == "__main__":
    print("only available on mod1")