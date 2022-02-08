# from asyncio import unix_events
import random as r
# print(r.random())
# print(r.uniform(1, 5))
# print(r.randint(100, 400))
# list = ['Win', 'lose', 'Draw']
# print(r.choice(list))

# seq = (1, 2, 3, 4, 5, 6, 9, 10, 20, 12)
# print(r.sample(seq, 3))


# make a function for random genrate password

import string
# string.ascii_letters return the string char in upper or lower case


def pass_gen(length):  # function declaration
    str = ''.jion(r.choice(string.ascii_letters) for i in range(length))
    str = ''.jion(r.sample(string.ascii_letters, length))


pass_gen(8)  # function call
