def grid(N):
    # First case
    if N < 0:
        return None
    # Constants
    alphabet = [chr(x) for x in range(ord('a'), ord('z') + 1)]
    d = N
    count = 0
    result = ''

    while d > 26:
        d -= 26
        count += 1

    # First row
    letters = alphabet * count
    for i in range(0, d):
        letters.append(alphabet[i])

    # Case then N <= 26
    if N <= 26:
        for i in range(N):
            for i in range(i, N + i):
                if i > 25:
                    i -= 26
                result += " ".join(alphabet[i])
                result += ' '
            result += '\n'
            result = result.replace(' \n', "\n")

            if result.count('\n') == N:
                return result[0:len(result) - 1]

    else:  # Then N > 26
        result += ''.join(letters)

        for i in range(1, N):
            result += '\n'
            result += ''.join(letters)[i:]
            sk = result[-1]
            left = N - len(''.join(letters)[i:])
            m = sk

            # Adding missing characters
            for x in range(left):
                if m == 'z':
                    m = chr(ord('a'))
                else:
                    m = chr(ord(m) + 1)
                result += chr(ord(m))

        # Adding space between characters
        result = (' '.join(result))
        result = result.replace(' \n ', "\n")
    return result[0:len(result)]
  
  
  
  """
  def grid(N):
    if N < 0 : return None
    abc = 'abcdefghijklmnopqrstuvwxyz' * N
    val = []
    for i in range(N):
        arr = list(abc[i: N+i])
        out = ' '.join(arr)
        val.append(out)
    return '\n'.join(val)
  """
