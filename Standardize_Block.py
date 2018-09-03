def Standardize_Block(block):
    x = 2
    while x < len(block) - 1:
        li_p = block[x - 1]
        li_c = block[x]
        li_n = block[x + 1]

        # delete this (remove or insert only one space)
        if li_c[0] != ' ' and len(li_c[1:].split()) == 0:
            block.pop(x)
            x -= 1
        # standardize the block
        # avoid a word seperating into two words
        # (note: more than 2: not resolved yet!!!)
        if(x + 2 < len(block) and li_p[0] != ' ' and li_p[0] == li_n[0] and li_c[0] == ' ' and block[x + 2][0] != ' '):
            # print('ok===>>>3')
            block[x - 1] += block[x][1:] + block[x + 1][1:]
            block[x + 2] = block[x + 2][0] + \
                block[x][1:] + block[x + 2][1:]
            #print(block[x - 1])
            #print(block[x + 2])
            block.pop(x)
            block.pop(x)
            # print(block)
            x -= 2
        elif(li_p[0] != ' ' and li_c[0] != ' ' and li_n[0] != ' ' and li_p[-1] != ' '):
            # print('ok===>>>1')
            block[x - 1] += li_n[1:]
            block.pop(x + 1)
            # print(block)
            x -= 2
        elif(li_p[0] != ' ' and li_c[0] != ' ' and li_n[0] != ' ' and li_p[-1] == ' ' and x + 2 < len(block) and block[x + 2][1] == ' '):
            block[x - 1] += ' ' + block[x + 1][1:]
            block.pop(x + 1)
            x -= 1
            # print('ok===>>>')
            # print(block)
        elif(li_p[0] != ' ' and li_c[1] != ' ' and li_n[0] != ' ' and len(li_c.split()) == 1):
            # print('ok===>>>2')
            # print(li_c[1:])
            block[x - 1] += li_c[1:]
            block[x + 1] = li_n[0] + li_c[1:] + li_n[1:]
            #print(block[x - 1])
            #print(block[x + 1])
            block.pop(x)
            # print(block)
            x -= 1
        x += 1
    return block