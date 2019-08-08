import docx
from os import listdir
from os.path import isfile, join
import Standardize_File_Docx as sfd
import Detect_Mistakes_Each_File as dmef
import inflect
p = inflect.engine()

nesl = input('Number of ESL: ')
# create out put file
# f = open('Result Each Week/'+ nesl + '.csv', 'w+')
fout = open('Result Each Week/'+ nesl + '.txt', 'w+')

orginial_file_name = '../WELEScripts/ESL ' + nesl + ' WELE.docx'
orginial_content = sfd.Standardize_File_Docx(orginial_file_name)
path = '../WELE Shared folder/Downloaded Member Scripts/ESL' + nesl 

Remove = []
Insert = []

def isNumber(word):
    try:
        int(word)
        return True
    except:
        return False

totalcnt = 0
totalerr = 0
for file in listdir(path):
    if isfile(join(path, file)):
        if ('(' not in file) and (')' not in file) and '.doc' in file:
            #print(file)
            try:
                totalcnt += 1
                compared_content = sfd.Standardize_File_Docx(path + '/' + file)
            except Exception as ex:
                totalerr += 1
                fout.write(file + '\n')
                print('{} => {}' .format(file, ex))
                continue

            rem, ins = dmef.Detect_Mistakes_Each_File(orginial_content, compared_content)
            for n in range(len(ins)):
                # At least heard something wrong!
                if len(rem[n]) != 0 and len(ins[n]) != 0:
                    # If the fault is too long (more than 10 words) => ignore
                    if len(rem[n].split()) < 10 and len(ins[n].split()) < 10:
                        # Convert numbers to words (6 # six, but ignore this wrongdoing)
                        if (isNumber(rem[n]) or isNumber(ins[n])) and \
                            (p.number_to_words(rem[n]) == ins[n] or rem[n] == p.number_to_words(ins[n])):
                            continue
                        else:
                            Remove.append(rem[n])
                            Insert.append(ins[n])

fout.write ('\n{} / {}\n\n' .format(totalerr, totalcnt))
# Summarize the result
res = {}
for n in range(len(Remove)):
    res[Remove[n]] = {'sum_err': 0}

for n in range(len(Remove)):
    res[Remove[n]][Insert[n]] = res[Remove[n]].get(Insert[n], 0) + 1
    res[Remove[n]]['sum_err'] += 1

# Sort
res = dict(sorted(res.items(), key = lambda x: x[1]['sum_err'], reverse = True))

for key, subdict in res.items():
    print('{} >> {} =>' .format(subdict['sum_err'], key), end = ' ')
    for k, v in subdict.items():
        if k is not 'sum_err':
            print('{}: {}' .format(k, v), end = '   ')
    print()

def WRITECSV(res):
    fout.write('Error >> Remove => Insert \n')
    for key, subdict in res.items():
        fout.write('{} >> {} => ' .format(subdict['sum_err'], key))
        for k, v in subdict.items():
            if k is not 'sum_err':
                fout.write('{}: {}   ' .format(k, v))
        fout.write('\n')
    fout.close()

WRITECSV(res)