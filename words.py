# -*- coding: utf-8 -*-
# @Author: Rohan Kumara
# @Date:   2020-10-25 22:19:03
# @Last Modified by:   Rohan Kumara
# @Last Modified time: 2020-10-25 22:23:53



name = input('Enter file:')
handle = open(name, 'r')
counts = dict()

for line in handle:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in list(counts.items()):
    if bigcount is None or count > bigcount:
                bigword = word
                bigcount = count


print(bigword, bigcount)