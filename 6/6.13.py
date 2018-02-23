import functools

def rabin_karp(t, s):
    if len(s) > len(t):
        return -1

    BASE = 26
    t_hash = functools.reduce(lambda h, c: h * BASE + ord(c), t[:len(s)], 0)
    s_hash = functools.reduce(lambda h, c: h * BASE + ord(c), s, 0)
    power_s = BASE ** max(len(s) - 1, 0)

    for i in range(len(s), len(t)):
        if t_hash == s_hash and t[i - len(s) : i] == s:
            return i - len(s)

        #Uses rolling has to compute the hash code
        t_hash -= ord(t[i - len(s)]) * power_s
        t_hash = t_hash * BASE + ord(t[i])

        #Tries to match s and t[-len(s):]
    if t_hash == s_hash and t[-len(s):] == s:
        return len(t) - len(s)
    return -1
