# In Python, you can do CRUD
# C - Create
# R - Read
# U - Update
# D - Delete


# The permissions are called Privileges

# ================================================================================================================= #
                                                # To Open the File
# open("file name.txt", "mode")

# r = read , a = append , w = write/overwrite, x = create

#Option 1
current = open("intro_to_file.py", "r") # This will read this current file
print(current.read())

#Option 2
with open("file_demo.txt", "r") as f: # The f is to assign it as variable f
    print(f.read())
# ================================================================================================================= #
                                                # To Create the File
# There are 2 options:

#Option 1
# Write this into terminal
# code filename.txt

#Option 2
# Use mode x to create the file
# We can create the file and use what we learned called exception handling to avoid any error
# why used it? What if the user create a file that got the same name? or they run the code multiple time
try:
    with open("created_demo_file.txt", "x"):
        print("The file as been created successfully")
except FileExistsError:
    print(f"The file already exists {FileExistsError}")

# ================================================================================================================= #
                                                # To Read the File
with open("created_demo_file.txt", "r") as f: # The f is to assign it as variable f
    print(f.read())

# ================================================================================================================= #
                                                # To Write/Update the File

# There are 2 types of write ( "a" - append, "w" - overwrite the file )

# First create a new file called it whatever you want
# I will paste lorem text into that file ( I called it lorem.txt )
with open("lorem.txt", "w") as f:
    f.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. In elit sapien, consectetur ut placerat nec, imperdiet vitae nulla. "
            "\nSed aliquet ante eget nisi iaculis, quis fermentum ligula rutrum. Duis ut nibh nunc. "
            "\nEtiam sit amet tincidunt augue, quis consectetur lectus. Aenean vitae tristique erat. Quisque aliquet nunc id lectus ullamcorper.")

# With this mode it will overwrite your file, for example:
# If file a text is ("Hello World" ) and you write "Hi"
# If you check your .txt file again, that Hello World will be gone and replaced by Hi instead

with open("lorem.txt", "a") as f:
    f.write("\n"
            "\nThis is append")

# ================================================================================================================= #
                                                # To Delete the File

# Do delete the file with python you will need to import os first
import os
#it's good to use exception handling again
try:
    os.remove("created_demo_file.txt")
    print("The file has been removed")
except FileNotFoundError:
    print("The file does not exist", FileExistsError)

