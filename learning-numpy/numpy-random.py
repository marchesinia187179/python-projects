import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.randint(100)
print(x)

print("\n")

x = random.rand()
print(x)

print("\n")

arr = random.randint(100, size=(3))
print(arr)

print("\n")

arr = random.randint(100, size=(3,5))
print(arr)

print("\n")

arr = random.rand(5)
print(arr)

print("\n")

arr = random.rand(3,5)
print(arr)

print("\n")

x = random.choice([1,2,3,4])
print(x)

print("\n")

arr = random.choice([1,2,3,4], size=(3, 5))
print(arr)

print("\n")

arr = random.choice([1,2,3,4], p=(0.4,0.1,0.3,0.2), size=(100))
print(arr)

print("\n")

arr = random.choice([1,2,3,4], p=(0.1,0.2,0.4,0.3), size=(3,4))
print(arr)

print("\n")

arr = random.randint(10, size=(5))
print(arr)
print(random.shuffle(arr))
print(arr)

print("\n")

arr = random.randint(10, size=(5))
print(arr)
print(random.permutation(arr))
print(arr)

print("\n")

#sns.displot([0,1,2,3,4,5])
#plt.show()

print("\n")

#sns.displot([0,1,2,3,4,5], kind="kde")
#plt.show()

print("\n")

x = random.normal(size=(2,3))
print(x)

print("\n")

x = random.normal(loc=1, scale=2, size=(2,3))
print(x)
#sns.displot(random.normal(size=100), kind="kde")
#plt.show()

print("\n")

arr = random.binomial(n=10, p=0.5, size=10)
print(arr)
#sns.displot(arr)
#plt.show()

print("\n")

data = {
    "normal": random.normal(loc=50, scale=5, size=1000),
    "binomial": random.binomial(n=100, p=0.5, size=1000)
}

#sns.displot(data, kind="kde")
#plt.show()

print("\n")

arr = random.poisson(lam=2, size=1000)
#print(arr)
#sns.displot(arr, kind="kde")
#plt.show()

print("\n")

data = {
  "normal": random.normal(loc=50, scale=7, size=1000),
  "poisson": random.poisson(lam=50, size=1000)
}
#sns.displot(data, kind="kde")
#plt.show()

print("\n")

data = {
  "binomial": random.binomial(n=1000, p=0.01, size=1000),
  "poisson": random.poisson(lam=10, size=1000)
}
#sns.displot(data, kind="kde")
#plt.show()

print("\n")

x = random.uniform(size=10)
print(x)
#sns.displot(x, kind="kde")
#plt.show()

print("\n")

x = random.logistic(loc=10, scale=10, size=10)
print(x)
#sns.displot(x, kind="kde")
#plt.show()

print("\n")

data = {
  "normal": random.normal(scale=2, size=1000),
  "logistic": random.logistic(size=1000)
}
#sns.displot(data, kind="kde")
#plt.show()

print("\n")

x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(x)

print("\n")

x = random.exponential(scale=2, size=10)
print(x)
#sns.displot(x, kind="kde")
#plt.show()

print("\n")

x = random.chisquare(df=1, size=10)
print(x)
#sns.displot(x, kind="kde")
#plt.show()

print("\n")

x = random.rayleigh(size=10)
print(x)
#sns.displot(x, kind="kde")
#plt.show()

print("\n")

x = random.pareto(a=2, size=10)
print(x)
#sns.displot(x)
#plt.show()

print("\n")

x = random.zipf(a=2, size=10)
print(x)
sns.displot(x[x<10])
plt.show()

print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")