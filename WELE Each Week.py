import docx
import re
from os import listdir
from os.path import isfile, join
import Standardize_File_Docx as sfd
import Detect_Mistakes_Each_File as dmef
import inflect
p = inflect.engine()

# A file result has 3 parts:
# 1: email address that cannot read
# 2: file error / total file
# 3: total error >> remove => insert


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

# All file names  
filenames = []
for file in listdir(path):
    if isfile(join(path, file)) and '.doc' in file:
        filenames.append(file)

# Remove files that re-send to sys and read the latest file
file_names = dict()
for item in filenames:
    if '(' in item and ')' in item:
        # esl_mailaddress.gmail (...).docx
        it = re.split('[) (]', item) #['esl_emailaddress.gmail', '', '...', .'docx']
        file_name = it[0] + it[-1]
        it_count_max = max(file_names.get(file_name, 0), int(it[2]))
        # update the latest file by the number
        file_names[file_name] = it_count_max 
    else:
        # if item is new, value = 0, if not, value = dict[key]
        file_names[item] = file_names.get(item, 0)

total_file_names = len(file_names)
total_unreadable_files = 0
for k, v in file_names.items():
    if v == 0:
        file_name = k
    else:
        # split the last delimiter # k = ...doc...doc...docx <= example
        file_name = k.rsplit('.doc', 1)
        file_name = file_name[0] + ' (' + str(v) + ').doc' + file_name[-1]
    # print(file_name)
    try:
        compared_content = sfd.Standardize_File_Docx(path + '/' + file_name)
    except Exception as ex:
        total_unreadable_files += 1
        fout.write(file_name + '\n')
        print('{} => {}' .format(file_name, ex))
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

fout.write ('\n{} / {}\n\n' .format(total_unreadable_files, total_file_names))

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