import re
def is_int(smth):
    return re.match(r'^[1-9]+$', smth)