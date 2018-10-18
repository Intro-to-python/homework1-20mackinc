#homework1
#Due 10/10/18

# Problem 1
#Write a Python program to count the number
#of even and odd numbers from a series of numbers.
#Be sure to print out what numbers are even and what numbers are odd.
#(Hint use a for loop)

#original homework
#numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
#countOdd = 0
#countEven = 0
#for x in numbers:
#    if not x % 2:
#        countEven+=1
#    else:
        countOdd+=1
#print("Number of even numbers: ",countEven)
#print("Number of odd numbers: ",countOdd)

def numberCount():
  numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
  countOdd = 0
  countEven = 0
  for x in numbers:
    if not x % 2:
      countEven+=1
    else:
        countOdd+=1

  print("Number of even numbers: ",countEven)
  print("Number of odd numbers: ",countOdd)


numberCount()

#x = countOdd
#y = countEven
#for x in range(0,10,2):
    #print(even)
#for y in range(0,10):
    #print(odd)
