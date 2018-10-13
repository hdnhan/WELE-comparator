from common import Logging
import os as os


logger = Logging.getLogger('FileCommon')

def listAllFilesFromFolder(folderPath):
    logger.info('>>>>>>>>>>>> START GET ALL FILE IN FOLDER => Folder Path %s', folderPath)
    files = []
    rootFile = os.walk(folderPath, topdown=False)
    for item in rootFile:
        files.append(item)
    logger.info('>>>>>>>>>>>> END GET ALL FILE IN FOLDER => Files %s', files)
    return files

def checkFileIsExist (filePath):
    logger.info('>>>>>>>>>>>> START CHECK FILE => File Path %s', filePath)
    return (os.path.isfile(filePath))

def joinFilePath (root, fileName):
    logger.info('>>>>>>>>>>>> START JOIN FILE PATH => Root: %s -- File Name %s', root, fileName)
    return os.path.join(root, fileName)

def createCSVFile (diff, root, fileName):
    logger.info('>>>>>>>>>>>> START CREATE CSV FILE')
    filePath = root + '\\' + fileName + '.csv'
    logger.info('>>>>>>>>>>>> CSV File path %s', filePath)
    f = open(filePath, 'w+')
    f.write('Lyric' + ',' + 'Correct (0)' + ',' + 'Insert (1)' + ',' + 'Missing (-1)' + '\n')
    for item in diff:
        if (item[0] == 0):
            f.write('\'' + item[1] + ',' + 'Y' + ',' + '' + ',' + '' + '\n')
        elif (item[0] == 1):
            f.write('\'' + item[1] + ',' + '' + ',' + 'Y' + ',' + '' + '\n')
        else:
            f.write('\'' + item[1] + ',' + '' + ',' + '' + ',' + 'Y' + '\n')
    f.close()
    logger.info('>>>>>>>>>>>> END CREATE CSV FILE')

def createHTMLFile (diff, root, fileName):
    logger.info('>>>>>>>>>>>> START CREATE HTML FILE')
    filePath = root + '\\' + fileName + '.html'
    logger.info('>>>>>>>>>>>> HTML File path %s', filePath)
    f = open(filePath, 'w+')
    for item in diff:
        f.write(item)
    f.close()
    logger.info('>>>>>>>>>>>> END CREATE HTML FILE')
