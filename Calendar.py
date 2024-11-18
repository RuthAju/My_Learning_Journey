import calendar

print("The calendar of a year")
year = int(input("Enter year: "))

print(calendar.calendar(year))


print ("A month in a year")
year = int(input("Enter year: "))

month_input = input("Enter the month of the year: ")
while True:
    if month_input.isdigit():
        month = (int(month_input))
        break

    else:
        month = list(calendar.month_name).index(month_input.capitalize())
        break

print(calendar.month(year, month))

print("Range of months in a year")

year = int(input("Enter year: "))

print("Enter your desired month range ... ")

From = input("From: ")
while True:   
    if From.isdigit():
        _from = (int(From))
        print("Proceeding...")
        break

    else:
        _from = list(calendar.month_name).index(From.capitalize())
        print("Proceeding...")
        break

To = input("To: ")
while True:  
    if To.isdigit():
        _to = (int(To))
        print("Proceeding...")
        break

    else:
        _to = list(calendar.month_name).index(To.capitalize())
        print("Proceeding...")
        break
    
_to += 1

Myrange = range(_from, _to)

# Create an empty list to append the month range
Mylist = []
for x in Myrange:
   Mylist.append(x)

for y in Mylist:
   print(calendar.month(year, y))



