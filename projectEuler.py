def oddsquares():
    squares = []

    for i in range(1,580001):
        square = i**2
        if square % 2 != 0:
            squares.append(square)

    print(sum(squares))

def problem1(num):
    nums = []
    for i in range(1,num):
        if i % 3 == 0 or i % 5 == 0:
            nums.append(i)
    print(sum(nums))

def problem2():
    sequence = []
    a = 1
    b = 2
    for i in range(1,15):
        sequence.append(a)
        sequence.append(b)
        a = a + b
        b = a + b

    print(sequence)
