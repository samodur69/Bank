import random
from string import digits

class BankSystem:

    prompt1 = '\n1. Create an acoount\n2. Log into account\n0. Exit>'
    prompt2 = '\n1. Balance\n2. Log out\n0. Exit'
    prompt3 = '\nYou have successfully logged in!\n'
    prompt4 = 'Wrong card number or PIN!\n'
    prompt5 = '\nEnter your card number:\n'
    prompt6 = 'Enter your PIN:\n'
    prompt7 = 'Your card number:>'
    prompt8 = 'Your card PIN:'
    prompt9 = 'Your card has been created'
    prompt10 = 'Wrong choice'
    prompt11 = '\nYou have successfully logged out!\n'
    IIN = '400000'
#    seed_number = random.seed(random.randint(1,1000))
    cards = []
    card_info = {}
    card_balance = {}

    def input(self, prompt):
        action = input(prompt)
        return action

    def main_menu(self):
        while True:
            action = input(self.prompt1)
            if action == '1':
                self.create_card()
            elif action == '2':
                self.login()
            elif action == '0':
                print('Bye!')
                exit()
            # TEST functions
#            elif action == '69':
#                print(self.card_info)
#                print(self.card_balance)
            #TEST functions


    def create_card(self):
       card_number = self.generate_number()
       card_pin = self.generate_pin()
       print('{}\n{}\n{}\n{}\n{}'.format(self.prompt9, self.prompt7, card_number, self.prompt8, card_pin))
       self.cards.append(card_number)
       self.card_info[card_number] = card_pin
       self.card_balance[card_number] = 0

    def generate_number(self):
        number = self.IIN
        for i in range (9):
            number += random.choice(digits)
        number += self.checksum_generate(number)
        return number

    def generate_pin(self):
        pin = ''
        for i in range(4):
            pin += random.choice(digits)
        return pin

    def login(self):
        card_number = self.input(self.prompt5)
        card_pin = self.input(self.prompt6)
        if self.check_pin(card_number, card_pin) == True:
            print(self.prompt3)
            self.account_action()
        else:
            print(self.prompt4)

    def check_pin(self, number, pin):
        if number in self.card_info.keys():
            if pin == self.card_info[number]:
                return True
            else:
                return False
        else:
            return False

    def balance(self):
        pass

    def checksum_generate(self, number):
        # number from string to integer
        dig_list = list(map(int, number))
        # multiply all odd elements by 2
        print(dig_list)
        for i, item in enumerate(dig_list):
            if i % 2 == 0:
                dig_list[i] *= 2
        print(dig_list)
        # substract 9 from numbers over 9
        for i, item in enumerate(dig_list):
            if item > 9:
                dig_list[i] -= 9
        print(dig_list)
        # checksum + sum(dig_list) % 10 must be 0
        print(sum(dig_list))
        checksum = 10 - (sum(dig_list) % 10)
        print(checksum)
        return str(checksum)

    def account_action(self):
        print(self.prompt2)
        action = input()
        if action == '1':
            pass
        elif action == '2':
            print(self.prompt11)
            return
        elif action == '0':
            print('\nBye!')
            exit()
#        else:
#            print(self.prompt10)


BankSystem().main_menu()
