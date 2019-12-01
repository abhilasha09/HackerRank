#!/bin/python3

import sys
max_sum = 0
grid = []
for grid_i in range(20):
	grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
	grid.append(grid_t)
for j in range(20):
    for i in range(20):
        if j<17: 
            a = grid[i][j] * \
            grid[i][j+1] * \
            grid[i][j+2] * \
            grid[i][j+3]
        if i<17: 
            b = grid[i][j] * \
            grid[i+1][j] * \
            grid[i+2][j] * \
            grid[i+3][j]
        if i<17 and j<17:
            c = grid[i][j] * \
            grid[i+1][j+1] * \
            grid[i+2][j+2] * \
            grid[i+3][j+3]
            d = grid[i][19-j] * \
            grid[i+1][18-j] * \
            grid[i+2][17-j] * \
            grid[i+3][16-j]
        if max(a,b,c,d) > max_sum: max_sum = max(a,b,c,d)
print(max_sum)

    #didnt understand the d part properly
def verticle_product(i,j):
    global grid
    if i <= 16:
        return grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j]
    else:
        return 0

def horizontal_product(i,j):
    global grid
    if j <= 16:
        return grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]
    else:
        return 0

def r_diagonal_product(i,j):
    global grid
    if i <= 16 and j <= 16:
        return grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]
    else:
        return 0

def l_diagonal_product(i,j):
    global grid
    if i <= 16 and j >= 3:
        return grid[i][j]*grid[i+1][j-1]*grid[i+2][j-2]*grid[i+3][j-3]
    else:
        return 0

grid = []
for grid_i in range(20):
	grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
	grid.append(grid_t)

maximum_product = 0
for i,row in enumerate(grid):
    for j,element in enumerate(row):
        product = max(verticle_product(i,j),horizontal_product(i,j),r_diagonal_product(i,j),l_diagonal_product(i,j))
        if product > maximum_product:
            maximum_product = product
print(maximum_product)
