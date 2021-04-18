file = open('2001.txt')

content = file.read()
li = content.split()

for x in range(len(li)):
    li[x] = int(li[x])

# part 1  :::  Time complexity O(N cube)
for x in range(len(li)):
    for y in range(x + 1, len(li)):
        
        if li[x] + li[y] == 2020:
            mult = li[x] * li[y]
            print(mult)

# part 2
for x in range(len(li)):
    for y in range(x + 1, len(li)):
        for z in range(y + 1, len(li)):
            
            if li[x] + li[y] + li[z] == 2020:
                mult = li[x] * li[y] * li[z]
                print(mult)
                
