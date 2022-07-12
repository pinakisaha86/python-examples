weekdays = ["Mon", "Tue", "Wed", "Thus", "Fri"]
weekends = ["Sat", "Sun"]
days = weekdays + weekends

day_indices = [1, 2, 3, 4, 5, 6, 7]
zipped = zip(days, day_indices)

#print("zip days and day indices: ", list(zipped))

#day_indices.append(10)

print("output", day_indices)


# Creating an empty dictionary:
dict_sample = {}

# Creating a dictionary with mixed keys:
dict_sample = {'fruit': 'mango', 1: [4, 6, 8]}
print("Output:", dict_sample)
# Create a dictionary by explicitly calling the Python's dict() method:
dict_sample = dict({1: 'mango', 2: 'pawpaw'})
print("Output:", dict_sample)
# created from a sequence as shown below:
dict_sample = dict([(1, 'mango'), (2, 'pawpaw')])
print("Output:", dict_sample)
# Dictionaries can also be nested, which means that we can create a dictionary inside another dictionary.
# For example:
dict_sample = {1: {'student1': 'Nicholas', 'student2': 'John', 'student3': 'Mercy'},
               2: {'course1': 'Computer Science', 'course2': 'Mathematics', 'course3': 'Accounting'}}
print("Output:", dict_sample)