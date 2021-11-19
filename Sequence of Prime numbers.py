#Program to print the prime number in an interval

start = int(input("Enter the first number = "))
end = int(input("Enter the last number = "))

if (start and end > 1):
	for i in range(start,end+1):
		if i>1:
			for j in range(2,i):
				if(i%j == 0):
					break
			else:
				print(i)
else:
	print("Enter the positive numbers(Number should be greater then 1)")
