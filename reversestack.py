import stackinpython

string = "gnimmargorp ni taerg eb ot gniog ma I dna oneitO llehctiM pilihP si eman yM"
reverse_string = ""
s = stackinpython.Stack()

for char in string:
    s.push(char)

while not s.is_empty():
    reverse_string += s.pop()

print(reverse_string)