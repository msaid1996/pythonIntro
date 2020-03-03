# w
# x
# a
# t
# b
# +
print(" -------------------------- EX1:  r = READ file --------------------------")


def open_and_print_file(file):
    try:
        with open(file,"r") as opened_file:                                # OPEN & READ the 'file' & "r" = read the text LINE BY LINE
            file_line_list = opened_file.readlines()                    # read the lines

            for line in file_line_list:
                print(line.rstrip('\n'))                                #removes empty line in the file

            opened_file.close()                                         #CLOSE the file

    except FileNotFoundError:
        print("File can't be found, please check the details provided")
        raise                                                       # returns the red error in run comman


#call the function
open_and_print_file("pretend.txt")

print(" -------------------------- EX2:  w = write & edit new info in file --------------------------")
def open_and_print_file(file):
    try:
        with open(file,"w") as write_file:                                # OPEN & READ the 'file' & "r" = read the text LINE BY LINE

            #adds the words
            write_file.write("hello \n")
            write_file.write("This is our new write file text \n")
            write_file.write("Another line \n")
            write_file.write("And another line \n")

            write_file.close()                                         #CLOSE the file

    except FileNotFoundError:
        print("File can't be found, please check the details provided")
        #raise                                                       # returns the red error in run comman


#call the function
open_and_print_file("w_file_forFIleExercise.txt")


print(" -------------------------- EX3:  a = appending mode = add new data to the end of the file --------------------------")

def append_and_print_file(file):
    try:
        with open(file,"a") as append_file:                                # append mode = add new info to file

            #adds the words
            append_file.write("hello \n")
            append_file.write("This is our new APPEND MODE NEW INFO ADDED TO file text \n")
            append_file.write("Another APPEND NEW INFO line \n")
            append_file.write("And another line \n")

            #append_file.read()

            append_file.close()                                         #CLOSE the file


    except FileNotFoundError:
        print("File can't be found, please check the details provided")
        #raise                                                       # returns the red error in run comman


#call the function
append_and_print_file("append.txt")




print(" ------------------ EX4:  x = open for exclusive creation = CREATES NEW txt file --------------------------")

def  open_for_exclusive_creation(file):
    try:
        with open(file,"x") as open_exclusive:                                # creates new file
            print("fzfd")
            #adds the words
            open_exclusive.write("hello \n")
            open_exclusive.write("This is our new APPEND MODE NEW INFO ADDED TO file text \n")
            open_exclusive.write("Another APPEND NEW INFO line \n")
            open_exclusive.write("And another line \n")

            open_exclusive.close()                                         #CLOSE the file

    except FileNotFoundError:
        print("File can't be found, please check the details provided")
        #raise                                                       # returns the red error in run comman

#call the function
open_for_exclusive_creation("ss.txt")                                                   #create the new file

print(" ------------------ EX6:  b = rb - reading binary & wb - writing binary --------------------------")

def  binary_function(file):
    try:
        with open(file,"wb") as binaryFile:                                # creates new file
            num = [5,10,15,20,25]
            arr=bytearray(num)
            binaryFile.write(arr)
            binaryFile.close()                                         #CLOSE the file

    except FileNotFoundError:
        print("File can't be found, please check the details provided")
        #raise                                                       # returns the red error in run comman

#call the function
#binary_function("binaryEx.bin")

