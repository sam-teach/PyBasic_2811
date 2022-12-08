i = int()
f = float()
s = str()
b = bool()

i = 123
s = '345'
# new_string = s + i
new_string = s + str(i)
print(new_string)

num_1 = 123
num_2 = 2.24
result = num_1 + num_2
print(type(result), result)
next_result=int(result)
print(type(next_result), next_result)

new_string = int(s) + i
print(new_string)