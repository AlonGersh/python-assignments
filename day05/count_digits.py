text = "1232343 34534"

# count the nummber of the number_of_digit
# in the text
count = 0
for char in text:
    if char.isdigit():
            count += 1
            print(count)
print(f"Number of number_of_digit in the text: {count}")
print(len(text))

# Count how many times each digit appears in the text
number_of_digit = [0] * 10
print(number_of_digit)
for char in text:
    if char.isdigit():
         number_of_digit
        [int(char)] +=1
print(number_of_digit)
for i, count in enumerate(number_of_digit):
    print(f"{i}: {count}")