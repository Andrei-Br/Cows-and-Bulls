from random import randint

class MyException(Exception):
    """custom exception"""

#function handling the user input and the error checking
def usr_num():
    while True:
        try:
            choice = int(input("Please enter a 4-digits number: "))
            print()
            if choice < 1000 or choice > 9999:
                raise MyException
        except MyException:
            print('The number has to be 4-digits. Please try again.\n')
        except ValueError:
            print('The number has to be an integer. Please try again\n')
        else:
            break
    return choice

#function comparing the user input with the random generated number
def num_check(guess):
    count = 1
    while True:
        num = usr_num()
        check = guess
        cows = 0
        bulls = 0
        while check > 0:
            if check % 10 == num % 10:
                cows += 1
            else:
                bulls += 1
            check = int(check/10)
            num = int(num/10)
        print('Cows:', cows)
        print('Bulls:', bulls)
        print()
        if cows == 4:
            print('You guessed right! It took you', count, 'tries!\n')
            break
        else:
            print('Try again!\n')
            count += 1
            continue

#main function
if __name__ == '__main__':
    guess = randint(1000, 10000)
    print('Guess:', guess,'\n')
    num_check(guess)