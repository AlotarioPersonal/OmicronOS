#-----IMPORTS
import time
import os
import ctypes
import math

#-----FUNCTIONS
def clear():
	if os.name == "posix":
		os.system('clear')
	else:
		os.system('cls')

def write():
	#code for writing code to a python-generated text file called 'output.txt'
	clear()
	#Taken from https://anh.cs.luc.edu/handsonPythonTutorial/files.html
	namethefile = input("Enter a file name: ")
	filenamed = "files/" + namethefile + ".txt"
	clear()
	outfile = open(filenamed, 'a')
	outfile.write(input("Enter your text here: "))
	outfile.close()
	print('text successfully written to' + str(filenamed))


def read():
	clear()
    #Taken from https://anh.cs.luc.edu/handsonPythonTutorial/files.html
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

def calc():
	#the worst calculator ever
	clear()
	try:
		x = int(input("enter a number: "))
		y = int(input("enter another number: "))
	except:
		print("That's not a number. try again.")
		time.sleep(1)
		calc()
	print("enter an operation number.")
	print ("addition (1), subtraction (2), multiplication (3), division(4)")
	oper = input("enter pick here: ")
	
	calculatoring(oper, x, y)


def checkid():
	clear()
	print("""
          
 _______  __   __  ___   _______  ______    _______  __    _ 
|       ||  |_|  ||   | |       ||    _ |  |       ||  |  | |
|   _   ||       ||   | |       ||   | ||  |   _   ||   |_| |
|  | |  ||       ||   | |       ||   |_| \ |  | |  ||       |
|  |_|  ||       ||   | |      _||    __  ||  |_|  ||  _    |
|       || ||_|| ||   | |     |_ |   |  | ||       || | |   |
|_______||_|   |_||___| |_______||___|  |_||_______||_|  |__|
          

          """)
	#numeric id check the program runs on startup
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
	#where the main filesystem browser goes. holds the executions for all the programs
	clear()
	print("""
          
 _______  __   __  ___   _______  ______    _______  __    _ 
|       ||  |_|  ||   | |       ||    _ |  |       ||  |  | |
|   _   ||       ||   | |       ||   | ||  |   _   ||   |_| |
|  | |  ||       ||   | |       ||   |_||_ |  | |  ||       |
|  |_|  ||       ||   | |      _||    __  ||  |_|  ||  _    |
|       || ||_|| ||   | |     |_ |   |  | ||       || | |   |
|_______||_|   |_||___| |_______||___|  |_||_______||_|  |__|
          

          """)
	print("""      
calc - Runs basic calculator with addition, subtraction, multiplication and division.
tencheck - Runs basic check for if a number is over ten, good for checking language version validity
write - Write to a new or existing text file.
read - Read from an existing text file.
logout - Log out of the current user profile
shutdown - Shut down the machine.
       """)
	command = input("OMI:>  ")
	#MAKE ABSOLUTE SURE THAT THE = are DOUBLED, like this: ==. otherwise it won't work
	if command == "calc":
		calc()
		clear()
		runprogram()
	elif command == "tencheck":
		tencheck()
		time.sleep(3)
		#'mememememe why dont you just put the time.sleep in the function itself' i will find your house
		runprogram()
	elif command == "write":
		write()
		time.sleep(2.5)
		runprogram()
	elif command == "read":
		read()
		runprogram()
	elif command == "shutdown":
		print("Closing Dobel Filesystem...")
		time.sleep(1)
		print("Shutting Down...")
		time.sleep(0.5)
		quit()
	elif command == "logout":
		print('Logging Out...')
		time.sleep(1)
		clear()
		print("""
          
 _______  __   __  ___   _______  ______    _______  __    _ 
|       ||  |_|  ||   | |       ||    _ |  |       ||  |  | |
|   _   ||       ||   | |       ||   | ||  |   _   ||   |_| |
|  | |  ||       ||   | |       ||   |_||_ |  | |  ||       |
|  |_|  ||       ||   | |      _||    __  ||  |_|  ||  _    |
|       || ||_|| ||   | |     |_ |   |  | ||       || | |   |
|_______||_|   |_||___| |_______||___|  |_||_______||_|  |__|
          

          """)
		checkid()
	else:
		print("Invalid Program Name.")
		time.sleep(1)
		runprogram()
		
def loadasset():
	#flashy loading screen
	clear()
	print("""
          
 _______  __   __  ___   _______  ______    _______  __    _ 
|       ||  |_|  ||   | |       ||    _ |  |       ||  |  | |
|   _   ||       ||   | |       ||   | ||  |   _   ||   |_| |
|  | |  ||       ||   | |       ||   |_||_ |  | |  ||       |
|  |_|  ||       ||   | |      _||    __  ||  |_|  ||  _    |
|       || ||_|| ||   | |     |_ |   |  | ||       || | |   |
|_______||_|   |_||___| |_______||___|  |_||_______||_|  |__|
          

          """)
	print("Welcome to OMICRON")
	time.sleep(2)
	print("Loading Assets...")
	time.sleep(1)
	var = 0
	while var < 101:
		print("""
          
 _______  __   __  ___   _______  ______    _______  __    _ 
|       ||  |_|  ||   | |       ||    _ |  |       ||  |  | |
|   _   ||       ||   | |       ||   | ||  |   _   ||   |_| |
|  | |  ||       ||   | |       ||   |_||_ |  | |  ||       |
|  |_|  ||       ||   | |      _||    __  ||  |_|  ||  _    |
|       || ||_|| ||   | |     |_ |   |  | ||       || | |   |
|_______||_|   |_||___| |_______||___|  |_||_______||_|  |__|
          

          """)
		print(str(var) + "% Loaded")
		time.sleep(0.05)
		var += 1
		clear()
	#i have to give some sort of visual fun to my eyeballs, python is already slow as balls let me have some fun
	print("""
          
 _______  __   __  ___   _______  ______    _______  __    _ 
|       ||  |_|  ||   | |       ||    _ |  |       ||  |  | |
|   _   ||       ||   | |       ||   | ||  |   _   ||   |_| |
|  | |  ||       ||   | |       ||   |_||_ |  | |  ||       |
|  |_|  ||       ||   | |      _||    __  ||  |_|  ||  _    |
|       || ||_|| ||   | |     |_ |   |  | ||       || | |   |
|_______||_|   |_||___| |_______||___|  |_||_______||_|  |__|
          

          """)
	print("Assets Loaded.")
	#i want a fullscreen function here someone figure that out please
	time.sleep(1)
	
def tencheck():
#joke code for checking if a number is over, under, or exactly 10
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
#don't run any other functions here