my_list= [1,2,3,"hello","world"]


print("length",len(my_list))

print("index:", my_list[4])

print("output:", my_list.append('hero'))
print("final:", my_list)
#print("insert:", my_list.pop())
#print("input:", my_list)

print("insert:", my_list.remove(1))
print("input:", my_list)
my_list.pop(2)
print("final:", my_list)



lst=[ 1, 6, 3, 5, 3, 4 ]
#checking if element 7 is present
# in the given list or not
i=5
# if element present then return
# exist otherwise not exist
if i in lst:
    print("exist")
else:
    print("not exist")

#########
print("Dictionary practise")

my_dic= {'key1':'Sam', 'key2':'Tom'}
print(my_dic)

print(my_dic['key2'])

price_dic ={'apple':40, 'mango':80}
print(price_dic['apple'])

price_dic.update({'Orange': 120})
print(price_dic)

print(my_dic['key2'].upper())

my_dic['key3']= 'ram'
print(my_dic)

print(my_dic.values())
print(my_dic.items())

print("Tuples practise")

print("exercise for print")
mystring ='aaabbbccabc'
mylist =[]
for letter in mystring:
    mylist.append(letter)
print(mylist)



work_hours =[('Piku',200), ('Pintu', 400), ('Chinku',100)]


def employee_check(work_hours):
    current_max = 0
    employee_of_the_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_the_month = employee
        else:
            pass

    return (employee_of_the_month, current_max)
result = employee_check(work_hours)
print("who is the hardest worker:", result)