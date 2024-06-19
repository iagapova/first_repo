from collections import UserString


class NumberString(UserString):
    def number_count(self):
        count = 0
        for i in self.data:
            if i.isdigit():
                count += 1
        print(count)
        return count
