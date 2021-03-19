#This asks the user how many numbers they are going to input
question = int(input("How many numbers do you need to check? "))
odd_count = 0
even_count = 0

#This asks for a number and outputs whether its even or odd
for i in range(question):
  num = int(input("Enter number: "))
  if (num % 2) == 0:
    print(f"{num} is an even number")
    even_count = even_count + 1
  else:
    print(f"{num} is an odd number")
    odd_count = odd_count + 1

print(f"You entered {even_count} even number(s)")
print(f"You entered {odd_count} odd number(s)")

