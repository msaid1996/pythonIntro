print("------------------------------------------- 1: SIMPLE STRUCTURE  ------------------------------------------")

try:
    file = open("pretend_order.txt")                                         # function to open any EXISTING FILE

except:                                                                      # remove the red error in 'run command'
    print("The file you requested, there has been an error!")


print("------------------------------------------- 2: NAME SPECIFIC ERROR in except------------------------------------------")
try:
    file = open("pretend_order.txt")

except FileNotFoundError:                                                     # name the error
    print("The file you requested, there has been an error!")



print("----------------------------------- 3: NAME SPECIFIC ERROR + 'as' in except  ------------------------------------------")
try:
    file = open("pretend_order.txt")

except FileNotFoundError as errmessage:                                       # as ...
    print("The file you requested, there has been an error!")
    print(errmessage)                                                         # prints MORE INFO of the error
    #raise                                                                     # raise the error back in run command


print("--------------------------- 3: METHOD1: try/error w. DEF FUNCTION: read line, close file  ------------------------------------------")

def open_and_print_file(file):
    try:
        opened_file = open(file,"r")                                # OPEN & READ the 'file' & "r" = read the text LINE BY LINE
        file_line_list = opened_file.readlines()                    # read the lines

        for line in file_line_list:
            print(line.rstrip('\n'))                                #removes empty line in the file

        opened_file.close()                                         #CLOSE the file

    except FileNotFoundError:
        print("File can't be found, please check the details provided")
        raise                                                       # returns the red error in run comman


#call the function
open_and_print_file("pretend.txt")


print("--------------------------- 4: METHOD2: same as above but includes WITH open() AS variablename  -----------------------------------")

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


print("--------------------------- 5. ADD 'FINALLY: ' @ end of try/except  -----------------------------------")

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
    finally:
        print("execution complete")


#call the function
open_and_print_file("pretend.txt")