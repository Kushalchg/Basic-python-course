number_grid=[
    [1,2,3,4],
    [2,4,5,8],
    [3,4,2,1]
]
print(number_grid[1][3])
#nested for loop

for row in number_grid:
    for col in row:
        print(col)