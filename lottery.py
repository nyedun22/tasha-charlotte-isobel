import random


class Lottery:

    def __init__(self):
        self._lottery_numbers = []

    def lotto():
        lottery_numbers = []
        for i in range(0, 6):
            number = random.randint(1, 50)
            # Check if this number has been added to the empty list
            while number in lottery_numbers:
                number = random.sample(1, 50)
            # now that we've got the unique number, append it to the list:
            lottery_numbers.append(number)

        print(lottery_numbers)

if __name__ == "__lotto__":
    main()


