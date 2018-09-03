
# Each block has many lines
# lines: a particular block
# pos: position of a line
# sig1, sig2: '-' (remove) or '+' (insert)
# lletter: left letters, if a word separates in a wrong way, it will get
#          the left letter back
# rletter: right letters, if a word separates in a wrong way, it will get
#          the right letter back


def Detect_Mistakes_Each_Block(lines, lletter, rletter):

    res = []
    # ignoring the first, second and end lines
    pos = 2
    while pos < len(lines) - 1:
        line_curr = lines[pos]
        if (line_curr[0] == '-'):
            res = Detect_Pair_Mistakes(lines, pos, '-', '+', lletter)
        elif(line_curr[0] == '+'):
            res = Detect_Pair_Mistakes(lines, pos, '+', '-', lletter)
        line_next = lines[pos + 1]

        if len(res)> 1 and res[2] == 1:
            pos += 2  # jump to the line behind the next line
        if len(res)> 1 and res[2]==2:
            pos += 1
        pos += 1

    Remove = []
    Insert = []
    if res != [] and any([len(res[0]) != 0, len(res[1]) != 0]):
        Remove.append(res[0])
        Insert.append(res[1])

    line_end = lines[-1]
    line_near_end = lines[-2]
    if(len(line_end.split()) == 1 and line_near_end[-1] != ' ' and line_end[1] != ' '):
        Remove[-1] += rletter
        Insert[-1] += rletter

    return Remove + Insert


def Detect_Pair_Mistakes(lines, pos, sig1, sig2, lletter):
    line_prev = lines[pos - 1]  # the privious line
    line_curr = lines[pos]      # the current line
    line_next = lines[pos + 1]  # the next line

    lp = line_prev.split()
    ln = line_next.split()

    case = 0
    remove_word = ''
    insert_word = ''

    if line_curr[0] == sig1:

        # The 3th line in a block
        if pos == 2:
            # a word breaks into two small words
            if len(lp) == 1 and line_prev[-1] != ' ':
                remove_word = lletter
                insert_word = lletter

        # case: has both removing and inserting words
        if (line_next[0] == sig2):
            case = 1
            # line_prev.at(end) != space, meaning it's a part of a word
            if(line_prev[-1] != ' '):
                # add the final string of line_prev
                remove_word += lp[-1]
                insert_word += lp[-1]

            # always exist a line after line_next in this case
            line_next_next = lines[pos + 2]
            lnn = line_next_next.split()
            if(line_next_next[1] != ' '):
                if (line_curr[-1] != ' '):
                    line_curr += lnn[0]
                if (line_next[-1] != ' '):
                    line_next += lnn[0]

            # add '-' to remove_word and '+' to insert_word
            if sig1 == '-':
                remove_word += line_curr[1:]
                insert_word += line_next[1:]
            if sig1 == '+':
                remove_word += line_next[1:]
                insert_word += line_curr[1:]

        # case: has only removing or inserting words
        else:
            case = 2
            if(line_prev[-1] != ' '):
                remove_word += lp[-1]
                insert_word += lp[-1]

            if (sig1 == '-'):
                remove_word += line_curr[1:]
            if (sig1 == '+'):
                insert_word += line_curr[1:]

            if(line_next[1] != ' ' and line_curr[-1] != ' '):
                remove_word += ln[0]
                insert_word += ln[0]

    return [remove_word, insert_word, case]
