def move(snake_index, snake_array): 

    if snake_array[snake_index] == "A": 
        target = snake_index + 1 # the target for an 'A' snake is always towards the right side of the array so we add 1 
        if target < len(snake_array) and snake_array[target] == "_": # makes sure target is in range and is also empty 
            snake_array[snake_index], snake_array[target] = snake_array[target], snake_array[snake_index] 
            return True # returns that the snake has moved so it can be checked by the moveSnake() function 

    elif snake_array[snake_index] == "B": 
        target = snake_index - 1 # the target for an 'B' snake is always towards the left side of the array so we subtract 1 
        if target >= 0 and snake_array[target] == "_": # makes sure target is in range and is also empty 
            snake_array[snake_index], snake_array[target] = snake_array[target], snake_array[snake_index] 
            return True # returns that the snake has moved so it can be checked by the moveSnake() function 
    return False # returns that the snake has not moved so it can be checked by the moveSnake() function 


def hop(snake_index, snake_array):

    if snake_array[snake_index] == "A": 
        target = snake_index + 2 # the target for an 'A' snake is always towards the right side of the array so we add 2 
        if target < len(snake_array) and snake_array[target] == "_" and snake_array[snake_index + 1] == "B": # makes sure target is in range and is also empty and the snake is jumping over a 'B'
            snake_array[snake_index], snake_array[target] = snake_array[target], snake_array[snake_index] 
            return True # returns that the snake has moved so it can be checked by the moveSnake() function 
        
    elif snake_array[snake_index] == "B": 
        target = snake_index - 2 # the target for an 'B' snake is always towards the left side of the array so we subtract 2 
        if target >= 0 and snake_array[target] == "_" and snake_array[snake_index - 1] == "A": # makes sure target is in range and is also empty and the snake is jumping over a 'B' 
            snake_array[snake_index], snake_array[target] = snake_array[target], snake_array[snake_index] 
            return True # returns that the snake has moved so it can be checked by the moveSnake() function 
    return False # returns that the snake has not moved so it can be checked by the moveSnake() function 


def moveSnake(current_turn, current_number, snake_array): 

    number_moved = 0 
    search = list(enumerate(snake_array)) 
    if current_turn == "A": 
        search = list(reversed(search)) 

    for index, snake in search: # if a snake can hop then it hops 
        if number_moved < current_number and snake == current_turn: 
            if hop(index,snake_array): 
                number_moved += 1

    for index, snake in search: # if a snake cannot hop then move it 
        if number_moved < current_number and snake == current_turn: 
            if move(index, snake_array): 
                number_moved += 1 

    return number_moved 


# input snake numbers 
snake_A = int(input("How many snake As?: ")) 
snake_B = int(input("How many snake Bs?: ")) 

maxNumber = max(snake_A,snake_B) 
snakesArray = ["A","A","A","_","B","B","B"] 
snakesArray = ["A"]*snake_A + ["_"] + ["B"]*snake_B # define snake array start point 
endPoint = list(reversed(snakesArray)) # defines end point of snake array (should be reverse of the original list) 

print(*snakesArray) 

currentTurn = "A" 
currentNumber = 1 


while snakesArray != endPoint:

    moves_made = moveSnake(currentTurn,currentNumber,snakesArray) 
    if moves_made > 0:
        print(*snakesArray)

    currentTurn = "B" if currentTurn == "A" else "A" 
    
    if currentNumber < maxNumber:
        currentNumber += 1
    else:
        currentNumber = maxNumber