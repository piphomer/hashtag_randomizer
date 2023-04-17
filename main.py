# Python 3

import random
import csv

def read_txt():
    f = open("F:/Michelle/hashtag_file.txt", "r") #open text file

    hashtag_list = f.readlines()

    hashtag_list = list(map(str.strip, hashtag_list)) #get rid of the \r tag from each line

    f.close()

    return hashtag_list


def read_csv():
    with open('F:/Michelle/hashtags.csv', mode='r') as infile:
        reader = csv.reader(infile)
        mydict = {rows[0]: int(rows[1]) for rows in reader}
        print(mydict)
        return mydict


if __name__ == '__main__':


    # split list into four parts
    # - over 10M posts
    # - 1M - 10M posts
    # - 100k - 1M posts
    # - <100k posts
    # pick 1 from top part, 3 from next part, 10 from next (14 tags total)

    post_list = []

    my_dict = read_csv()

    print(len(my_dict))

    d1 = dict((k, v) for k, v in my_dict.items() if v >= 10000000)
    d2 = dict((k, v) for k, v in my_dict.items() if (v >= 1000000 and v < 10000000))
    d3 = dict((k, v) for k, v in my_dict.items() if (v >= 100000 and v < 1000000))
    d4 = dict((k, v) for k, v in my_dict.items() if v < 100000)

    print(d1)
    print(len(d1))
    print(d2)
    print(len(d2))
    print(d3)
    print(len(d3))
    print(d4)
    print(len(d4))




    candidate_list = d1
    print(candidate_list)
    #
    for count in range(2):

        length = len(candidate_list) #get length of list

        tag = random.randint(0,length-1) #then generate a random integer less than or equal that length
        print(tag)

        post_list.append(candidate_list.pop(tag)) #remove the tag at that position from the list and  put it in a new list

    print(post_list)

