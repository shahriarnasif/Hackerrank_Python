#First solution
n = int(input())
arr = map(int, input().split())


print (sorted(set(arr))[-2])
#Second solution
n = int(input())
arr = list(map(int, input().split()))
print(max([x for x in arr if x!=max(arr)]))

#Third solution
n = int(input())
arr = map(int, input().split())
print(sorted(set(arr))[::-1][1])
