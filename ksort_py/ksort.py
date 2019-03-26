

def ksort(S):

    part = []

    def push(cur):
        pos = len(part)
        part.append(cur)
        while pos > 0:
            par = (pos -1) >> 1

            if S[ part[par][0] ] <= S[ cur[0] ]:
                break

            part[pos] = part[par]
            pos = par

        part[pos] = cur


    ###
    i = 0
    j = 1
    N = len(S)
    while j < N:
        if S[ j-1 ] > S[ j ]:
            while j < N and S[j-1] >= S[j]:
                j += 1

            push([j-1, i-1, -1])
            i = j
            j = j+1

        else:
            while j < N and S[j-1] <= S[j]:
                j += 1
            push([i, j, +1])
            i = j
            j = j + 1

    if i < N:
        push([i, j, +1])
    ###

    def pop():
        head = part[0][0]
        part[0][0] += part[0][2]


        if part[0][0] == part[0][1]:
            part[0] = part[-1]
            del part[-1]
            if not part:
                return S[head]

        pos = 0
        cur = part[0]

        n = len(part)
        m = (n) >> 1

        while pos < m:

            sel = (pos << 1) + 1
            if sel+1 < n and S[ part[sel][0] ] > S[ part[sel+1][0] ]:
                    sel += 1

            if S[ part[sel][0] ] >= S[ cur[0] ]:
                break

            part[pos] = part[sel]
            pos = sel

        part[pos] = cur
        return S[head]

    ###
    T = [ pop() for _ in range(N) ]
    return T


