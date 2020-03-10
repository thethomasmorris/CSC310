def reverse(S, start, stop):
  """Reverse elements in implicit slice S[start:stop]."""
  if start < stop - 1:                         # if at least 2 elements:
    S[start], S[stop-1] = S[stop-1], S[start]  # swap first and last
    reverse(S, start+1, stop-1)                # recur on rest
  return S

def reverse_iterative(S):
  """Reverse elements in sequence S."""
  start, stop = 0, len(S)
  while start < stop - 1:
    S[start], S[stop-1] = S[stop-1], S[start]  # swap first and last
    start, stop = start + 1, stop - 1          # narrow the range
  return S

if __name__ == '__main__':
    S = [10,20,30,40,50]
    print (reverse(S, 0, len(S))) #Output [50, 40, 30, 20, 10]
    print(reverse_iterative(S))   #Output [10, 20, 30, 40, 50]