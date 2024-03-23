result = 0;
for i in range(int(input())):
	number = int(input());
	result += number // 4;
	if (number % 4 == 1):
		result += 1;
	elif (number % 4 == 0):
		continue;
	else:
		result += 2;

print(result);