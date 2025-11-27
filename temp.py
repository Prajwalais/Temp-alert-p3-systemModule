import sys

if len(sys.argv) > 1:
    numbers = list(map(int, sys.argv[1:]))
else:

    nums = input("Enter numbers separated by space: ")
    numbers = list(map(int, nums.split()))

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Total Even Numbers: {even_count}")
print(f"Total Odd Numbers: {odd_count}")
