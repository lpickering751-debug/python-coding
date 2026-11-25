#are there four positive integers a,b,c,d such that the sum of any two is a factor of the product of all four?

def checkNums(a,b,c,d):
    product = a*b*c*d
    if product%(a+b) == 0:
        if product%(a+c) == 0:
            if product%(a+d) == 0:
                if product%(b+c) == 0:
                    if product%(b+d) == 0:
                        if product%(c+d) == 0:
                            print(a,b,c,d)


for a in range(1,50):
    for b in range(1,50):
        for c in range(1,50):
            for d in range(1,50):
                checkNums(a,b,c,d)