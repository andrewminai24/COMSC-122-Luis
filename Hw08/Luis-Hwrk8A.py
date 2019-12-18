print("luis")

ifs = open("text.txt",'r')

lines = ifs.readlines()

ifs.close()

upper = 0

lower = 0
white = 0
digit = 0
nonalpha = 0
idx = 0
while idx < len(lines):
    for ch in lines[idx]:
        if ch.islower():
            lower = lower + 1;
        if ch.isupper():
            upper = upper + 1;
        if ch.isdigit():
            digit = digit + 1;
        if ch.isspace():
            white = white + 1;
        if not ch.isalnum() :
            nonalpha = nonalpha + 1;
    idx = idx+1

print (" upper : ", upper)
print (" lower : ", lower)
print (" digit : ", digit)
print (" white : ", white)
print (" nonalphanumeric : ", nonalpha)


print("Luis")

ifs = open("text.txt",'r')

lines = ifs.readlines()

ifs.close()

print (lines)

idx = 0
res = 0
wordarr = []
while idx < len(lines):
    wordarr = lines[idx].split()
    for word in wordarr:
        if word != "--":
          res = res + 1;
    idx = idx + 1

print ( " Number of words : " , res )