from statistics import mean
# conditions:
# 1
number1: float = float(input("enter first number:"))
number2: float = float(input("enter second number:"))
smaller: float = number1 if number1 < number2 else number2
for _ in range(3):
    print(smaller)

# 2:
number1: int = int(input("enter first number:"))
number2: int = int(input("enter second number:"))
print("avg:", (number1 + number2) / 2)

# 3:
number1: int = int(input("enter first number:"))
number2: int = int(input("enter second number:"))
number3: int = int(input("enter third number:"))
bigger: int = 0
if number1 > number2 and number1 > number3:
    bigger = number1
elif number2 > number3:
    bigger = number2
else:
    bigger = number3
print(f"the bigger of the 3 numbers: {number1}, {number2}, {number3} is: {bigger}")

# 4
movie_len = int(input("enter movie length:"))
print(f"{movie_len // 60} hours {"" if movie_len % 60 == 0 else f"and {movie_len % 60} minutes"}")

# 5
number_4_digits: int = int(input("enter 4 digits number:"))
print("Rightmost digit is:", number_4_digits % 10)

# 6:
number_4_digits: int = int(input("enter 4 digits number:"))
print("The second digit from the right:", number_4_digits % 100 // 10)

# 7:
while True:
    number_2_digits: int = int(input("enter 2 digits number:"))
    if not 0 < number_2_digits < 99:
        print("try again")
        continue;
print(f"sum of the number {number_2_digits} is: {number_2_digits // 10 + number_2_digits % 10}")

# 8:
while True:
    number_2_digits: int = int(input("enter 2 digits number:"))
    if not 0 < number_2_digits < 99:
        print("try again")
        continue
    break;
print(f"reverse number:{number_2_digits % 10 * 10 + number_2_digits // 10}")

# 9:
number: int = int(input("enter a number:"))
print(f"the number {number} is {"even" if number % 2 == 0 else "odd"}")

# 10:
salary = int(input("enter origin salary to pay (bigger than 0):"))
tax: float = 0
origin = salary
while True:
    if origin < 6_000:
        tax = 0
        break
    else:
        salary -= 6_000
    if origin > 12_000:
        tax += 6_000 * 0.1
        salary -= 6_000
    else:
        tax += salary * 0.1
        break
    if origin > 18_000:
        tax += 6_000 * 0.2
        salary -= 6_000
    else:
        tax += salary * 0.2
        break
    if origin > 25_000:
        tax += 7_000 * 0.3
        salary -= 7_000
    else:
        tax += salary * 0.3
        break
    if origin > 35_000:
        tax += 10_000 * 0.4
        salary -= 10_000
    else:
        tax += salary * 0.4
        break
    if origin > 50_000:
        tax += 15_000 * 0.45
        salary -= 15_000
    else:
        tax += salary * 0.45
        break
    if origin > 50_000:
        tax += salary * 0.51
        break
print(f" Total tax for your {origin} are : {tax}")

# 11:
is_allow = False
age: int = int(input("enter age:"))
height: int = int(input("enter height:"))
if 8 <= age <= 18 and height >= 115:
    is_allow = True
elif age > 18 and height > 100:
    is_allow = True
print(f"you are {"allow" if is_allow else "not allow"} to get on the roller coaster")

# loops:
# 1
while True:
    top: int = int(input("enter a natural number"))
    if top < 0:
        print("try again")
        continue
    break
for i in range(top):
    print(i, " ")
print()

# 2
number1: int = int(input("enter first number"))
number2: int = int(input("enter second number"))
if number1 > number2:
    for i in range(number2, number1):
        print(i, end="")
else:
    for i in range(number1, number2):
        print(i, end="")
print()

# 3:
n = int(input("enter number:"))
if n % 2 == 1:
    n += 1
for i in range(0,n+2, 2):
    print(i,end=" ")
print()

# 4
max_num: int = int(input("enter max number number"))
den: int = int(input("enter divider number"))
print("the dividable numbers are: ")
for i in range(0,max_num+1):
    if i % den == 0:
        print(i, end=" ")
print()

# data analysis:
# 1
SENTINEL: int = -99
my_sum: int = None
while True:
    number = int(input("enter a number:"))
    if number == SENTINEL:
        break;
    if my_sum is None:
        my_sum = 0
    my_sum += number

print(f"my_sum:{my_sum}")

# 2:
max_num: int = None
min_num: int = None
while True:
    num = int(input("enter a number:"))
    if num <= 0 or num == SENTINEL:
        break;
    if max_num is None or max_num < num:
        max_num = num
    if min_num is None or min_num > num:
        min_num = num
print("max:", max_num)
print("min:", min_num)

# 3
max_num: int = None
max_index: int = 0
for i in range(5):
    num: int = int(input("enter a number:"))
    if max_num is None or max_num < num:
        max_num = num
        max_index = i
print(f"the max number is {max_num} in index:{max_index + 1}")

# 4:
number1: int = int(input("enter a number:"))
number2: int = int(input("enter multiple number:"))
result = 0
for _ in range(number2):
    result += number1
print("the result is:", result)

# 5:
number1: int = int(input("enter a number:"))
number2: int = int(input("enter power number:"))
result = 1
for _ in range(number2):
    result *= number1
print("the result is:", result)

# 6:
number: int = int(input("enter number:"))
digit: int = int(input("enter digit:"))

while number > 0:
    if number % 10 == digit:
        print(True)
        break
    number //= 10
else:
    print(False)

# 7:
number1: int = int(input("enter first number:"))
number2: int = int(input("enter second number:"))
smaller:int = number1 if number1 < number2 else number2
for i in range(smaller, 1, -1):
    if number1 % i == 0 and number2 % i == 0:
        print("gsd:",i)
        break

# 8:
is_prime: bool = True
x: int = int(input("enter a number:"))
if x == 2:
    print("prime")
    is_prime = True
elif x % 2 == 0:
    is_prime = False

divider: int = 3
while divider <= (x ** 0.5 + 1):
    if x % divider == 0:
        is_prime = False
        break
    divider += 2;

print(f" the number {x} is {"prime" if is_prime else "not prime"}")

# complex loops:
#1
temperature: float = -1
total: int = 12
list_temp: list[float] = []
while len(list_temp) < total:
    try:
        temperature = float(input("enter temperature:"))
        if temperature < -5 or temperature > 40:# if invalid data , stop and print only!
            print("wrong data")
            break
        print("correct data")
        if not temperature and( list_temp and not list_temp[len(list_temp) - 1]):
            continue
        list_temp.append(temperature)
    except ValueError:
        print("ERROR: invalid number")
    except Exception as e:
        print("ERROR:", e)
else:
    if list_temp:
        print("avg:", mean(list_temp))
        print("max:", max(list_temp))
        print("min:", min(list_temp))

# 2
count_list: list[int] = [0] * 3
required_count: int = 44
country_index: int = 1
VETO_NUMBER: int = 4
IN_FAVOR_NUMBER: int = 1
AGAINST_NUMBER: int = 2
options: list[str] = ["in favor", "against", "avoided"]
in_favor_index: int = None
against_index: int = None
while country_index <= required_count:
    try:
        vote: int = int(input("enter your vote number:"))
        if not IN_FAVOR_NUMBER <= vote <= VETO_NUMBER:
            continue
        if vote == VETO_NUMBER:
            print(f"the country with the index {country_index} voted 'veto'")
            break;
        if vote == IN_FAVOR_NUMBER:
            if in_favor_index is None:
                in_favor_index = country_index
        elif vote == AGAINST_NUMBER:
            if against_index is None:
                against_index = country_index
        country_index += 1
        count_list[vote - 1] += 1
    except ValueError:
        print("in valid vote")
else:
    for i in range(len(count_list)):
        print(f"total count of '{options[i]}' is:", count_list[i])
    if against_index is not None:
        print(" the first country that voted 'against' was in index of :", against_index)
    if in_favor_index is not None:
        print(" the first country that voted 'in favor' was in index of :", in_favor_index)
