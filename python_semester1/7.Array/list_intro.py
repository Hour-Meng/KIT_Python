#List datatype 
#ប្រភេទ Datatype List

#នៅក្នុងPython Programming, គេប្រើList សម្រាប់រក្សាទុក ទិន្នន័យចំនួនច្រើន ក្នុងឈ្មោះអរថេរតែមួយ។ (Array)
""" In python, programming, we use List to store a collection of data under a single varibale name."""

#ឧបមាថា យើងមានទិន្មន័យឈ្មោះ #ផ្លែឈើ ជាច្រើន យើងច្បាស់ជាត្រូវបង្កើតអរថេរមួយៗ ដូចខាងក្រោម:
"""Let's say, we have "Fruits" data, for sure we need to create an Array to store every Fruit items"""
fruit1 = "apple"
fruit2 = "banana"
fruit3 = "cherry"
fruit4 = 'durian'

#វិធីល្អជាងនឹងបើយើងប្រើList
''' Better and More Efficient '''

#LIST data type
fruit_list = ["apple", "banana", "cherry"]
print(fruit_list[-1])


""""List has builtin functions to Create and manipulate data"""
#គេប្រើList សម្រាប់ Read, Update(Insert new Data, Update Existing Data), and Delete
# មានសកម្មភាព CRUD លើទិន្នន័យ:
'''
CREATE -បង្កើត
READ -ទាញមកប្រើ
UPDATE - កែប្រែ /បន្ថែម
DELETE -លុប data.
'''

'''
CREATE -បង្កើត

'''
#Create a List to store a group of Fruit

fruit_list = ["apple", "banana", "cherry", "durian", "mango"]


'''
READ -ទាញមកប្រើ
'''
# ការទាញយកទិន្នន័យក្នុងList - Accessing List Items
# print(fruits[4])

#To Read the Last Item in List


'''
UPDATE​ - ​កែប្រែ /បន្ថែម
'''
#ការដាក់បញ្ចូល នូវទិន្នន័យបន្ថែមចូលទៅក្នុងList - Add Items into List
# print(fruits) #Before


#ការកែតម្លៃណាមួយក្នុង​List: Edit List Item
#Update(Update Existing Data)


[] #Empty List
'''
DELETE​ -លុប
'''
#Delete:ការលុបទិន្នន័យចេញពីList - Rmove Items from List
#To clear entire List's items


#To remove List's items based on its Index/Address/N.O


#To remove specific item's name



'''
ប្រតិបត្តិការណ៍ ផ្សេងទៀត!
'''
#ការស្វែងរក ក្នុងList -- List Search


#How to Unpacks the Item in List -- ការទាញយកទិន្នន័យក្នុងList ម្តងមួយៗ


#Using for loop

# Crud operations


# more info --

new_list = ["apple", "banana", "cherry", "durian", "mango"]
user_input = input("Please enter the fruit name: ")

"""if user_input.lower() in new_list:
    print(f" Yes bro the {user_input} is in the list")
else:
    print(f"NO bro {user_input} is not in the list")"""

print(user_input if user_input.lower() in new_list else "Not Found")