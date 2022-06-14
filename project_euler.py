# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

x=[]

for i in range(1,1000):
    if i%3 == 0 or i%5==0:
        x.append(i)
print(sum(x))


# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

the_sum = 0
for number in range(2000000):
    if number > 3:
        for i in range(2,number):
            if (number%i)==0:
                break
            elif i == (number-1):
                the_sum += number

print (the_sum)
