# Try to get rid of all exceptions or noises
# And get the standard form: [' abc', '+(-)abc', ('-(+)abc',) ' abc']
# (): optional
# Or to be precise:
# case 1: [' abc', '+abc', '-abc', ' abc']
# case 2: [' abc', '-abc', '+abc', ' abc']
# case 3: [' abc', '+abc', ' abc']
# case 4: [' abc', '-abc', ' abc']


def Standardize_Block(block):
    x = 2
    while x < len(block) - 1:
        lp = block[x - 1]  # previous line
        lc = block[x]     # current line
        ln = block[x + 1]  # next line

        # delete this error (remove or insert only one space)
        # eg. '- ' or '+ '
        if lc[0] != ' ' and len(lc[1:].split()) == 0:
            block.pop(x)
            x -= 1

        # two removing or inserting words in succession
        # eg: ['-lo', '-ve'] => ['-love']
        if lp[0] != ' ' and lc[0] != ' ' and lp[0] == lc[0]:
            block[x - 1] += lc[1:]
            block.pop(x)
            x -= 1

        # three removing or inserting words in succession
        # eg: ['h', '-ear ', '+istor', '-stories', '+y']
        #       => ['h', '-ear stories', '+istor', '+y']
        if lp[0] != ' ' and lc[0] != ' ' and ln[0] != ' ' and \
                lp[0] == ln[0] and any([lc[0] == '-', lc[0] == '+']):
            block[x - 1] += ln[1:]
            block.pop(x + 1)

        # eg. ['-k', ' no', '-w'] => ['-know', '+no']
        # another eg. ['-an ', ' advance', '-d']
        #             => ['-an advanced', '+advance']
        if lp[0] != ' ' and ln[0] != ' ' and lp[0] == ln[0] and \
                lp[-1] != ' ' and lc[-1] != ' ' and \
                lc[0] == ' ' and lc[1] != ' ' and len(lc.split()) == 1:
            # print('ok ===>>> 1')
            block[x - 1] += lc[1:] + ln[1:]
            if lp[0] == '-':
                block[x + 1] = '+' + lc[1:]
            else:
                block[x + 1] = '-' + lc[1:]
            block.pop(x)
            x -= 1

        # eg. ['-in', ' tens' '+ion', '-e'] => ['-intens', '+tension' '-e']
        if lp[0] != ' ' and ln[0] != ' ' and lp[0] != ln[0] and \
                lp[-1] != ' ' and lc[-1] != ' ' and \
                lc[0] == ' ' and lc[1] != ' ' and len(lc.split()) == 1:
            # print('ok ===>>> 1')
            block[x - 1] += lc[1:]
            block[x + 1] = ln[0] + lc[1:] + ln[1:]
            block.pop(x)
            x -= 1
        x += 1
    return block
