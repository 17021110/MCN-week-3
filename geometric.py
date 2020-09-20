import math

def prob(n, p):
  return 1.0*p**n

def infoMeasure(n, p):
  return -math.log(prob(n, p), 2)

def sumProb(N, p):
  "Không gian mẫu có N giá trị, xác xuất được phân bố cho N giá trị đó, thì tổng xác xuất của N giá trị đó đương nhiên bằng 1"
  sum=0.0
  for i in range(1,N+1,1):
    sum += prob(i,p)
  return sum

def approxEntropy(N,p):
  """
  1. Kết quả trả về là giá trị kì vọng của Entropy, bằng tổng tất cả các (lượng tin * xác xuất tương ứng) 
  2. Thực nghiệm :
    approxEntropy(10,1/2) = 1,988 ~ 2
    approxEntropy(100,1/2) = 1,99998 ~ 2"""
  sum=0.0
  for i in range(1,N+1,1):
    sum += infoMeasure(i,p)*prob(i,p)
  return sum

# print(sumProb.__doc__)
print(sumProb(100,1/2))
# print(approxEntropy.__doc__)
print(approxEntropy(10,1/2))