import sys

def diagonal_check(a, b):
    if abs(a[0]-b[0]) == abs(a[1]-b[1]):
        print("Yes")
    else:
        print("No")

def get_idx_after_step(step, idx, size):
    if step == "right" and idx[1] + 1 < size[1]:
        return idx[0], idx[1] + 1
    elif step == "left" and idx[1] - 1 >= 0:
        return  idx[0], idx[1] - 1
    elif step == "down" and idx[0] + 1 < size[0]:
        return  idx[0] + 1, idx[1]
    elif step == "up" and idx[0] -1 >= 0:
        return idx[0] - 1, idx[1]
    else:
        return idx[0], idx[1]

def minefield(data):
    matrix = data.split("\n")[:-2]
    step_D = data.split("\n")[-2] # Dolores
    idx_D = [(idx, row.index('D')) for idx, row in enumerate(matrix) if 'D' in row][0]
    idx_D = get_idx_after_step(step_D, idx_D, (len(matrix), len(matrix[0])))
    step_W = data.split("\n")[-1] # William
    idx_W = [(idx, row.index('W')) for idx, row in enumerate(matrix) if 'W' in row][0]
    idx_W = get_idx_after_step(step_W, idx_W, (len(matrix), len(matrix[0])))
    if matrix[idx_W[0]][idx_W[1]] == 'X':
        diagonal_check(idx_W, idx_D)
    else:
        print("No")

if __name__ == '__main__':
    data = ""
    for line in sys.stdin: 
        data += line
    minefield(data)