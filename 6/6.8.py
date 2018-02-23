import itertools

def look_and_say(n):
    def next_numbers(s):
        result, i = [], 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                i += 1
                count += 1
            result.append(str(count) + s[i])
            i += 1
        return ''.join(result)
    s = '1'
    for _ in range(1,n):
        s = next_numbers(s)
    return s

def look_and_say_pythonic(n):
    s = '1'
    for _ in range(n-1):
        s = ''.joing(
                str(len(list(group))) + key for key, group in itertools.groupby(s))
    return s
