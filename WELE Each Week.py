import docx
from os import listdir
from os.path import isfile, join
import Standardize_File_Docx as sfd
import Detect_Mistakes_Each_File as dmef

nesl = input('Number of ESL: ')
orginial_file_name = '../WELEScripts/ESL ' + nesl + ' WELE.docx'
orginial_content = sfd.Standardize_File_Docx(orginial_file_name)
path = '../WELE Shared folder/Downloaded Member Scripts/ESL' + nesl 

Remove = []
Insert = []

def spell(word):
    for letter in word.split():
        if len(letter) > 1:
            return False
    return True

for file in listdir(path):
    if isfile(join(path, file)):
        if ('(' not in file) and (')' not in file):
            #print(file)
            try:
                compared_content = sfd.Standardize_File_Docx(path + '/' + file)
            except Exception as ex:
                print('{} => {}' .format(file, ex))
                continue

            rem, ins = dmef.Detect_Mistakes_Each_File(orginial_content, compared_content)
            for n in range(len(ins)):
                if len(rem[n]) != 0 and len(ins[n]) != 0  and \
                   len(rem[n].split()) < 10 and len(ins[n].split()) < 10 and \
                   '%09' not in ins[n] and spell(rem[n]) == False: 
                    Remove.append(rem[n])
                    Insert.append(ins[n])

#dmef.PRINT(Remove, Insert)

resrem = []
resins = []
stt = []
check = [False] * len(Remove)
for n in range(len(Remove)):
    temp = []
    if check[n] == False:
        resrem.append(Remove[n])
        temp.append(Insert[n])
    for i in range(n + 1, len(Remove)):
        if Remove[n] == Remove[i] and check[i] == False:
            temp.append(Insert[i])
            check[i] = True
    
    
    if check[n] == False:
        checktemp = [False] * len(temp)
        restemp = ''
        for m in range(len(temp)):
            cnt = 0
            if checktemp[m] == False:
                restemp += str(temp[m])
                cnt = 1
            for j in range(m + 1, len(temp)):
                if temp[m] == temp[j] and checktemp[j] == False:
                    cnt += 1
                    checktemp[j] = True
            if cnt > 0:
                restemp += ' => ' + str(cnt) + ' | '
        resins.append(restemp[0:-3])
        stt.append(len(temp))
    
#dmef.PRINT(resrem, resins)

dic = []
for n in range(len(stt)):
    dic.append((n, stt[n])) 
def takeSecond(elem):
    return elem[1]    
dic.sort(key = takeSecond, reverse = True)    
stt =  []
for d in dic:
    stt.append(d[0])

RE = []
IN = []
for n in stt:
    RE.append(resrem[n])
    IN.append(resins[n])

dmef.PRINT(RE, IN)

def WRITECSV(Remove, Insert):
    # create out put file
    f = open('Result Each Week/'+ nesl + '.csv', 'w+')
    f.write('Remove' + ',' + 'Insert' + '\n')
    for it in range(len(Remove)):
        # add new line
        f.write(Remove[it] + ',' + Insert[it] + '\n')
    # finish writing file
    f.close()

WRITECSV(RE, IN)