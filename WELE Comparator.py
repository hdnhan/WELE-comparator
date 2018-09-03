import Standardize_File_Docx as sfd
import Detect_Mistakes_Each_File as dmef

# Desired results
Remove = []  # from orginial file (WELE file, answer)
Insert = []  # from compared file (Member's file)

#
#esl = [10087, 10086, 10085, 10084, 10083]
#esl = [10083]
#member_name = 'Ho Duc Nhan'

esl = [10004]
member_name = 'Hoang Loc'

for esl_index in esl:   
    orginial_file_name = 'FileTest/ESL' + ' ' + str(esl_index) + ' ' + 'WELE'
    compared_file_name = 'FileTest/ESL' + \
        ' ' + str(esl_index) + ' ' + member_name

    orginial_content = sfd.Standardize_File_Docx(orginial_file_name)
    compared_content = sfd.Standardize_File_Docx(compared_file_name)

    # save file
    sfd.Save_File_Docx(orginial_content, orginial_file_name)
    sfd.Save_File_Docx(compared_content, compared_file_name)

    print(compared_file_name)
    dmef.Detect_Mistakes_Each_File(orginial_content, compared_content)
