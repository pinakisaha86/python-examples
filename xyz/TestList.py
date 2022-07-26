weekdays=["Mon","Tue","Wed", "Thu", "Fri"]
weekends= ["Sat", "Sun"]

days = weekdays + weekends

#print("days:", days)

#print("days + weekends:", weekdays+ weekends)

#print("days +weekends:", weekdays.__add__(weekends))

day_indices = [1, 2, 3, 4, 5, 6, 7]
zipped = zip(days, day_indices)
print("zip days and day indices: ", list(zipped))
print("weekdays head:", weekdays[-1])
print("Weekdays contains 'Tue':", "Tue" in weekdays)
print("Weekdays contains 'Mon'", weekdays.__contains__("Mon"))
print("Weekdays contains from 1stindex to 3rd index:", weekdays[1:4])
print("Weekdays size of:", weekdays.__sizeof__(), bytes)
print("No of days:", len(weekdays))

weekdays.reverse()
print("Weekdays of reverse:", weekdays)

print('Index of element \'Wed\':', weekdays.index("Wed"))
print(' ~ '.join(day for day in days))

numbers=[]

for i in range(10):
    numbers.append(7)
    print(numbers)


count = 0
my_string = "aabbbcabc"
my_char = "r"

for i in my_string:
    if i == my_char:
        count += 1

print(count)
print("__________________counter for taking count of string____________________")
from collections import Counter
a_string = 'aabbbcabc'
collection = Counter(a_string)
print(collection)

print("__________________print any number____________________")
x =input("enter the number:")
x= int(x)
count=0
while x>0:
    x = x // 10
count=count+1
print(count)

print("__________________counter for taking count of string____________________")

# output = {}
# for ch in input:["aabbbcabc"]
# output[ch] = output.get(ch, 0) + 1
# print(output)
