# Assuem s is a strin encoded as bytearray
def reverse_words(s):
    # First, reverse the whole string.
    s.reverse()

    def reverse_range(s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start, end = start + 1, end - 1

    start = 0
    while True:
        end = s.find(b' ', start)
        if end < 0:
            break
        reverse_range(s, start, end - 1)
        start = end + 1
    # reverse the last word
    reverse_range(s, start, len(s) - 1)

if __name__ == '__main__':
    a = 'Alice loves Bob'
    b = bytearray()
    b.extend(map(ord,a))
    reverse_words(b)
    print(b.decode())
