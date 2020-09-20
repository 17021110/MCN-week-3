import math

def giaithua(n):
  return math.factorial(n)

def prob(n, p, N):
  return giaithua(N)/( giaithua(n)*giaithua(N-n)*2**N )

def infoMeasure(n, p, N):
  return -math.log(prob(n, p, N), 2)

def sumProb(N, p):
  "Không gian mẫu có N giá trị, xác xuất được phân bố cho N giá trị đó, thì tổng xác xuất của N giá trị đó đương nhiên bằng 1"
  sum=0.0
  for i in range(1,N+1,1):
    sum += prob(i,p,N)
  return sum

def approxEntropy(N,p):
  """
  1. Kết quả trả về là giá trị kì vọng của Entropy, bằng tổng tất cả các (lượng tin * xác xuất tương ứng) 
  2. Thực nghiệm :
    approxEntropy(10,1/2) = 2.69666
    approxEntropy(500,1/2) = 5.529987
    approxEntropy(1000,1/2) = 6.0299876"""
  sum=0.0
  for i in range(1,N+1,1):
    sum += infoMeasure(i,p,N)*prob(i,p,N)
  return sum

print(sumProb(1000,1/2))
print(approxEntropy(1000,1/2))