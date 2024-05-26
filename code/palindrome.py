# some important notes
# Building a function that receives a string, and checks if its a palindrome
# A string in python is "blablabla", and each character can be accessed by indexing, for example

word = "tree"
print(word)
print(word[1])

for i in range(len(word)):
    print(word[i])


# traffic light example

# 1. You start at traffic lights
# 2. You press the button
# 3. Check the lights, if green, check traffic, then cross, else if red, repeat 3

# 1. You engage visual perception system, motor control system, and tactile perception system, test all systems work
# 2. You use visual perception to find the crossing button
# 3. You compute a plan, with your planning system, to move your hand, and press the crossing button

# Palindrome example

# 1. Receive a word
# 2. Check if Nth character is equal to 0th character
# 3. Check if (N-1)th character is equal to 1st character
# 4. ...
# 5. If at any point, I have no paired character, or if I have run out of pairs,
# and all pairs have been equal, return this is a palindrome, else return this is not a palindrome


def check_if_word_is_palindrome(word: str):
    # word is "johny"
    N = len(word)  # N = 5

    total_pairs = N / 2  # total_pairs = 2.5

    if N % 2 == 1:  # it is odd
        total_pairs = total_pairs - 0.5  # total_pairs = 2

    for i in range(total_pairs):  # so i will be, 0 and then 1 and then it will exit.
        front_pointer = i  # when i=0, front_pointer=0, when i=1, front_pointer=1
        tail_pointer = N - i - 1  # when i=0, tail_pointer=4, when i=1, tail_pointer=3
        if word[front_pointer] != word[tail_pointer]:
            return False
    return True
