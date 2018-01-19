#   This will read file from the specific path
def readFile(fileName):
    file = open(fileName,"r")
    lines = file.readlines()
    
    return lines;

#   This will print like an editor
def printLikeEditor(lineInFile):
    lineNumber = 1
    
    for i in lineInFile:
        print(lineNumber,end=' ')
        for j in range(len(i)):
            print(i[j],end='')
        lineNumber+=1
        
    print()
     

#   Finding the longest common sub-sequence here. Trying to figure out what are the common lines between this wo files    
def lcs(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
    result = [] 
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert a[x-1] == b[y-1]            
            result.append(a[x-1])
            x -= 1
            y -= 1
    return result[::-1]

#   replaceing all the whitespace with certain string of characters.
def replaceSpaceAndNewLine(linesFile):
    lineWdoutSPNL = []
      
    for i in range(len(linesFile)):
        tempLine = linesFile[i].replace('\n','!$\$\$n').replace(' ','!$\$\$s')
        lineWdoutSPNL.append(tempLine)
        
#        lineWdoutSPNL.append(linesFile[i].replace('\n','!').replace(' ','?'))      
    return lineWdoutSPNL 



def checkUpdates(l1, l2, common):
    for i in l1:
        if(i not in common):
            print('--',i.replace('!$\$\$n','[new_line]').replace('!$\$\$s','[space]'))
        
    for i in l2:
        if(i not in common):
            print('++',i.replace('!$\$\$n','[new_line]').replace('!$\$\$s','[space]'))
        

    

if __name__ == "__main__":
#    reading file
    linesFile1 = readFile("first.txt")
    linesFile2 = readFile("second.txt.txt")
    
#   replacing all white spaces and newline with !$\$\$s , !$\$\$n respectively    
    l1 = (replaceSpaceAndNewLine(linesFile1))
    l2 = (replaceSpaceAndNewLine(linesFile2))
    
    
    print('Matching String')
#   Macthing the common elements between two files.    
    commonMatch = lcs(l1,l2)    
    print(commonMatch)
    
    print('File1')
    print(l1)
    print('File1')
    print(l2)
    
    print('Preview')
    
    checkUpdates(l1,l2,commonMatch)
    
