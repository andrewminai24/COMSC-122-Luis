boynames = []
girlnames = []

with open("BoyNames.txt") as fh:
for line in fh:
boynames.append(line.strip().lower())

with open("GirlNames.txt") as fh:
for line in fh:
girlnames.append(line.strip().lower())

while True:
name = input("Enter a name to search or type QUIT to exit:\n")
if name.upper() == 'QUIT':
break
boyFound = False
girlFound = False
boyLine = 0
girlLine = 0
if name.lower() in boynames:
boyFound = True
boyLine = boynames.index(name.lower()) + 1
  
if name.lower() in girlnames:
girlFound = True
girlLine = girlnames.index(name.lower()) + 1
if boyFound and girlFound:
print("The name '" + name + "' was found in both lists: boy names (line " + str(boyLine) + ") and girl names (line " + str(girlLine) + ").")
elif not (boyFound or girlFound):
print("The name '" + name + "' was not found in either list.")
else:
if boyFound:
print("The name '" + name + "' was found in popular boy names list (line " + str(boyLine) +").")
if girlFound:
print("The name '" + name + "' was found in popular girl names list (line " + str(girlLine) +").")