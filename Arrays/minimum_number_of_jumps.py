jumps=0
currend=0
currfar=0

for i in range(0,n-1):
  currfar=max(currfar,i+arr[i])
  if i==currend:
    jumps+=1
    currend=currfar
  if currend>=n-1:
    break
if currend<n-1:
  return -1
return jumps
