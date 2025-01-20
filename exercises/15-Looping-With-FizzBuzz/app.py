def fizz_buzz():
    # ✅↓ Write your code here ↓✅
for i in range(1, 101):  # Corrected 'for i range' to 'for i in range'
    if i % 3 == 0 and i % 5 == 0:  # Check for multiples of both 3 and 5
        print("FizzBuzz")
    elif i % 3 == 0:  # Check for multiples of 3
        print("Fizz")
    elif i % 5 == 0:  # Check for multiples of 5
        print("Buzz")
    else:
        print(i)  # Print the number if none of the above conditions are true

# ❌↓ DON'T CHANGE THE CODE BELOW ↓❌
fizz_buzz()