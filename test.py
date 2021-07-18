numbers = int(input ())
number_list = list(map(int,input().split()[:numbers]))

for number in number_list:
    if(number == number_list[0]):
        max_number = number
        min_number = number
        continue
    if(max_number <= number):
        max_number = number
    if(min_number >= number):
        min_number = number

print("%d %d" % (min_number, max_number))