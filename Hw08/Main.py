def main():
#local variables
num_upper = 0
num_lower = 0
num_space = 0
num_digits = 0
data = ''
#open file text.txt for reading
infile = open('text.txt', 'r')
# read in data from the file
data = infile.read()
# Step through each character in the file
#Determine if the character is uppercase
#lowercase, a digit or space and keep a
#running total of each
for ch in data:
if ch.isupper():
num_upper = num_upper + 1
if ch.islower():
num_lower = num_lower + 1
if ch.isdigit():
num_digits = num_digits + 1
if ch.isspace():
num_space = num_space + 1
#Close the file
infile.close()
#Display the totals
print('The number of uppercase letters is:', num_upper)
print('The number of lowercase letters is:', num_lower)
print('The number of digits is:', num_digits)
print('The number if whitespace is:', num_space)
# call the main function
main()