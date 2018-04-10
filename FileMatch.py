#   This will read file from the specific path
def readFile(fileName):
    file = open(fileName,"r")
    lines = file.readlines()
    
    return lines;
     
def output(m, fileName):
    with open(fileName, 'w') as out_file:
        for i in range(len(m)):

            out_file.writelines(m[i].value +' '+ m[i].text.replace('!$\$\$n','\n').replace('!$\$\$s',' '))

        
        
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


def checkUpdates(l1, l2, common):
    cmm1 = common
    cmm2 = common
    for i in l1:
        if(i not in cmm1):
            print('--',i.replace('!$\$\$n','[new_line]').replace('!$\$\$s','[space'))
#        else:  cmm1.remove(i)  
        
    for i in l2:
        if(i not in cmm2):
            print('++',i.replace('!$\$\$n','[new_line]').replace('!$\$\$s','[space]'))
#        else:  cmm2.remove(i)  

    


class map(object):
    def __init__(self, text, value): #value means (+ve)  or (-ve)
        self.text = text
        self.value = value

        
    return m1

def checkUpdate2(lines, common, fileNumber): # here fileNumber means the file number.  
    i, j = 0, 0
    m1 = []
    


def deletation(l1, common):
    i, j = 0
    m1 = []
    while i < len(l1):
        flag = False
        if(l1[i] != common[j]):
            flag = True
            i+=1
        m1.append(map(l1[i],flag))
        i += 1
        j += 1
    return m1

def addition(l2, common):
    i, j = 0
    m2 = []
    while i < len(l1):
        flag = False
        if(l2[i] != common[j]):
            flag = True
            i+=1
        m2.append(map(l2[i],flag))
        i += 1
        j += 1
    return m2
    
  
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

        if(j<=lengthOfCommonLines-1):
            if(lines[i] != common[j]):
                value = tempValue            
                m1.append(map(lines[i],value))
                i += 1 
            
            else: 
                m1.append(map(lines[i],value))
                i += 1
                j += 1
        else: m1.append(map(lines[i],value))
    

    return m1


def temMethod(l2):
    for i in l2:
        print('++',i.replace('!$\$\$n','[new_line]').replace('!$\$\$s','[space]'))
    

if __name__ == "__main__":
#    reading file
    linesFile1 = readFile("temp/1.txt")
    linesFile2 = readFile("temp/2.txt")

    
#   replacing all white spaces and newline with !$\$\$s , !$\$\$n respectively    
    l1 = (replaceSpaceAndNewLine(linesFile1))
    l2 = (replaceSpaceAndNewLine(linesFile2))
    
#    printLikeEditor(l1)
#    printLikeEditor(l2)
    print('Matching String')
#   Macthing the common elements between two files.    
    commonMatch = lcs(l1,l2)
    temMethod(commonMatch)

    m1 = checkUpdate2(l1, commonMatch, 0)
    m2 = checkUpdate2(l2, commonMatch, 1)
    
    output(m1, "output1.txt")
    output(m2, "output2.txt")
    
#    print(commonMatch)
#    temMethod(commonMatch)

    

    
#    print('File1')
#    print(l1)
#    print('File1')
#    print(l2)
#    
#    print('Preview')
#    
#    checkUpdates(l1,l2,commonMatch)
#############need to solve .. jodi kono line er por '\n' na thake taile '\n' lagiye nite hbe    
