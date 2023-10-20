# -----IMPORTS
import time
import os
import subprocess

# -----FUNCTIONS


def clear():
    if os.name == "posix":
        os.system('clear')
    else:
        os.system('cls')


def write():
    # code for writing code to a python-generated text file called 'output.txt'
    clear()
    # Taken from https://anh.cs.luc.edu/handsonPythonTutorial/files.html
    namethefile = input("Enter a file name: ")
    filenamed = "files/" + namethefile + ".txt"
    clear()
    outfile = open(filenamed, 'a')
    lines = int(input("Enter the number of lines needed: "))
    for i in range(lines):
        outfile.write(input("Enter your text here: "))
        outfile.write("\n")
    outfile.close()
    print('text successfully written to' + str(filenamed))


def read():
    clear()
# Taken from https://anh.cs.luc.edu/handsonPythonTutorial/files.html
    textrequest = input("Enter the file name here: ")
    try:
        inFile = open("files/" + str(textrequest) + ".txt", 'r')
        clear()
    except:
        print("Path invalid. Try again.")
        read()

    clear()
    contents = inFile.read()
    print(contents)
    purposefulvariable = input("Enter to continue . . .")
    runprogram()


def calculatoring(oper, x, y):
    if oper == "1":
        z = x + y
        print("Answer: " + str(z))
        time.sleep(3)
        runprogram()

    elif oper == "2":
        z = x - y
        print("Answer: " + str(z))
        time.sleep(3)
        runprogram()

    elif oper == "3":
        z = x * y
        print("Answer: " + str(z))
        time.sleep(3)
        runprogram()

    elif oper == "4":
        z = x / y
        print("Answer: " + str(z))
        time.sleep(3)
        runprogram()
    else:
        print("That's an invalid operation!")
        time.sleep(1)
        calc()

def systemaccess():
    cmd = input("(" + os.name + ")cmd:")
    os.system(cmd)
    filler = input('Enter To Continue. . .')

def calc():
    # the worst calculator ever
    clear()
    try:
        x = int(input("enter a number: "))
        y = int(input("enter another number: "))
    except:
        print("That's not a number. try again.")
        time.sleep(1)
        calc()
    print("enter an operation number.")
    print("addition (1), subtraction (2), multiplication (3), division(4)")
    oper = input("enter pick here: ")

    calculatoring(oper, x, y)


def checkid():
    clear()
    print("""
 ██████╗ ███╗   ███╗██╗ ██████╗██████╗  ██████╗ ███╗   ██╗ ██████╗ ███████╗
██╔═══██╗████╗ ████║██║██╔════╝██╔══██╗██╔═══██╗████╗  ██║██╔═══██╗██╔════╝
██║   ██║██╔████╔██║██║██║     ██████╔╝██║   ██║██╔██╗ ██║██║   ██║███████╗
██║   ██║██║╚██╔╝██║██║██║     ██╔══██╗██║   ██║██║╚██╗██║██║   ██║╚════██║
╚██████╔╝██║ ╚═╝ ██║██║╚██████╗██║  ██║╚██████╔╝██║ ╚████║╚██████╔╝███████║
 ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
                                                                           
          """)
    # numeric id check the program runs on startup
    id = input("enter your six-digit numeric id: ")
    if id == "179141":
        print("id verified")
        print(" ")
        time.sleep(1)
        loadasset()
        runprogram()
    else:
        print("incorrect")
        time.sleep(1)
        clear()
        checkid()


