from parsers import HcPizzaParser
import numpy as np


if __name__ == '__main__':
    hcp = HcPizzaParser('c_medium.in')

    # parse the first line as numbers and initlize R,C,L,H variables
    R, C, L, H = hcp.to_list(0)

    # parse the rows from 1 to R, passed the transform function extract_MT
    # to convert T as 1 and M as 0 (simplify matrix inspection)
    matrix = hcp.to_matrix(1, R, transform=HcPizzaParser.extract_MT)

    # print the matrix parsed
    print(matrix)

    rect_possible = []
    for x in range(1, H + 1):
        for y in range(1, H + 1):
            mult = x * y
            if mult >= L and mult <= H:
                rect_possible.append((x, y))
    rect_possible = sorted(rect_possible,
                           key=lambda x: x[0]*x[1], reverse=True)

    # if slice used set 1
    sliced = np.zeros_like(matrix)

    print(sliced)
