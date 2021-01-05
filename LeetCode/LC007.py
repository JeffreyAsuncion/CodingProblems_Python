class Solution:
    def reverse(self, x: int) -> int:
        # check Bounds
        if x >= 2 ** 31 - 1 or x <= -2 ** 31 :
            return 0
        neg = 1
        x = str(x)
        
        # this takes care of the neg sign
        if "-" in x:
            neg = -1
            x = x.strip('-')

        # this is a rev for str
        x = x[::-1]
        
        x = int(x) * neg

        # check Bounds
        if x >= 2 ** 31 - 1 or x <= -2 ** 31 :
            return 0
        return x        