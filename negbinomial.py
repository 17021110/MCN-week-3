import math

def giaithua(n):
  return math.factorial(n)

def prob(n, p, r):
  return giaithua(n+r-1)/( giaithua(r-1)*giaithua(n) ) * p**r * (1-p)**n

def infoMeasure(n, p, r):
  return -math.log(prob(n, p, r), 2)

def sumProb(N, p, r):
  "Không gian mẫu có N giá trị, xác xuất được phân bố cho N giá trị đó, thì tổng xác xuất của N giá trị đó đương nhiên bằng 1"
  sum=0.0
  for i in range(1,N+1,1):
    sum += prob(i,p,r)
  return sum

def approxEntropy(N,p,r):
  """
  1. Kết quả trả về là giá trị kì vọng của Entropy, bằng tổng tất cả các (lượng tin * xác xuất tương ứng) 
  2. Thực nghiệm :
    approxEntropy(10,1/2,10) = 2.24023
    approxEntropy(100,1/2,10) = 4.14100
    approxEntropy(1000,1/2,10) = 4.14100"""
  sum=0.0
  for i in range(1,N+1,1):
    sum += infoMeasure(i,p,r)*prob(i,p,r)
  return sum

print(sumProb(1200,1/2,10))
print(approxEntropy(1000,1/2,10))