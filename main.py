# Python 3

import random
import csv

# def read_txt():
#     f = open("F:/Michelle/hashtag_file.txt", "r") #open text file
#
#     hashtag_list = f.readlines()
#
#     hashtag_list = list(map(str.strip, hashtag_list)) #get rid of the \r tag from each line
#
#     f.close()
#
#     return hashtag_list


def read_csv():
    with open('F:/Michelle/hashtags.csv', mode='r') as infile:
        reader = csv.reader(infile)
        mydict = {rows[0]: int(rows[1]) for rows in reader}
        # print(mydict)
        return mydict


if __name__ == '__main__':

    post_list = []

    # split list into four parts
    # - over 10M posts
    # - 1M - 10M posts
    # - 100k - 1M posts
    # - <100k posts
    # pick 1 from top part, 3 from next part, 6 from next, 6 from last (16 tags total)

    qty_dict = {'d1': 1, 'd2': 3, 'd3': 6, 'd4': 6}

    my_dict = read_csv()

    # print(len(my_dict))

    d1 = dict((k, v) for k, v in my_dict.items() if v >= 10000000)
    d2 = dict((k, v) for k, v in my_dict.items() if (v >= 1000000 and v < 10000000))
    d3 = dict((k, v) for k, v in my_dict.items() if (v >= 100000 and v < 1000000))
    d4 = dict((k, v) for k, v in my_dict.items() if v < 100000)

    candidate_list = list(d2.items())
    print(candidate_list)
    #

    for key, value in qty_dict.items():

        print("Getting tags from dict: ", key)

        for count in range(value):
        #
            print(count)

        #
            length = len(candidate_list) #get length of list
        #
        #     tag = random.randint(0,length-1) #then generate a random integer less than or equal that length
        #     # print(tag)
        #
        #     post_list.append(candidate_list.pop(tag)) #remove the tag at that position from the list and  put it in a new list

    print(post_list)

