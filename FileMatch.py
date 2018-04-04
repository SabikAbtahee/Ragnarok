#   This will read file from the specific path
def readFile(fileName):
    file = open(fileName,"r")
    lines = file.readlines()
    
    return lines;
     
def output(m, fileName):
    with open(fileName, 'w') as out_file:
        for i in range(len(m)):
            out_file.writelines(m[i].value +' '+ m[i].text.replace('!$\$\$n','').replace('!$\$\$s',' ')+'\n')
        
        
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
    return result[::-1] #returns the reverse



#   replaceing all the whitespace with certain string of characters.
def replaceSpaceAndNewLine(linesFile):
    lineWdoutSPNL = []
      
    for i in range(len(linesFile)):
        tempLine = linesFile[i].replace('\n','!$\$\$n').replace(' ','!$\$\$s')
        lineWdoutSPNL.append(tempLine)
    
    return addNewLine(lineWdoutSPNL) 


class map(object):
    def __init__(self, text, value): #value means (+ve)  or (-ve)
        self.text = text
        self.value = value
        
  
def checkUpdate(lines, common, fileNumber): # here fileNumber means the file number.  
    i, j = 0, 0
    m1 = []
    
    lengthOfLines = len(lines)
    lengthOfCommonLines = len(common)
    
    if(fileNumber==1): tempValue = '+'
    elif(fileNumber==0): tempValue = '-' 
#  ################################################  
    while i < (lengthOfLines):
        value = ' '
        if(j<lengthOfCommonLines):
            if(lines[i] != common[j]):
                value = tempValue            
#                print(lines[i])
                m1.append(map(lines[i],value))
                i += 1 
            
            else:
                m1.append(map(lines[i],value))
                i += 1
                j += 1
        else:
             m1.append(map(lines[i],tempValue))
             i += 1
        
    return m1

def checkUpdate2(lines, common, fileNumber): # here fileNumber means the file number.  
    i, j = 0, 0
    m1 = []
    
    lengthOfLines = len(lines)
    lengthOfCommonLines = len(common)
    
    if(fileNumber==1): tempValue = '+'
    elif(fileNumber==0): tempValue = '-' 
#  ################################################  
    while i < (lengthOfLines):
        value = ' '
        if(j<lengthOfCommonLines):
            if(lines[i] != common[j]):
                value = tempValue            
#                print(lines[i])
                m1.append(map(lines[i],value))
                i += 1 
            
            else:
                m1.append(map(lines[i],value))
                i += 1
                j += 1
        else:
             m1.append(map(lines[i],tempValue))
             i += 1
        
    return m1


def temMethod(l2):
    for i in l2:
        print('++',i.replace('!$\$\$n','[new_line]').replace('!$\$\$s','[space]'))
    
def addNewLine(lines):
    if(lines[len(lines) - 1][-7:] != '!$\$\$n'):
        lines[len(lines) - 1]+'!$\$\$n'
    return lines

if __name__ == "__main__":
#    reading file
    linesFile1 = readFile("1.txt")
    linesFile2 = readFile("2.txt")
    
#   replacing all white spaces and newline with !$\$\$s , !$\$\$n respectively    
    l1 = (replaceSpaceAndNewLine(linesFile1))
    l2 = (replaceSpaceAndNewLine(linesFile2))
    
#    printLikeEditor(l1)
#    printLikeEditor(l2)
    print('Matching String')
#   Macthing the common elements between two files.    
    commonMatch = lcs(l1,l2)
    temMethod(commonMatch)
    m1 = checkUpdate(l1, commonMatch, 0)
    m2 = checkUpdate(l2, commonMatch, 1)
    
    output(m1, "output1.txt")
    output(m2, "output2.txt")
    
