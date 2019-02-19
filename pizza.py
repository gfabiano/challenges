from parsers import HcPizzaParser

if __name__ == '__main__':
    hcp = HcPizzaParser('d_big.in')

    # parse the first line as numbers and initlize R,C,L,H variables
    R, C, L, H = hcp.to_list(0)

    # parse the rows from 1 to R, passed the transform function extract_MT
    # to convert T as 1 and M as 0 (simplify matrix inspection)
    matrix = hcp.to_matrix(1, R, transform=HcPizzaParser.extract_MT)

    # print the matrix parsed
    print(matrix)
