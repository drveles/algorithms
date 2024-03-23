n = int(input()) 
m = int(input())
k = int(input())
x = int(input())
y = int(input())
z = int(input())
t = int(input())
a = int(input())

two_n_m = n + m - (x + t)
two_m_k = m + k - (y + t)
two_n_k = n + k - (z + t)
only_n = x - m - two_n_m - t
only_m = x - n - two_n_m - t
only_k = z - n - two_n_k - t
# прочитали только одну книгу;
only_one = only_n + only_m + only_k + t
# прочитали две книги; 
only_two = two_n_m + two_n_k + two_m_k 
# не прочитали ни одной из рекомендованных книг.
no_one = a - (only_one + only_two + t)

print(only_one)
print(only_two)
print(no_one)

# OK