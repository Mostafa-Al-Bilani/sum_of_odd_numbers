number = int(input("choose a number:"))
sum_of_odd = 0
for i in range(number + 1): #We use number + 1 in the range to include the number chosen by the user
    if i % 2 != 0: #We check if the number is odd by checking if the remainder of the division by 2 is 0 or not
        sum_of_odd += i # The odd numbers will be added to sum_of_odd
print(f"The sum of odd numbers up to {number} is {sum_of_odd}")