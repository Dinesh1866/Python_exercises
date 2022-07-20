'''Array Problem Solving'''

'''#rotating an array by k times
def rotatingRight(arr,n):
      temp = arr[n-1]
      for i in range(n-1,0,-1):
            arr[i] =arr[i-1]
      arr[0]=temp
      return arr

def printArr(arr,n):
      for i in range(n):
            print(arr[i],end=" ")

def main():
      t = int(input())
      while t>0:
            n,k =map(int,input().split())
            arr = list(map(int,input().split()))
            for i in range(k):
                  rotatingRight(arr,n)
            printArr(arr,n)
            print()
            t -=1

if __name__=='__main__':
      main()
#note this is just a basic method not the best one  


#now will do it for left rotation
def rotateLeft(arr,n):
      temp = arr[0]
      for i in range(0,n-1):
            arr[i]=arr[i+1]
      arr[n-1]=temp

def printArray(arr,n):
      for i in range(n):
            print(arr[i],end=" ")
      print()


def main():
      T = int(input())
      while T>0:
            n,k = map(int,input().split())
            arr = list(map(int,input().split()))
            for i in range(k):
                  rotateLeft(arr,n)
            printArray(arr,n)
            T -=1

if __name__ =="__main__":
      main()'''


#Reversal Algorithm
'''i.e : if the elements to be rotated "right" k no of times then
1. first will reverse the elements from n-1 to n-k
2. then reverse the elements from 0 to n-k-1
3. then reverse the whole array we get the result 
in this how large the array can be we get the result using same no of operations'''

def reverseRightAlgo(arr,i,j):
      while i<j:
            temp = arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            i +=1
            j -=1

def printArr(arr,n):
      for i in range(n):
            print(arr[i],end=" ")
      print()

def main():
      T = int(input())
      while T>0:
            n,k = map(int,input().split())
            arr = list(map(int,input().split()))
            reverseRightAlgo(arr,n-k,n-1)
            reverseRightAlgo(arr,0,n-k-1)
            reverseRightAlgo(arr,0,n-1)
            printArr(arr,n)
            T -=1

if __name__=="__main__":
      main()