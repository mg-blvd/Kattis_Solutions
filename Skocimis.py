def bigger_difference(arr):
    first_difference = arr[1] - arr[0]
    second_difference = arr[2] - arr[1]
    if(first_difference > second_difference):
        return first_difference
    return second_difference
numbers = input().split()

for i in range(3):
    numbers[i] = int(numbers[i])

print(bigger_difference(numbers) - 1)    
