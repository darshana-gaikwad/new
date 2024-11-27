# Function to calculate the average of 5 numbers
def average_of_five():
    # Taking input for 5 numbers
    numbers = []
    for i in range(5):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)
    
    # Calculating the average
    average = sum(numbers) / len(numbers)
    
    # Printing the result
    print(f"The average of the numbers {numbers} is {average:.2f}")

# Call the function
average_of_five()
