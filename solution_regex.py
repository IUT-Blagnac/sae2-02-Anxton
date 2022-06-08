import re

# return string without spaces
def erase(cc):
    return re.sub(r'^ ([^ ])|([^ ]) ([^ ])|([^ ]) $', r'\1\2\3\4', cc)