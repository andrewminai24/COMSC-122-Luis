def matMultiplier(matA,matB):
    zip_b = zip(*matB)
    zip_b = list(zip_b)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b))
             for col_b in zip_b] for row_a in matA]


def readFromFile(filename):
    allNumbers = []
    for line in open(filename):
        content = line.split()
        for item in content:
            allNumbers.append(int(item))

    return allNumbers


def writeMatrixToFile(filename, matrix):
    opFile = open(filename,'a')
    for matLine in matrix:
        for item in matLine:
            opFile.write(str(item)+' ')
        opFile.write('\n')

    opFile.write('\n----------------------\n\n')
    opFile.close()

#Reading all numbers from file
allNumbers=readFromFile('input.txt')
totalNumbers = len(allNumbers)
X = int(totalNumbers/5)

#Matrix creation
matA=[ allNumbers[i:(i+X)] for i in range(0,totalNumbers,X) ]
matB=[ allNumbers[i:(i+5)] for i in range(0,totalNumbers,5) ]
#MAtrix Multiplication
matRes=matMultiplier(matA,matB)

#Writing data to file
writeMatrixToFile('out.txt', matA)
writeMatrixToFile('out.txt', matB)
writeMatrixToFile('out.txt', matRes)