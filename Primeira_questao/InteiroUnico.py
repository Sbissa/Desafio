def find_single_number(numbers):
    numbers = numbers.split(' ')
    numbers = list(map(int, numbers))
    for x in numbers:
        cont = 0
        for y in numbers:
            if x == y:
                cont += 1
        if cont > 1:
            numbers = list(filter(x.__ne__, numbers))
    print(numbers)
    return numbers[0]
