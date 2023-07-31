#FILE HANDLING IN PYTHON
  #python handles files as texts or binary
  #Each line of a file is terminated with a special character, called the EOL or End of Line 
  #characters like comma {,} or newline character.
  #Opening a file
  #f= open(filename,mode)
#python offers an inbuilt function to open existing files the open function
#takes two parameters the filename and the mode in which the file should be opened
#"r" ->read only,"w" ->write only n overides existing information ,"a"-> appends info to the file
f=open("today.txt","a")
# for x in f:
#     print(x)
# read_file=f.read(3) 
append=f.write("hey")
print(read_file)  
new_file=open("new.txt","w")
new_file.write("hey I am new")

#EXCEPTION HANDLING IN PYTHON

# In Python, exception handling is a mechanism to handle errors or exceptional situations that may occur during program execution.
# It allows you to catch and handle specific exceptions gracefully, preventing the program from crashing.

# The basic structure of exception handling in Python involves the following keywords:

# try:
#     The code block placed inside the 'try' block is the one where an exception might occur.
#     It is the section of code where you anticipate potential errors.

# except ExceptionType:
#     If an exception of type 'ExceptionType' occurs inside the 'try' block, the corresponding 'except' block is executed.
#     'ExceptionType' represents the specific type of exception that you want to handle.
#     You can catch and handle specific exceptions, such as ValueError, TypeError, or FileNotFoundError, or use a more general 'except' block to handle any exception.

# except ExceptionType as error:
#     You can assign the exception instance to a variable 'error' using the 'as' keyword.
#     This allows you to access the details of the exception and handle it accordingly.

# else:
#     The 'else' block is optional and executed if no exceptions occur in the 'try' block.
#     It contains code that should run only if the 'try' block does not raise any exceptions.

# finally:
#     The 'finally' block is optional and always executed, regardless of whether an exception occurred or not.
#     It is useful for performing cleanup tasks or releasing resources that should be done regardless of the outcome of the exception handling.


try:
    # Code that may raise an exception
    x = int(input("Enter a number: "))
    result = 10 / x
    print("Result:", result)

except ZeroDivisionError:
    # Handling a specific exception (division by zero)
    print("Cannot divide by zero")

except ValueError as error:
    # Handling a specific exception (invalid input)
    print("Invalid input:", str(error))

except Exception as error:
    # Handling any other exception
    print("An error occurred:", str(error))

else:
    # Code executed if no exceptions occur
    print("No exceptions occurred")

finally:
    # Code always executed
    print("Finally block")



"""


# Try-except statement
num1 = 10
num2 = 0

try:
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero")
    
    

# List of phones
phones = ["iPhone", "Samsung", "Google Pixel", "OnePlus"]

try:
    
    index = int(input("Enter the index of the phone you want to access: "))


    selected_phone = phones[index]
    print("Selected phone:", selected_phone)

except IndexError:
    print("Invalid index! The list does not have an element at the specified index.")

except ValueError:
    print("Invalid input! Please enter a valid integer index.")

except Exception as error:
    print("An error occurred:", str(error))

finally:
    print("Exception handling completed.")   
