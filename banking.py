import random
from string import digits
import sqlite3 as sq


class Cards:
    id = 0
    cards = []

    def __init__(self):
        pass


class BankSystem:
    prompt1 = '\n1. Create an account\n2. Log into account\n0. Exit\n'
    prompt2 = '\n1. Balance\n2. Log out\n0. Exit\n'
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
    logged_card = None

    @staticmethod
    def input(prompt):
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
                conn.close()
                exit()

    def create_card(self):
        card_number = self.generate_number()
        card_pin = self.generate_pin()
        user_id = random.randint(0, 1000000)
        print('{}\n{}\n{}\n{}\n{}'.format(self.prompt9, self.prompt7, card_number, self.prompt8, card_pin))
        cur.execute("""INSERT INTO card VALUES (?, ?, ?, ?)""", (user_id, card_number, card_pin, 0))
        conn.commit()

    def generate_number(self):
        number = self.IIN
        for i in range(9):
            number += random.choice(digits)
        number += self.checksum_generate(number)
        return number

    @staticmethod
    def generate_pin():
        pin = ''
        for i in range(4):
            pin += random.choice(digits)
        return pin

    def login(self):
        card_number = self.input(self.prompt5)
        card_pin = self.input(self.prompt6)
        cur.execute("""SELECT 
            number, 
            pin 
            FROM card 
            WHERE number=:number""", {"number": card_number})
        if card_pin in cur.fetchone():
            self.logged_card = card_number
            print(self.prompt3)
            self.account_action()
        else:
            print(self.prompt4)

    def balance(self):
        cur.execute("""SELECT 
            balance 
            FROM card 
            WHERE number=:number""", {"number": self.logged_card})
        print(f'Balance: ', cur.fetchone())

    @staticmethod
    def checksum_generate(number):
        # make list of numbers from string 1char - 1 int
        dig_list = list(map(int, number))
        # multiply all odd elements by 2
        for i, item in enumerate(dig_list):
            if i % 2 == 0:
                dig_list[i] *= 2
            if item > 9:
                dig_list[i] -= 9
        # checksum + sum(dig_list) % 10 must be 0
        checksum = 10 - (sum(dig_list) % 10)
        return str(checksum)

    def account_action(self):
        print(self.prompt2)
        action = input()
        if action == '1':
            self.balance()
        elif action == '2':
            self.logged_card = None
            print(self.prompt11)
        elif action == '0':
            print('\nBye!')
            conn.close()
            exit()


conn = sq.connect('card.s3db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS card 
                (
                id INTEGER,
                number TEXT,
                pin TEXT,
                balance INTEGER DEFAULT 0
                )""")
conn.commit()
BankSystem().main_menu()
