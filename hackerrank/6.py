literal_low = []
literal_high = []
number_odd = []
number_even = []
number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

string_user = input()
for let in string_user:
    if let in number_list:
        if int(let) % 2 != 0:
            number_odd.append(let)
        if int(let) % 2 == 0:
            number_even.append(let)
    else:
        if let == let.lower():
            literal_low.append(let)
        else:
            literal_high.append(let)

literal_low.sort()
literal_high.sort()
number_odd.sort()
number_even.sort()

sorted_list = literal_low + literal_high + number_odd + number_even
result = ''.join(sorted_list)
print(result)

