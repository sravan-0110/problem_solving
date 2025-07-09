def is_prime(num):
    if num <= 1:
         return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
        return True

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
print(f"Prime numbers between {start} and {end}:")
for i in range(start, end + 1):
    if is_prime(i):
        print(i, end=' ')
        print("Print all prime numbers between two numbers ")
