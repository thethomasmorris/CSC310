def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

if __name__ == '__main__':
    print (factorial (4)) #4!  = 24
    print(factorial(10))  # 10! = 3,628,800