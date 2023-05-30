#!/usr/bin/python3
"""Pascal's triangle function"""


def pascal_triangle(n):
    """return list of integers rep Pascal's triangle"""

    if n <= 0:
        return []
    tri = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i+1):
            if j == i:
                row.append(1)
            else:
                row.append(tri[i-1][j-1] + tri[i-1][j])
        tri.append(row)
    return tri
