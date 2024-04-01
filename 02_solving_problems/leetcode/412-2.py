class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []

        for i in range(1, n + 1): 
            temp_string = ''

            if i % 3 == 0:
                temp_string += "Fizz"
            if i % 5 == 0: 
                temp_string += "Buzz"
            if not temp_string: 
                temp_string += str(i)

            answer.append(temp_string)

        return answer

#OK 
# 16% time, 70% memory