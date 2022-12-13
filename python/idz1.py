#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import sys

if __name__ == '__main__':
    tour1 = []
    tour2 = []
    for i in range(0, 26):
        tour1.append(random.randrange(0, 5))
        tour2.append(random.randrange(0, 5))

    tour1, tour2 = tuple(tour1), tuple(tour2)

    print(f"Overall summ: {sum(tour1) + sum(tour2)}")
