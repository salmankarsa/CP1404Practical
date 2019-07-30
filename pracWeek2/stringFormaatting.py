#TODO
# Using a for loop with the range function and string formatting
# produce the following output (right-aligned numbers)
# 0
# 50
# 100

numbers = [0, 50, 100]
for i in range(len(numbers)):
    print("{1}".format(i + 1, numbers[i]))

