

def ksort(S):

    part = []

    def push(cur):
        C = 0 if cur[2] > 0 else 1

        pos = len(part)
        part.append(cur)
        while pos > 0:
            par = (pos -1) >> 1

            P = 0 if part[par][2] > 0 else 1
            if S[ part[par][P] ] <= S[ cur[C] ]:
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
            while j < N and S[j-1] > S[j]:
                j += 1

            push([i-1, j-1, -1])
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
        if part[0][2] > 0:
            head = part[0][0]
            part[0][0] += 1

        else:
            head = part[0][1]
            part[0][1] -= 1

        if part[0][0] == part[0][1]:
            part[0] = part[-1]
            del part[-1]
            if not part:
                return S[head]

        pos = 0
        cur = part[0]
        C = 0 if part[0][2] > 0 else 1

        n = len(part)
        m = (n) >> 1

        while pos < m:

            sel = (pos << 1) + 1
            if sel+1 < n:
                L = 0 if part[sel][2] > 0 else 1
                R = 0 if part[sel+1][2] > 0 else 1
                if S[ part[sel][L] ] > S[ part[sel+1][R] ]:
                    sel += 1

            P = 0 if part[sel][2] > 0 else 1
            if S[ part[sel][P] ] >= S[ cur[C] ]:
                break

            part[pos] = part[sel]
            pos = sel

        part[pos] = cur
        return S[head]

    ###
    T = [ pop() for _ in range(N) ]
    return T


