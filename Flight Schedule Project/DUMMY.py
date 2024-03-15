import datetime
##
##def calc(b):
##    i = b
##    if i == 4:
##        pass
##    else:
##       print("NOPE")
##       return False
##
##    print("BAGNA")
##    
##b = int(input("Enter:"))
##
##calc(b)

x = datetime.time(20,30)
print(x)
# the "#" removes zero padding turning
# 08:30pm -> 8:30pm
#.lower() is to lower the AM/PM since I get an error using "%P"
y = x.strftime("%#I:%M%p").lower()
print(y)

a = datetime.timedelta(days = 1, hours = 00, minutes = 30)
p = datetime.timedelta(days = 0, hours = 20, minutes = 30)
time = a - p
time = ':'.join(str(time).split(':')[:2])
print(time)

next_day = input("enter:")

#print(next_day.upper())

if next_day.upper() == "Y":
    next_day = 1
    print(next_day)
elif next_day.upper() == "N":
    next_day = 0
    print(next_day)
else:
    print("NICE")


g = 25
b = 30
if not (0 <= g <= 30) and not (0 <= b <= 30):
    print("good")
else:
    print("bad")
