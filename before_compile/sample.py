import math
def sqr(x):
    return x * x
data = [66, 59, 62, 64, 63, 69, 70, 80, 73, 72]
n = len(data)
print("n =%d" % n)
print("Data...")
i=1
for x in data:
    print("%5d:"%i+" %f"%x)
    i+=1
sum = 0.0
for x in data:
    sum += x
average = sum / n
print("Average = %f" % average)

class SampleTest:
    def __init__(self):
        self.variable = 2

    def main(self, a):
        print(a, self.variable)