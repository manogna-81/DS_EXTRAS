#this code works in python 3 having matplotlibrary
import matplotlib.pyplot as plt
#this function returns the probability value of given input( i.e the no.of people)
def probability(j):
     #to convert the string to int datatype
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
#for plotting graph
plt.plot(n, p)
plt.xlabel("no.of people")
plt.ylabel("probability")
plt.title("Birthday paradox")
plt.show()
#looping until there is no input provided
if __name__ == '__main__':
    while True:
       try:
         n = input()
         #input() converts the input into a string
         result = probability(n)
         print(format(result,'.100f'))
       #to avoid eof error message in online compilers
       except EOFError:
           break
