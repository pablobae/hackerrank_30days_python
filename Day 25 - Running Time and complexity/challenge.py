def is_prime(number: int) -> bool:
    number_is_prime = True

    search_limit = number ** 0.5

    if number == 1:
        return not number_is_prime
    else:
        i = 2
        while number_is_prime and i <= search_limit:
            if number % i == 0:
                number_is_prime = False
            else:
                i += 1

        return number_is_prime


if __name__ == '__main__':
    total_numbers = int(input())

    for i in range(total_numbers):
        number = int(input())
        if is_prime(number):
            print('Prime')
        else:
            print('Not prime')
