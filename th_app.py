def fizzbuzz(number):
    if number <= 0:
        return None
    elif number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif  number % 3 == 0:
        return "Fizz"
    elif numer % 5 == 0:
        return "Buzz"
    return number