import Standardize_Block as sb
import Detect_Mistakes_Each_Block as dmeb
import diff_match_patch as dmp_module
dmp = dmp_module.diff_match_patch()


# pos: position
# dire: direction
#   -1 => left
#    1 => right

def Get_Letters(content, pos, dire):
    res = ''
    i = 1
    while (content[pos] != ' ' and content[pos + i * dire] != ' '):
        if dire < 0:
            res = content[pos + i * dire] + res
        else:
            res += content[pos + i * dire]
        i += 1
    return res


def Detect_Mistakes_Each_File(orginial_content, compared_content):
    # Desired results
    Remove = []  # from orginial file (WELE file, answer)
    Insert = []  # from compared file (Member's file)

    patches = dmp.patch_make(orginial_content, compared_content)

    ###Start_Remove = []
    ###Count_Remove = []
    Start_Insert = []
    Count_Insert = []

    for blocks in patches:
        lines = str(blocks).splitlines()
        index = lines[0].replace('@', '').replace(',', ' ')\
                        .replace('-', '').replace('+', '').split()
        ###Start_Remove.append(int(index[0]) - 1)
        # Count_Remove.append(int(index[1]))
        Start_Insert.append(int(index[2]) - 1)
        Count_Insert.append(int(index[3]))

    ###cnt = 0
    # for it in range(len(Start_Remove) - 1):
    ###    cnt += Count_Remove[it] - Count_Insert[it]
    ###    Start_Remove[it + 1] += cnt

    for cnt in range(len(patches)):
        lletter = Get_Letters(compared_content, Start_Insert[cnt], -1)
        rletter = Get_Letters(compared_content, Start_Insert[
                              cnt] + Count_Insert[cnt] - 1, 1)

        block = str(patches[cnt]).splitlines()

        #print(block)
        block = sb.Standardize_Block(block)
        block = sb.Standardize_Block(block)
        #print(block)

        res = []
        res = dmeb.Detect_Mistakes_Each_Block(block, lletter, rletter)
        # sometimes, res = []
        leng = int(len(res) / 2)
        for n in range(0, leng):
            Remove.append(res[n])
            Insert.append(res[leng + n])

    ##########################################################################
    # RESULT

    #Remove = [word for pair in Remove for word in pair.split() if  word.islower()]
    #Insert = [word for pair in Insert for word in pair.split() if  word.islower()]
    def PRINT():
        print('=' * 70)
        print('|| ' + 'Remove     '.rjust(30) +
              ' || ' + '     Insert'.ljust(30) + ' ||')
        print('=' * 70)
        # create out put file
        f= open('FileTest/result_file.csv','w+')
        f.write('Remove' + ',' + 'Insert' +'\n')
        for it in range(len(Remove)):
            print('|| ' + Remove[it].rjust(30) +
                  ' || ' + Insert[it].ljust(30) + ' ||')
            #add new line
            f.write(Remove[it] + ',' +Insert[it] +'\n')
        print('=' * 70)
        # finish writing file
        f.close()
        print()
        print()
    PRINT()
    return
