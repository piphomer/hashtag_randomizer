# Python 3

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    post_list = []

    #open text file

    f = open("F:/Michelle/hashtag_file.txt", "r")

    # look for strings preceeded by # and make a list of them

    hashtag_list = f.readlines()

    hashtag_list = list(map(str.strip, hashtag_list))

    f.close()

    #get length of list, then generate a random integer less than or equal that length

    count = 0

    while count < 10:

        length = len(hashtag_list)

        tag = random.randint(0,length-1)

        #get the tag at that position and put it in a new list


        post_list.append(hashtag_list.pop(tag))

        #remove the tag from the candidate list (pop?)

        count += 1

    print(post_list)

