
def fizzbuzz(num):
    if num % 3 ==0 and num % 5 !=0:
        return ("Fizz")
    if num % 5 == 0 and num % 3 != 0:
        return ("Buzz")
    if num % 3 == 0 and num % 5 == 0:
        return ("FizzBuzz")
    elif num % 3 != 0 and num % 5 != 0:
        return (num)
fizzbuzz(15)