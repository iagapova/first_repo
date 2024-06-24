class StripChar:
    def __init__(self, chars):
        self.chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise ValueError("данные не являются строкой")
        return args[0].strip(self.chars)


s1 = StripChar('!@ .,?:')
s2 = StripChar(' ')
print(s1(" Agapova Iryna! "))
print(s2(" Agapova Iryna! "))
