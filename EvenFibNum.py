my_input = int(input("Enter the value of N: "))
fabonacci = [0] * (2 * my_input + 1)
fabonacci[0] = 0
fabonacci[1] = 1
sum = 0

for i in range(2, 2 * my_input + 1):
    fabonacci[i] = fabonacci[i - 1] + fabonacci[i - 2]
    if i % 2 == 0:
        sum += fabonacci[i]

print("Even sum of fibonacci series till number", my_input, "is", sum) 
