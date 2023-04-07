# Python 3

import random

if __name__ == '__main__':

    post_list = []

    f = open("F:/Michelle/hashtags.csv", "r") #open text file

    hashtag_list = f.readlines()

    hashtag_list = list(map(str.strip, hashtag_list)) #get rid of the \r tag from each line

    f.close()

    for count in range(10):

        length = len(hashtag_list) #get length of list

        tag = random.randint(0,length-1) #then generate a random integer less than or equal that length

        post_list.append(hashtag_list.pop(tag)) #remove the tag at that position from the list and  put it in a new list

    print(post_list)

