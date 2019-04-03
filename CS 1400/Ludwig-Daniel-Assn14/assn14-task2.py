import random

eachNum = []
allNum = []

for i in range(1000):
    num = random.randint(0, 9)
    allNum.append(num)

for i in range(0, 10):
    counts = allNum.count(i)
    eachNum.append(counts)

countOfNumbers = ['0s: ' + str(eachNum[0]),
                  '1s: ' + str(eachNum[1]),
                  '2s: ' + str(eachNum[2]),
                  '3s: ' + str(eachNum[3]),
                  '4s: ' + str(eachNum[4]),
                  '5s: ' + str(eachNum[5]),
                  '6s: ' + str(eachNum[6]),
                  '7s: ' + str(eachNum[7]),
                  '8s: ' + str(eachNum[8]),
                  '9s: ' + str(eachNum[9])]

print('\n'.join(countOfNumbers))

