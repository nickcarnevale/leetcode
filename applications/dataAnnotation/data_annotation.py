# Nick Carnevale
# Data Annotation Assessment 7/18/2024


# Inital Thoughts
# Start from the starting point 
# Use a recursive function call to search each open end of the pipe
# Only use recursion at a split in the pipe, if it can go two ways call the search function again
# Add each found letter to a string
# Sort the string in alphabetic sorted(string)
# return the sorted string


def connectedSinks(file_path):
    # First thing we want to do is recieve the input from the text file. 
    with open(file_path, 'r') as file:
        # Next we want to iterate through each line in the file 
        # Ordered pair tuple as key and the pipe or sink as value
        grid = {}

        # key for traversing grid
        # 12 == UP
        # 3 == RIGHT
        # 6 == DOWN
        # 9 == LEFT
        key = {'═':[3,9], '║':[12,6], '╔':[3,6], '╗':[6,9], '╚':[12,3], '╝':[12,9], '╠':[12,3,6], '╣':[12,6,9], '╦':[3,6,9], '╩':[12,3,9], '*':[12,3,6,9]}
        
        # keep track of the starting ordered pair
        index = 0
        start = None

        # initalize the grid
        for line in file:
            # for each pipe or letter, we should store them in a dictionary
            # will will be searching a lot and accessing so a dictionary is fitting
            
            # using a tuple to store the key of the hashmap because tuple is hashable 
            parts = line.split()
            value = parts[0]
            ordered_pair = (int(parts[1]), int(parts[2]))
            grid[ordered_pair] = value

            # get the first ordered pair (where it starts)
            if value == '*':
                start = ordered_pair
            
        # recursive function to traverse the grid
        
        # Adds sinks to the list
        arr = []

        # Need to keep track of visited nodes
        visited = set()

        def traverseGrid(pair): 

            if pair in visited:
                return
            
            visited.add(pair)

            # check each ajacent cell
            x = pair[0]
            y = pair[1]

            # Define directions as (x_offset, y_offset)
            directions = {
                12: (0, 1),
                3: (1, 0),
                6: (0, -1),
                9: (-1, 0)
            }

            for direction in key[grid[pair]]:
                dx, dy = directions[direction]
                next_pair = (x + dx, y + dy)
                
                if next_pair in grid:
                    if grid[next_pair].isalpha():
                        arr.append(grid[next_pair])
                    else:
                        traverseGrid(next_pair)
            return 
        
        traverseGrid(start)
        sorted_arr = sorted(arr)
        sorted_string = ''.join(sorted_arr)

        return sorted_string

            
print(connectedSinks("coding_qual_input.txt"))
