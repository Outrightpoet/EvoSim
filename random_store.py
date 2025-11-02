import random

zero_thousand = [random.randint(0, 1000) for _ in range(5000)]
zero_five_hundred = [random.randint(0, 500) for _ in range(5000)]
zero_hundred = [random.randint(0, 100) for _ in range(5000)]
zero_thirty = [random.randint(0, 30) for _ in range(5000)]
neg_one_one = [random.randint(-1, 1) for _ in range(5000)]
neg_two_two = [random.randint(-2, 2) for _ in range(5000)]
one_three = [random.randint(1, 3) for _ in range(5000)]
one_ten = [random.randint(1, 10) for _ in range(5000)]
neg_ten_ten = [random.randint(-10, 10) for _ in range(5000)]
zero_one = [random.randint(0, 1) for _ in range(5000)]

count = 0

def get_randint_zero_thousand():
    global count
    try:
        count += 1
        return zero_thousand[count]
    except IndexError:
        count = 0
        return zero_thousand[count]

def get_randint_zero_hundred():
    global count
    try:
        count += 1
        return zero_hundred[count]
    except IndexError:
        count = 0
        return zero_hundred[count]

def get_randint_zero_thirty():
    global count
    try:
        count += 1
        return zero_thirty[count]
    except IndexError:
        count = 0
        return zero_thirty[count]

def get_randint_neg_one_one():
    global count
    try:
        count += 1
        return neg_one_one[count]
    except IndexError:
        count = 0
        return neg_one_one[count]

def get_randint_neg_two_two():
    global count
    try:
        count += 1
        return neg_two_two[count]
    except IndexError:
        count = 0
        return neg_two_two[count]

def get_randint_one_three():
    global count
    try:
        count += 1
        return one_three[count]
    except IndexError:
        count = 0
        return one_three[count]

def get_randint_one_ten():
    global count
    try:
        count += 1
        return one_ten[count]
    except IndexError:
        count = 0
        return one_ten[count]

def get_randint_neg_ten_ten():
    global count
    try:
        count += 1
        return neg_ten_ten[count]
    except IndexError:
        count = 0
        return neg_ten_ten[count]

def get_randint_zero_one():
    global count
    try:
        count += 1
        return zero_one[count]
    except IndexError:
        count = 0
        return zero_one[count]

def get_randint_zero_five_hundred():
    global count
    try:
        count += 1
        return zero_five_hundred[count]
    except IndexError:
        count = 0
        return zero_five_hundred[count]