def arithmetic_arranger(problems, answers=False):
    arranged_problems = ''
    if len(problems) > 5:
        raise Exception('Too many problems')
    elements = [i.split() for i in problems]
    first_num = [i[0] for i in elements]
    second_row = [i[1] + ' ' + i[2] for i in elements]
    operator = [i[1] for i in elements]
    second_num = [i[2] for i in elements]
    # Checks for correct import
    for n in first_num:
        if not n.isdigit():
            raise Exception('Numbers must only contain digits.')
        elif len(n) > 4:
            raise Exception ('Numbers cannot be more than four digits.')
    for n in second_num:
        if not n.isdigit():
            raise Exception('Numbers must only contain digits.')
        elif len(n) > 4:
            raise Exception('Numbers cannot be more than four digits.')
    for i in operator:
        if i == '+' or i == '-':
            pass
        else:
            raise Exception("Operator must be '+' or '-'.")
    #continues
    temp_num = zip(first_num, second_num)
    max_num = []
    answer_row = []
    for i in temp_num:
        tmp3 = [int(i[0]), int(i[1])]
        max_num.append(str(max(tmp3)))
    splitter_line = []
    for b in max_num:
        spl = len(b) * '-' + '--'
        splitter_line.append(spl)
    # Answer creation
    for x, o, z in zip(first_num, operator, second_num):
        if o == '+':
            ans = int(x) + int(z)
            answer_row.append(str(ans))
        else:
            ans = int(x) - int(z)
            answer_row.append(str(ans))
    if answers:
        row_arranged = [first_num, second_row, splitter_line, answer_row]
    else:
        row_arranged = [first_num, second_row, splitter_line]
    for row in row_arranged:
        if row is second_row:
            for i, v in enumerate(row):
                mw = len(splitter_line[i])
                tmp = v.split()
                if i == len(row) - 1:
                    arranged_problems += tmp[0] + tmp[1].rjust(mw - 1, ' ')
                else:
                    arranged_problems += tmp[0] + tmp[1].rjust(mw-1, ' ') + '    '
            if row != row_arranged[-1]:
                arranged_problems += '\n'
        else:
            for i, v in enumerate(row):
                mw = len(splitter_line[i])
                if i == len(row) - 1:
                    arranged_problems += v.rjust(mw, ' ')
                else:
                    arranged_problems += v.rjust(mw, ' ') + '    '
            if row != row_arranged[-1]:
                arranged_problems += '\n'
    return arranged_problems

print(arithmetic_arranger(['98 + 35', '3801 - 2', '45 + 43', '123 + 49'],True))

