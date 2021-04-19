## A positive integer N≤100000, a number x between 0 and 1, and a DNA string s
# of length at most 10 bp.


def probability(N, x, s):
    at = 0
    gc = 0
    for base in s:
        if base == 'A' or base == 'T':
            at += 1
        else:
            gc += 1
    randomProb = (((1 - x) / 2) ** at) * ((x / 2) ** gc)
    p = 1 - (1 - randomProb) ** N
    return ('%0.3f' % p)


s = 'ATAGCCGA'
print(probability(90000, 0.6, s))
