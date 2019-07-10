import Standardize_File_Docx as sfd
import Detect_Mistakes_Each_File as dmef
import os
import pandas as pd
#import glob
#import re


# Desired results
Remove = []  # from orginial file (WELE file, answer)
Insert = []  # from compared file (Member's file)

#
#esl = [10087, 10086, 10085, 10084, 10083]
#esl = [10083]
#member_name = 'Ho Duc Nhan'
filenames = [filename for filename in os.listdir('Single Member/')]
#filenames = ['10094_chau.ecom@gmail.com.docx']
esls = [filename[:5] for filename in filenames]

#esl = [10065]
#member_name = 'Nguyen Thi My Huyen'

def categorise_mistake(Remove,Insert):
    for r,i in zip(Remove,Insert):
        if str(r) ==str(i)+'s' or str(i) == str(r) +'s':
            print r,i

good_vocab = []
for esl,filename in zip(esls,filenames):   
    #orginial_file_name = 'FileTest/ESL' + ' ' + str(esl_index) + ' ' + 'WELE' + '.docx'
    #compared_file_name = 'FileTest/ESL' + ' ' + str(esl_index) + ' ' + member_name + '.docx'

    original_file_name = 'ESL WELE/ESL '+ str(esl)+ ' WELE.docx'
    compared_file_name = 'Single Member/'+filename
    
    original_content = sfd.Standardize_File_Docx(original_file_name)
    compared_content = sfd.Standardize_File_Docx(compared_file_name)
    
    #print(orginial_content)
    #print('***********************')
    #print(compared_content)

    # save file
    #sfd.Save_File_Docx(orginial_content, orginial_file_name)
    #sfd.Save_File_Docx(compared_content, compared_file_name)

    print(compared_file_name)
    Remove, Insert = dmef.Detect_Mistakes_Each_File(original_content, compared_content)
    Corlis = [x for x in original_content.split() if x not in Remove]
    for word in Corlis:
        good_vocab.append([esl,word])
    accu = float(len(Corlis))/len(compared_content.split())
    print accu
#    dmef.PRINT(Remove, Insert)
#    categorise_mistake(Remove,Insert)
    
a = pd.DataFrame(good_vocab)
b= a['word'].value_counts()