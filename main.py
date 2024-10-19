def divide(ourdividend, ourDivisor):
  # Determine the sign of the result
  sign = (-1 if ((ourdividend < 0) ^ (ourDivisor < 0)) else 1)

  # Take the absolute value of both numbers
  ourdividend = abs(ourdividend)
  ourDivisor = abs(ourDivisor)

  quotientNumber = 0
  tempNumber = 0

  # Perform division using bit manipulation
  for i in range(31, -1, -1):
      if (tempNumber + (ourDivisor << i) <= ourdividend):
          tempNumber += ourDivisor << i
          quotientNumber |= 1 << i

  # Adjust the sign of the quotient
  if sign == -1:
      quotientNumber = -quotientNumber

  return quotientNumber

# Input the numbers and display the result
a = int(input("Enter a for a/b: "))
b = int(input("Enter b for a/b: "))