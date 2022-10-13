import random as rnd
import numpy as np


a=[]

# for i in range(10):
#     v=rnd.random()
#     if v<=0.2:
#         a.append(np.random.normal(0,1))
#     else:
#         a.append(np.random.normal(1,2))

v=np.random.uniform(0,1,100)
# print(v)

# taking two univariate normal distribution with mean 0 , 5 and variance 1 ,2 respectively
for i in np.nditer(v):
    if i<=0.3:
        a.append(np.random.normal(0,1))
    else:
        a.append(np.random.normal(5,2))



mean=np.sum(a)/100.0
# print("Mean = ",mean)

b=np.full(100,mean)

# print("const array = ", b)

c=np.subtract(a,b)

# print("subtracted array = ", c)

d=np.square(c)

# print("squared array = ", d)
e=np.sum(d)
# print("sum ", e)
variance=e/(100-1)

print("estimated mean = ", mean)

print("estimated variance = ", variance)

