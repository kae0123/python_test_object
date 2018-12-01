#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# file open
input_path = "input.txt"
with open(input_path,"r") as f:
    line = f.read().split("\n")

m = int(line[len(line)-1])

# [[i1:s1],[i2:s2],...]を作成、並び替え
input_lst = []
for l in line[:-1]:
    lst = l.split(":")
    lst[0] = int(lst[0])
    input_lst.append(lst)
input_lst.sort()

# 倍数のときprint
count = 0
for l in input_lst:
    if m % l[0] == 0:
        sys.stdout.write(l[1])
        count+=1
if count==0:
    print(m)