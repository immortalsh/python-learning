# 八皇后 
queen = [0 for i in range(9)]

def canput(k):
    for i in range(1,k):
        if (queen[k] == queen[i]) or (abs(k - i) == abs(queen[k] - queen[i])):
             return False
    return True
    
def queenput(k):
    for i in range(1,9):
        queen[k]=i
        if (k == (len(queen) - 1 )) and (canput(k)):
            print(queen[1:])
            return
        elif canput(k):
            queenput(k + 1)
queenput(1)
    


       
    
    
