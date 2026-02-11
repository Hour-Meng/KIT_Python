#ប្រភេទ Datatype: Tuple

#នៅក្នុងPython Programming, គេប្រើTuple សម្រាប់រក្សាទុក ទិន្នន័យចំនួនច្រើន ក្នុងឈ្មោះអរថេរតែមួយ។
""" In python, programming, we use TUPLE to store a collection of data under a single varibale name."""


#Tuple ស្រដៀងទៅនឹងList ដែរ មិនអាចធ្វើការ បន្ថែម(Update) កែប្រែ(Edit) ឬលុប(Delete) នូវទិន្នន័យបាននោះទេ។
"""Tuple is similar to List Data Type, but we cannot Update, Edit and Delete data."""

#គេប្រើTuple គឺពេលណាដែល យើងច្បាស់ថាទិន្នន័យទាំងនោះ នឹងមិនមានការកែប្រែនាពេលអនាគត។
"""We use Tuple when we are sure that the Data is not going to Update or Edit in the future."""

#គេប្រើTuple សម្រាប់ Readទិន្នន័យ ប៉ុណ្ណោះ!
"""We use Tuple as the Data type for Read/View only."""

#ឧទាហរណ៍១: យើងមាន Tuple ថ្ងៃទាំងអស់ ក្នុងសប្តាហ៏។
"""Example 1: Day of the Week"""
days = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")

for a, b in enumerate(days):
    print(f"{a + 1}:{b} ")

#ឧទាហរណ៍២: យើងមាន Tuple បង្ហាញទិន្នន័យរបស់ ភ្លើងសញាណចរាចរណ៏។
"""Example 2: Traffic Light Signal"""
traffic_light = ("RED", "YELLOW", "GREEN")

#TUPLE is READ only

'''
READ -ទាញមកប្រើ
'''
#ការទាញយកទិន្នន័យក្នុងTuple - Accessing Tuple Items using Address/N.o/Index

#Read/Accessing last item in Tuple


'''
ប្រតិបត្តិការណ៍ ផ្សេងទៀត!
'''
#ការស្វែងរក ក្នុងList -- List Search

#How to Unpacks the Item in List -- ការទាញយកទិន្នន័យក្នុងList ម្តងមួយៗ