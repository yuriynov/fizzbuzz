import sys

if len(sys.argv)>1:
  try:  limit = int(sys.argv[1])
  except ValueError:
    while True:
      try: 
        limit = int(raw_input("Please enter a positive integer."))
        if type(limit) is int:
          break
      except: pass
       
else:
  try:  limit = int(raw_input("Let's play FizzBuzz! How high should we go?"))
  except ValueError:
    while True:
      try: 
        limit = int(raw_input("Please enter a positive integer."))
        if type(limit) is int:
          break
      except: pass


num = 1
running = True

while  num<=limit:
  if (num%3==0) and (num%5==0): 
      print("{} - Fizz Buzz".format(num))
  elif num%3==0:  print("{} - Fizz".format(num))
  elif num%5==0:  print("{} - Buzz".format(num))
  else:   print num
  num += 1

# for num in range(1,limit+1):
#   if (num%3==0) and (num%5==0):
#     print("Fizz Buzz")
#   elif num%3==0:  print("Fizz")
#   elif num%5==0:  print("Buzz")
#   else:   print num

      