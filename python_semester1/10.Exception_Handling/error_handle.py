# In this we will learn about error handling

# The 3 main are: try, except, finally

u_input = input("Please enter a number: ")

try:
    result = 1/int(u_input)
except ZeroDivisionError as error: # error is a variable( you can name it something else as long as it make sense)
    print("Cannot man") # if you enter 0 you will get this result

except ValueError:
    print("Cannot do that too")

except TypeError:
    print(TypeError())

# These are the type of errors
# 1. ZeroDivisionError (when devide by 0)
# 2. ValueError (when converting string(abc) to int)
# 3. TypeError (when calculating with string)