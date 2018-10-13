import diff_match_patch as dmp_module
import common.Standardize_File_Docx as sfd 
import common.FileCommon as fileCommon
import re as research
import os as os
from common import Logging
import time

start = time.time()
dmp = dmp_module.diff_match_patch()
# get logger 
logger = Logging.getLogger('WELEComparatorV1')
# global variable
originalFiles = []
weleFiles = []
ORIGINAL_ROOT = "D:\Hoang Loc\Comparation\FolderTest\OrginalFiles"
WELE_ROOT = "D:\Hoang Loc\Comparation\FolderTest\WeleFiles"
CSV_ROOT = "D:\Hoang Loc\Comparation\FolderTest\OutPutFiles\CSVFiles"
HTML_ROOT = "D:\Hoang Loc\Comparation\FolderTest\OutPutFiles\HTMLFiles"
STANDARD_ROOT = 'D:\Hoang Loc\Comparation\FolderTest\StandardFiles\Original'
WELE_STANDARD_ROOT = 'D:\Hoang Loc\Comparation\FolderTest\StandardFiles\WELE'
ESL_PATTERN = '\ESL '
WELE_PATTERN = ' WELE.docx'


# read all WELE's member file from folder "/Comparation/FolderTest/OrginalFiles"
allFiles = os.walk(ORIGINAL_ROOT, topdown=False)
for root, dirs, files in allFiles:
    logger.info('>>>>>>>>>>>> START')
    # check has file or not
    if(files == []):
        continue
    # if file is exist, will find the number string in file fileName
    for fileName in files:
        # remove extension in file name
        noExtensionName = fileName.replace('.docx', '')
        
        orginialFile = fileCommon.joinFilePath(root, fileName)
        orginalStandard = STANDARD_ROOT + '\\' + fileName
        strNumber = research.search(r'\d+', fileName).group()
        # if don't find the number string, will continue another file
        if(strNumber == ''):
            continue
        # checking if WELE file is exist or not
        compareFile = WELE_ROOT + ESL_PATTERN + strNumber + WELE_PATTERN
        weleStandard = WELE_STANDARD_ROOT + ESL_PATTERN + strNumber + WELE_PATTERN
        if(fileCommon.checkFileIsExist(compareFile)): 
            orginialContent = sfd.Standardize_File_Docx(orginialFile)
            comparedContent = sfd.Standardize_File_Docx(compareFile)
            #save file 
            sfd.Save_File_Docx(orginialContent, orginalStandard)
            sfd.Save_File_Docx(comparedContent, weleStandard)
            
            diff = dmp.diff_main(orginialContent, comparedContent)
            logger.info('====>> ORGINAL %s: ', diff)
                
            # diff = dmp.diff_main( "Hello World.", "Goodbye World.")
            # Result: [(-1, "Hell"), (1, "G"), (0, "o"), (1, "odbye"), (0, " World.")]
            dmp.diff_cleanupSemantic(diff)
            #print('==========================')
            logger.info('====>> AFTER CLEAN UP %s: ',diff) 
            # Result: [(-1, "Hello"), (1, "Goodbye"), (0, " World.")]
            # create CSV file
            fileCommon.createCSVFile(diff, CSV_ROOT, noExtensionName)
            # craete HTML file
            fileCommon.createHTMLFile(dmp.diff_prettyHtml(diff), HTML_ROOT, noExtensionName)
            end = time.time()
        logger.info('>>>>>>>>>>>> END ==> TOTAL TIME (second) %s', end -start)