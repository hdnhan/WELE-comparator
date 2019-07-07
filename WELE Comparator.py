import Standardize_File_Docx as sfd
import Detect_Mistakes_Each_File as dmef

# Desired results
Remove = []  # from orginial file (WELE file, answer)
Insert = []  # from compared file (Member's file)

#
#esl = [10087, 10086, 10085, 10084, 10083]
#esl = [10083]
#member_name = 'Ho Duc Nhan'

esl = [10065]
member_name = 'Nguyen Thi My Huyen'

for esl_index in esl:   
    #orginial_file_name = 'FileTest/ESL' + ' ' + str(esl_index) + ' ' + 'WELE' + '.docx'
    #compared_file_name = 'FileTest/ESL' + ' ' + str(esl_index) + ' ' + member_name + '.docx'

    original_file_name = 'ESL WELE/ESL 1072 WELE.docx'
    compared_file_name = 'ESL WELE MEMBERS/1072_alexyuna2106@gmail.com.docx'

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

    dmef.PRINT(Remove, Insert)

