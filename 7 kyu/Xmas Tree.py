def xmastree(n):
    tree = []
    s = '#'
    for i in range(n): 
        if i == 0:
            top = (n-1) * '_'+ '#' + (n-1) * '_'
            bottom = top 
            tree.append(top)
        else: 
            s = s + '#'*2
            middle = (n-(i+1)) * '_'+ (s) + (n-(i+1)) * '_'
            tree.append(middle)
    tree.append(bottom)
    tree.append(bottom)
    return tree
