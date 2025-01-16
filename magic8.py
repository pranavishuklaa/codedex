import random

q = input("Ask a question: ")

num = random.randint(1, 8)

if num == 1:
    print("Magic 8 ball says: It is certain.")
elif num == 2:
    print("Magic 8 ball says: It is decidedly so.")
elif num == 3:
    print("Magic 8 ball says: Without a doubt.")
elif num == 4:
    print("Magic 8 ball says: Reply hazy, try again.")
elif num == 5:
    print("Magic 8 ball says: Ask again later.")
elif num == 6:
    print("Magic 8 ball says: Better not tell you now.")
elif num == 7:
    print("Magic 8 ball says: My sources say no.")
elif num == 8:
    print("Magic 8 ball says: Outlook not so good.")
else:
    print("Magic 8 ball says: Very Doubtful")

