# 👉Wrie a programe to generate prime numbers with the help of a
#   function to test prime or not.



def test_prime(num):

    for i in range(2,num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")

num = int(input("Enter number="))
test_prime(num)


#output:-
# Enter number=10
# Not a prime number

# Enter number=11
# Prime number
