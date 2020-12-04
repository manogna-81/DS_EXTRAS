def probability(j):
    n=int(j)
    if n >= 365.00:
        return 1
    k = 1
    for i in range(0, n):
         a = (365 - i) / 365
         k = k * a
    return 1 - k
if __name__ == '__main__':
    while True:
      try:
       n = input()
       result = probability(n)
       print(format(result,'.100f'))
      except EOFError:
        break