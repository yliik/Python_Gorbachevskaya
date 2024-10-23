number = int(input("Enter a number: "))
if number > 7:
    print("Hello")
name = input("Enter a name: ")


if name == "John":
    print("Hello,John")
else:
    print("There is no such name")


array = list(map(int, input("Enter the numbers separated by a space: ").split()))
array_3 = []
for num in array:
    if num % 3 == 0:
        array_3.append(num)
print(array_3)
