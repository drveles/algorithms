info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
        'emp2': {'name': 'Ruslan', 'job': 'Developer'},
        'emp3': {'name': 'Rustam', 'job': 'Tester'}}

for emp, inf in info.items():
    print('Employee ID:', emp)
    for key in inf:
        print(key + ':', inf[key])
    print()


squares = {i: i**2 for i in range(6)}
print(squares)

squares = {i: {j: j**2 for j in range(i + 1)} for i in range(5)}

for value in squares.values():
    print(value)
print(squares)

numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1] 
result = {} 
for num in numbers: 
	result[num] = result.get(num, 0) + 1
print(result)