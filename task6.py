#хэллоу агай, можно я сделаю с тру, фалс вместо "да,нет" спасибо!!!!! (просто я это запомнила)

num = 17
if num < 2:
    print(False)
else:
    is_prime = True
    i = 2
    while i * i <= num:
        if num % i == 0:
            is_prime = True
            break
        i += 1
    print(is_prime)

num = 18
if num < 2:
    print(False)
else:
    is_prime = True
    i = 2
    while i * i <= num:
        if num % i == 0:
            is_prime = False
            break
        i += 1
    print(is_prime)

num = 2
if num < 2:
    print(False)
else:
    is_prime = True
    i = 2
    while i * i <= num:
        if num % i == 0:
            is_prime = False
            break
        i += 1
    print(is_prime)