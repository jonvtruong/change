coins = [25, 10, 5, 1]
answer = []
numberCoins = {} 

# all answers found when [0 0 0 num]

def calculate(value, constraint):
    for j in range(len(constraint)):
        value -= constraint[j] * coins[j] 

    temp = []
    
    #get index of first zero constraint
    index = constraint.index(0)

    while index < len(coins):
        currentCoin = coins[index]
        numberCoins[currentCoin] = value//currentCoin
        temp.append(numberCoins[currentCoin])
        if (value % currentCoin == 0): #if solved (exact change combination determined) then add it to list of answers
            answer.append(temp)
            break
        else:
            value -= currentCoin*numberCoins[currentCoin]
        
        index+=1

def printAnswer():
    for index in answer:
        for i in range(len(index)):
            if (i == 0):
                print("quarters: " + str(index[i]))
            elif (i == 1):
                print("dimes: " + str(index[i]))
            elif (i == 2):
                print("nickels: " + str(index[i]))
            else:
                print("pennies: " + str(index[i]))
        print("------------")

if (__name__ == '__main__'):
    amount = int(input("Amount: "))
    calculate(amount, [0,0,0,0])
    printAnswer()
    