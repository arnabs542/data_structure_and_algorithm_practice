from copy import deepcopy

def print_grid(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            print(grid[r][c], end=' ')
        print()
    print()

def valid_space(grid, r,c):
    if grid[r][c] != '+':
        return True
    else:
        return False

def add_vertically(grid, word, r, c):
    letter_index = 0
    if r-1 >= 0 and grid[r-1][c]!='+':
        return False

    while letter_index < len(word) and r < len(grid):
        if grid[r][c] == '+': # word too long
            return False
        elif grid[r][c] != '-' and grid[r][c] != word[letter_index]:
            # another word shares this space and letters don't match
            return False
        grid[r][c] = word[letter_index]
        letter_index+=1
        r+=1
    if r < len(grid) and grid[r][c]!='+': # word too short
        return False
    if letter_index < len(word): # word couldn't fit
        return False
    return True

def add_horizontally(grid, word, r, c):
    letter_index = 0
    if c-1 >= 0 and grid[r][c-1]!='+':
        return False
    while letter_index < len(word) and c < len(grid[0]):
        if grid[r][c] == '+': # word too long
            return False
        elif grid[r][c] != '-' and grid[r][c] != word[letter_index]:
            # another word shares this space and letters don't match
            return False
        grid[r][c] = word[letter_index]
        letter_index+=1
        c+=1
    if c < len(grid) and grid[r][c]!='+': # word too short
        return False
    if letter_index < len(word): # word couldn't fit
        return False
    return True

def solve(grid, words, r, c):
    if len(words)==0:
        print_grid(grid)
        return True
    # if not valid_space(grid, r,c):
    #     return False
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if valid_space(grid, row, col):
                for word in words:
                    new_grid = deepcopy(grid)
                    if add_vertically(new_grid, word, row, col):
                        new_word_list = deepcopy(words)
                        new_word_list.remove(word)
                        if solve(new_grid, new_word_list, row, col):
                            return True
                    new_grid = deepcopy(grid)
                    if add_horizontally(new_grid, word, row, col):
                        new_word_list = deepcopy(words)
                        new_word_list.remove(word)
                        if solve(new_grid, new_word_list, row, col):
                            return True
    return False

grid = [['+', '-', '+', '+', '+', '+', '+', '+', '+', '+'],
        ['+', '-', '+', '+', '+', '+', '+', '+', '+', '+'],
        ['+', '-', '+', '+', '+', '+', '+', '+', '+', '+'],
        ['+', '-', '-', '-', '-', '-', '+', '+', '+', '+'],
        ['+', '-', '+', '+', '+', '-', '+', '+', '+', '+'],
        ['+', '-', '+', '+', '+', '-', '+', '+', '+', '+'],
        ['+', '+', '+', '+', '+', '-', '+', '+', '+', '+'],
        ['+', '+', '-', '-', '-', '-', '-', '-', '+', '+'],
        ['+', '+', '+', '+', '+', '-', '+', '+', '+', '+'],
        ['+', '+', '+', '+', '+', '-', '+', '+', '+', '+']]

words = ['LONDON', 'DELHI', 'ICELAND', 'ANKARA']

grid = [['+', '-', '+', '+', '+', '+', '+', '+', '+', '+'],
        ['+', '-', '+', '+', '+', '+', '+', '+', '+', '+'],
        ['+', '-', '-', '-', '-', '-', '-', '-', '+', '+'],
        ['+', '-', '+', '+', '+', '+', '+', '+', '+', '+'],
        ['+', '-', '+', '+', '+', '+', '+', '+', '+', '+'],
        ['+', '-', '-', '-', '-', '-', '-', '+', '+', '+'],
        ['+', '-', '+', '+', '+', '-', '+', '+', '+', '+'],
        ['+', '+', '+', '+', '+', '-', '+', '+', '+', '+'],
        ['+', '+', '+', '+', '+', '-', '+', '+', '+', '+'],
        ['+', '+', '+', '+', '+', '+', '+', '+', '+', '+']]

words = ['AGRA', 'NORWAY', 'ENGLAND', 'GWALIOR']

solve(grid, words, 0, 0)

grid = [['+', '+', '+', '+', '+', '+', '-', '+', '+', '+'],
        ['+', '+', '-', '-', '-', '-', '-', '-', '+', '+'],
        ['+', '+', '+', '+', '+', '+', '-', '+', '+', '+'],
        ['+', '+', '+', '+', '+', '+', '-', '+', '+', '+'],
        ['+', '+', '+', '-', '-', '-', '-', '-', '-', '+'],
        ['+', '+', '+', '+', '+', '+', '-', '+', '-', '+'],
        ['+', '+', '+', '+', '+', '+', '-', '+', '-', '+'],
        ['+', '+', '+', '+', '+', '+', '+', '+', '-', '+'],
        ['+', '+', '+', '+', '+', '+', '+', '+', '-', '+'],
        ['+', '+', '+', '+', '+', '+', '+', '+', '-', '+']]

words = ['ICELAND', 'MEXICO', 'PANAMA', 'ALMATY']

solve(grid, words, 0, 0)

grid = [['+', '+', '+', '+', '+', '+', '+', '+', '+', '+'],
        ['+', '+', '+', '+', '+', '+', '+', '+', '+', '+'],
        ['+', '+', '+', '+', '+', '+', '+', '+', '+', '+'],
        ['+', '+', '+', '+', '+', '+', '+', '+', '+', '+'],
        ['+', '+', '+', '+', '+', '+', '+', '+', '+', '+'],
        ['+', '+', '+', '+', '+', '+', '+', '+', '+', '+'],
        ['+', '+', '+', '+', '+', '+', '+', '+', '+', '+'],
        ['+', '+', '+', '+', '+', '+', '+', '+', '+', '+'],
        ['+', '+', '+', '+', '+', '+', '+', '+', '+', '+'],
        ['+', '+', '+', '+', '+', '+', '+', '+', '+', '+']]

words = ['', '', '', '']
