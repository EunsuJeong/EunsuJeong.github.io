"""
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv
"""
"""print(np.random.randint(10,size=10))"""
"""크기 10에 0~9까지 랜덤출력"""
"""print(np.random.randint(10,size=10))"""
""" \를 기준으로 위 아래가 바뀜.(행렬)
A= np.matrix("1 2 3;4 5 6;7 8 9")
E= A.transpose()
for row in E:
  print(row)
"""
""" 역행렬 출력 예제
a = np.matrix('1 2; 3 4')
ainv = inv(a)

for row in ainv:
  print(row)
"""

""" 그래프 그리는 예제
plt.plot([1,2,3,4],[4,5,6,7])
plt.axis([0,5,0,10])
plt.show()
plt.cla()
"""
"""
Aarr = np.array([np.random.randint(100,size=2),np.random.randint(100,size=2)])
Barr = np.array([np.random.randint(100,size=2),np.random.randint(100,size=2)])
for z in Aarr:
  print(z)
for asdf in Barr:
  print(asdf)
  """
"""trans
Aarr = np.array([np.random.randint(4,size=2),np.random.randint(4,size=2)])
Barr = np.array([np.random.randint(4,size=2),np.random.randint(4,size=2)])
AarrT = Aarr.transpose()
BarrT = Barr.transpose()
for z in Aarr:
  print(z)
for asdf in Barr:
  print(asdf)
  
for zt in AarrT:
  print(zt)
for asdft in BarrT:
  print(asdft)
"""
""" invers
Aarr = np.array([np.random.randint(4,size=2),np.random.randint(4,size=2)])
Barr = np.array([np.random.randint(4,size=2),np.random.randint(4,size=2)])
AarrI = inv(Aarr)
BarrI = inv(Barr)
for z in Aarr:
  print(z)
for asdf in Barr:
  print(asdf)
  
for zi in AarrI:
  print(zi)
for asdfi in BarrI:
  print(asdfi)
  """

