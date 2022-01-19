

# write a function to check prime number


def check_prime_number(n):
    for index in range(2, n):
        if n%index == 0:
            return False
    return True

print("tinh hayho hi helo")

n = int(input("enter you number: "))

if check_prime_number(n):
    print(f"{n} is a prime number \n\r end code here")
else:
    print(f"{n} is not a prime number \n\r end code here")

