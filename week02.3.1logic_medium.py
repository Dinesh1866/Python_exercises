#Boxes and Toys
'''from sklearn.cluster import k_means


n = int(input())
count =0
while n>0:
      T,C = map(int,input().split())
      if (C-T)==2:
            count +=1
      n -=1
print (count)'''


#code chef - https://www.codechef.com/LTIME73B/problems/PAJAPONG
'''
T = int(input())
if 1<=T<=50:
      while T>0:
            x,y,k = map(int,input().split())
            if 0<=x<=10**9 and 0<=y<=10**9 and 1<=k<=10**9:
                  total_game = x+y
                  no_of_serves = total_game//k #miss floor division then most times we get wrong ans
                  if no_of_serves%2 ==0:
                        print("Chef")
                  else:
                        print("Paja")
            T -=1
'''


#Perfrct Numbers and Divisors:
T = int(input())
while T >0:
      N = int(input())
      lst = 0
      for num in range(1,N):
            divisor = N%num
            if divisor ==0:
                  lst += num
      if lst == N:
            print("true")
      else:
            print("false")
      T -=1

#Socks
T = int(input())
while T>0:
      pair = int(input())
      worst_case = pair + 1
      print(worst_case)
      T -=1


#show the angle between two hands in analogue clock
T = int(input())
while T>0:
  h,m = map(int,input().split())
  h = h*60*0.5
  angle_small_hand = h +(m*0.5)
  angle_large_hand = m * 6
  if angle_small_hand > angle_large_hand:
      print(int(angle_small_hand-angle_large_hand))
  else:
      print(int(angle_large_hand-angle_small_hand))
  T -=1






#hard Problems
#print n number of times the value with min times with just copy pasting the o/p
def minSteps(n):
      ans = 0
      d = 2
      while n > 1:
            while n % d == 0:
                  ans += d
                  n /= d
            d += 1
      return ans

T = int(input())
while T>0:
      N = int(input())
      print(minSteps(N))
      T -=1