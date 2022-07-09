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
            