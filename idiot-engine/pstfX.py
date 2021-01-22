def converts_to_postfix(regex):
    OP = ['|', '.', '*']
    is_letter = lambda x: x not in OP and x not in '()'
    concataned = [regex[0]]
    for i in range(1, len(regex)):
        if regex[i-1] not in '|(' and regex[i] not in '|)*':
            concataned.append('.' + regex[i])
        else:
            concataned.append(regex[i])
    regex = ''.join(concataned)
    stack, Q = [], []
    for i in '('+regex+')':
        if is_letter(i) or i == '(':
            stack.append(i)
        elif i in OP:
            while stack and stack[-1] in OP and OP.index(stack[-1]) > OP.index(i):
                Q.append(stack.pop())
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                Q.append(stack.pop())
    return Q
