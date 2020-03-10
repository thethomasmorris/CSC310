def fibonacci(n):
  """Return the nth Fibonacci number."""
  if n <= 1:
    return n
  else:
    return fibonacci(n-2) + fibonacci(n-1)