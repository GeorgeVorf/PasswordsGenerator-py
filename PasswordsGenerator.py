from random import randint


def get_random_password():
    global result
    sum = 0
    result = ''
    while sum < 8:
        random_num = randint(40, 126)
        sum += 1
        result += (chr(random_num))
    return result

def is_valid_password(password):
    upper = list(range(65, 91))
    lower = list(range(97, 123))
    number = list(range(0, 10))
    lengh = ""

    if not len(password)==8:
        return False

    for up in upper:
        if chr(up) in password:
            lengh += (chr(up))
            break

    for low in lower:
        if chr(low) in password:
            lengh += (chr(low))
            break

    for num in number:
        if str(num) in password:
            lengh += (str(num))
            break

    if len(lengh) == 3:
        return True
    else:
        return False


def get_password():
    funk = [False, None]
    while True:
        if is_valid_password(get_random_password()) in funk:
            continue
        else:
            return result

print(get_password())






