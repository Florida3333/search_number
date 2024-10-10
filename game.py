import random
from config import NUM_DIGITS, MAX_GUESSES


class Bagels:
    def run_game(self):
        print(format(NUM_DIGITS))

        while True:
            secretNum = self.getSecretNum()
            print('')
            print(format(MAX_GUESSES))

            numGuesses = 1
            while numGuesses <= MAX_GUESSES:
                guess = ''
                # Продолжаем итерации до получения правильной догадки:
                while len(guess) != NUM_DIGITS or not guess.isdecimal():
                    print('Guess #{}: '.format(numGuesses))
                    guess = input('> ')

                clues = self.getClues(guess, secretNum)
                print(clues)
                numGuesses += 1

                if guess == secretNum:
                    break  # Правильно, выходим из цикла.
                if numGuesses > MAX_GUESSES:
                    print('У вас закончились попытки.')
                    print(
                        'вы пориграли правильный ответ был {}.'.format(
                            secretNum))

            print('Хотите сыграть еще раз? (да или нет)')
            if not input('> ').lower().startswith('y'):
                break
        print('')

    def getSecretNum(self):
        secretNum = ''
        numDigits = NUM_DIGITS
        for i in range(numDigits):
            secretNum += str(random.randint(0, 9))
            if secretNum == "0":
                numDigits += 1
                secretNum = ''
        return secretNum

    def getClues(self, guess, secretNum):

        if guess == secretNum:
            return 'Вы чемпион угадали число!'
        elif guess > secretNum:
            return ('меньше')
        elif guess < secretNum:
            return ('больше')
