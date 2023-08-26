#import sys
s = 'puthon run.py first second'

def parse_args(s):
    
    result = s[(s.find('.py ')+4):]
    
        
            
    
    return result

print(parse_args(s))