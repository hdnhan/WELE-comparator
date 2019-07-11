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
learnt_vocab = []
false_vocab = []
Improve_words = []
Improve_point = 0
Total_Unique_Words = 0
stat = []
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
    Corlis_0 = [x for x in original_content.split() if x not in Remove]
    Corlis = [x for x in Corlis_0 if x in compared_content.split()]
    Learn = [x for x in Corlis if x not in learnt_vocab]
#    df_Learn = pd.DataFrame(Learn,columns=['word'])
    df_Learn = pd.DataFrame([[x,Learn.count(x)] for x in Learn],columns=['word','freq'])
#    Unique_Learn = df_Learn['word'].value_counts()
    Unique_Learn = df_Learn.drop_duplicates().sort_values(by = 'freq')
    Total_Unique_Words += len(Unique_Learn)
    Improve = [x for x in Unique_Learn['word'] if x in false_vocab] 
    Improve_words = Improve_words+Improve 
    Improve_point = Improve_point+len(Improve)
    for word in Corlis:
        good_vocab.append([esl,word])
        learnt_vocab.append(word)
    for word in Remove:
        false_vocab.append(word)
    accu = float(len(Corlis))/len(compared_content.split())
    print "Your accuracy in the ESL {} episode is {:.1f}%".format(esl,accu*100)
    print "You have learnt {} new unique words".format(len(Unique_Learn))
    print "The words that you missed and now you can hear are"
    print " ".join(Improve)
    print "\n"
    stat.append([esl,accu,len(Unique_Learn)])
#    print Unique_Learn
#    print ",".join(Unique_Learn)
#    dmef.PRINT(Remove, Insert)
#    categorise_mistake(Remove,Insert)

print "Summary"
print "The total unique words that you've learnt is {}".format(Total_Unique_Words)
print "The total amound of words that you've once missed and now can hear is {}".format(Improve_point)
print "The words that you now can hear better than before are"
print " ".join(Improve_words)

df_good_vocab = pd.DataFrame(good_vocab, columns = ['esl','word'])
#print df_good_vocab['word'].value_counts()
df_false_vocab = pd.DataFrame(false_vocab, columns = ['word'])
df_stat = pd.DataFrame(stat,columns = ['esl','accu','unique_learn'])
#print df_false_vocab['word'].value_counts()
