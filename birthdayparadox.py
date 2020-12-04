import matplotlib.pyplot as plt
def probability(j):
     n=int(j)
     if n >= 365.00:
        return 1
     k = 1
     for i in range(0, n):
         a = (365-i) / 365
         k = k * a
     return 1 - k
n = []
p = []
for i in range(1, 400):
    n.append(i)
    p.append(probability(i))
plt.plot(n, p)
plt.xlabel("no.of people")
plt.ylabel("probability")
plt.title("Birthday paradox")
plt.show()
if __name__ == '__main__':
    while True:
       try:
         n = input()
         result = probability(n)
         print(format(result,'.100f'))
       except EOFError:
           break