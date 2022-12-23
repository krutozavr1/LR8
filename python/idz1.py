#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import sys

if __name__ == '__main__':
    t1 = (random.randrange(0, 5) for i in range(0, 26))
    t2 = (random.randrange(0, 5) for i in range(0, 26))

    print(f"Overall summ: {sum(t1) + sum(t1)}")
