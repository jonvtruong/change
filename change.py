coins = [25, 10, 5, 1]
answer = []
numberCoins = {} 

# all answers found when [0 0 0 num]

def calculate(value, constraint):
    temp = []
    for key in coins: # max out with quarters first
        numberCoins[key] = value//key
        temp.append(numberCoins[key])
        if (value % key == 0): #if solved (exact change combination determined) then add it to list of answers
            answer.append(temp)
            break
        else:
            value -= key*numberCoins[key]

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
    