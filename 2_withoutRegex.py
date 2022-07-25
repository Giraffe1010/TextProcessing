# Here is the count funtion without using Regex

f = open('ABM.txt','r')
content = f.read()
f.close()

count = 0
for word in content.split():
    if "Alabama" in word:
        count = count+1

print(count)
