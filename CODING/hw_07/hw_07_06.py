def solve_riddle(riddle, word_length, start_letter, reverse=False):
    pos = riddle.find(start_letter)
    if pos == -1:
        result = ''
    elif reverse == False:
        result = riddle[pos: pos + word_length]
    else:
        result = riddle[pos - len(riddle): pos - word_length - len(riddle): -1]
    return result
