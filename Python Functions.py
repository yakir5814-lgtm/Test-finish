def count_digits(number):
    return len(str(abs(number)))  # Returns the number of digits, ignoring negative numbers

def main():
    while True:
        num = int(input("Enter a number (enter -999 to exit): "))
        if num == -999:
            break  # Exit the loop when the user enters -999
        digit_count = count_digits(num)
        print(f"The number {num} has {digit_count} digits.")

# Call the main function
main()