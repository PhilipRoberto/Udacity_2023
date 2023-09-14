def too_long(s):
    chk = len(s)
    if chk < 16:
        return "Too short"
    else:
        return s;

print(too_long("philipphilipphilip"));