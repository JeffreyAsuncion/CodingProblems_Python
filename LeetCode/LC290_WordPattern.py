def wordPattern(self, pattern: str, s: str) -> bool:
        # word key - letter value
        d1 = {}
        d2 = {}

        # split the string of words into a List
        words = s.split()

        # case where pattern and str are not equal returns False
        if len(words) != len(pattern):
            return False

        # iterate thru pattern and words
        for i in range(len(words)):
            # if word not seen in d1 and pattern not seen in d2
            if words[i] not in d1 and pattern[i] not in d2:
                # map word to letter in pattern
                d1[words[i]] = pattern[i]
                # not sure that this does anything
                # let's comment it out
                d2[pattern[i]] = pattern[i]

            # otherwise it is in both maps
            # check if word matches pattern    
            # NOTE is d2[pattern[i]==None] it will give you an error below
            elif d1.get(words[i]) != pattern[i]:
                # this is just to look-see
                # print(d1.get(words[i]), pattern[i])
                return False

        return True