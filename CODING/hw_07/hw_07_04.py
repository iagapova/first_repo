def is_integer(s):
    s = str(s)
    if len(s) == 0:
        return False
    else:
        if s.strip().isdigit():
            return True
        elif ((s.strip().startswith('-') or s.strip().startswith('+')) and s.strip()[1:].isdigit()):
            return True
        else:
            return False
