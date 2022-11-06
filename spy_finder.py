"""Script for found the spy. We have q-ty of suspects and array/nested list of information
-> example [1,2] means that suspect 1 has information that 2 is spy. And in this case 2 is spy.
If we have information [[1,2],[2,3]] than there no any suspects which falls under requirements."""

suspects = int(input("Input number of suspects: "))

# Inputting array/nested list "has_information" of information about spy
stu = []
has_information = []
if suspects == 2:
    count = 1
else:
    count = (suspects // 2 + 1)
for i in range(0, count):
    stu.append(input())
    stu.append(input())
    has_information.append(stu)
    stu = []

print(f"You have {suspects} suspects.")
print(f"The array of information is next: {has_information}\n")

# Crates from array of information simple list for next seeking through it
list_for_information = []
for element in has_information:
    list_for_information.append(element[0])
    list_for_information.append(element[1])

# Founding the spy. Main point - to check if about spy was only one 'information' and if suspect which says about
# spy hasn't any mentions himself from other suspects.
spy = 0
count = 0
for elem in list_for_information[1:]:
    checker_id = list_for_information.index(elem) - 1
    if elem != list_for_information[0] and list_for_information.count(elem) == 1 and list_for_information.count(list_for_information[checker_id]) == 1:
        spy = elem
        count += 1
    else:
        spy = 0

if count == 0:
    print('No suspects which meet spy requirements.')
else:
    print(f"The spy is {spy}")

