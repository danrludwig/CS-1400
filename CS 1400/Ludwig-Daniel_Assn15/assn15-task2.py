list_of_numbers = []
done = False
count = 0
total = 0

while not done:
    num = input('Enter a number: ')
    if num != '':
        list_of_numbers.append(num)
        count += 1
    else:
        done = True

for i in range(count):
    total += int(list_of_numbers[i])

maxNum = max(list_of_numbers)
minNum = min(list_of_numbers)
avgNum = total / count

print('Number of values entered: ' + str(count))
print('Maximum value: ' + str(maxNum))
print('Minimum value: ' + str(minNum))
print('Sum of all values: ' + str(total))
print('Average Value: ' + str(avgNum))
