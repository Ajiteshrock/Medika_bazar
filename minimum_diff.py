speed_array = [470, 240, 380, 440, 190,320, 265]

speed_array.sort()
min_diff = speed_array[1]-speed_array[0]
for i in range(1,len(speed_array)-1):
    if speed_array[i+1]-speed_array[i]<min_diff:
        min_diff = speed_array[i+1]-speed_array[i]


for i in range(len(speed_array)-1):
     if speed_array[i+1]-speed_array[i]==min_diff:
        print((speed_array[i],speed_array[i+1],min_diff))
        break

#time complexity - o(n)