def runprogram():
    # where the main filesystem browser goes. holds the executions for all the programs
    clear()
    print("""
 ██████╗ ███╗   ███╗██╗ ██████╗██████╗  ██████╗ ███╗   ██╗ ██████╗ ███████╗
██╔═══██╗████╗ ████║██║██╔════╝██╔══██╗██╔═══██╗████╗  ██║██╔═══██╗██╔════╝
██║   ██║██╔████╔██║██║██║     ██████╔╝██║   ██║██╔██╗ ██║██║   ██║███████╗
██║   ██║██║╚██╔╝██║██║██║     ██╔══██╗██║   ██║██║╚██╗██║██║   ██║╚════██║
╚██████╔╝██║ ╚═╝ ██║██║╚██████╗██║  ██║╚██████╔╝██║ ╚████║╚██████╔╝███████║
 ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
                                                                           
          """)
    print("""omicronOSv0.2.1
managed by L.Kaminski, 2023
 
Type 'help' for a list of commands.""")
    command = input("OMI:>  ")
    # MAKE ABSOLUTE SURE THAT THE = are DOUBLED, like this: ==. otherwise it won't work
    if command == "calc":
        calc()
        clear()
        runprogram()
    elif command == "help":
        print("""      
calc - Runs basic calculator with addition, subtraction, multiplication and division.
tencheck - Runs basic check for if a number is over ten, good for checking language version validity
write - Write to a new or existing text file.
read - Read from an existing text file.
omizone - Activate the omiZone, a 3D interactive space within omicronOS
sysacc - run a single system command on your operating system's default CMD.
logout - Log out of the current user profile
exit - Shut down the machine.
       """)
        moarfiller = input("Enter to Continue. . .")
        clear()
        runprogram()
    elif command == "sysacc":
        clear()
        systemaccess()
        clear()
        runprogram()
    elif command == "tencheck":
        tencheck()
        time.sleep(3)
        # 'mememememe why dont you just put the time.sleep in the function itself' i will find your house
        runprogram()
    elif command == "write":
        write()
        time.sleep(2.5)
        runprogram()
    elif command == "read":
        read()
        runprogram()
    elif command == "omizone":
        subprocess.run(["python", r"omizone.py"])
        clear()
        runprogram()
    elif command == "exit":
        clear()
        print("Closing OmicronOS Runtime. . .")
        time.sleep(0.2)
        print("Checking Save Validity. . .")
        time.sleep(1)
        print("Shutting Down...")
        time.sleep(0.5)
        quit()
    elif command == "logout":
        print('Logging Out...')
        time.sleep(1)
        clear()
        print("""
 ██████╗ ███╗   ███╗██╗ ██████╗██████╗  ██████╗ ███╗   ██╗ ██████╗ ███████╗
██╔═══██╗████╗ ████║██║██╔════╝██╔══██╗██╔═══██╗████╗  ██║██╔═══██╗██╔════╝
██║   ██║██╔████╔██║██║██║     ██████╔╝██║   ██║██╔██╗ ██║██║   ██║███████╗
██║   ██║██║╚██╔╝██║██║██║     ██╔══██╗██║   ██║██║╚██╗██║██║   ██║╚════██║
╚██████╔╝██║ ╚═╝ ██║██║╚██████╗██║  ██║╚██████╔╝██║ ╚████║╚██████╔╝███████║
 ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
                                                                           
          """)
        checkid()
    else:
        print("Invalid Program Name.")
        time.sleep(1)
        runprogram()




    



def loadasset():
    # flashy loading screen
    clear()
    print("""
 ██████╗ ███╗   ███╗██╗ ██████╗██████╗  ██████╗ ███╗   ██╗ ██████╗ ███████╗
██╔═══██╗████╗ ████║██║██╔════╝██╔══██╗██╔═══██╗████╗  ██║██╔═══██╗██╔════╝
██║   ██║██╔████╔██║██║██║     ██████╔╝██║   ██║██╔██╗ ██║██║   ██║███████╗
██║   ██║██║╚██╔╝██║██║██║     ██╔══██╗██║   ██║██║╚██╗██║██║   ██║╚════██║
╚██████╔╝██║ ╚═╝ ██║██║╚██████╗██║  ██║╚██████╔╝██║ ╚████║╚██████╔╝███████║
 ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
                                                                           
          """)
    print("Welcome to OMICRON")
    print("Loading Assets...")
    time.sleep(1)
    var = 0
    while var < 101:
        print(str(var) + "% Loaded \r"),
        time.sleep(0.01)
        var += 1
        clear()
    # i have to give some sort of visual fun to my eyeballs, python is already slow as balls let me have some fun
    print("""
 ██████╗ ███╗   ███╗██╗ ██████╗██████╗  ██████╗ ███╗   ██╗ ██████╗ ███████╗
██╔═══██╗████╗ ████║██║██╔════╝██╔══██╗██╔═══██╗████╗  ██║██╔═══██╗██╔════╝
██║   ██║██╔████╔██║██║██║     ██████╔╝██║   ██║██╔██╗ ██║██║   ██║███████╗
██║   ██║██║╚██╔╝██║██║██║     ██╔══██╗██║   ██║██║╚██╗██║██║   ██║╚════██║
╚██████╔╝██║ ╚═╝ ██║██║╚██████╗██║  ██║╚██████╔╝██║ ╚████║╚██████╔╝███████║
 ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
                                                                           
          """)
    print("Assets Loaded.")
    # i want a fullscreen function here someone figure that out please
    time.sleep(1)


def tencheck():
    # joke code for checking if a number is over, under, or exactly 10
    clear()
    try:
        x = int(input("Input a number: "))
    except:
        print("That's not a number!")
        time.sleep(1)
        tencheck()
    if x < 10:
        print("less than 10")
        time.sleep(1.5)
    elif x > 10:
        print("more than 10")
        time.sleep(1.5)
    elif x == 10:
        print("exactly 10")
        time.sleep(1.5)
    runprogram()
# don't run any other functions here

#VARIABLES