class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        #         plen = len(pattern)
        #         pat = [-1]*plen
        #         pat[0] = 0
        #         for i in range(1,plen):
        #             for j in range(i):
        #                 if pattern[j]==pattern[i]:
        #                     pat[i] = j
        #         res = []
        #         print(pat)
        #         for word in words:
        #             wlen = len(word)
        #             flag = 0
        #             if wlen!=plen:
        #                 continue
        #             for i in range(1,wlen):
        #                 if pat[i]!=-1 and word[i]==word[pat[i]]:
        #                     continue
        #                 elif pat[i]!=-1 and word[i]!=word[pat[i]]:
        #                     flag = 1
        #                     break
        #                 else:
        #                     for j in range(i):
        #                         if word[j]==word[i]:
        #                             flag=1
        #                             break
        #             if flag == 0:
        #                 res.append(word)

        #         return res
        b = pattern

        def is_iso(a):
            return len(a) == len(b) and len(set(a)) == len(set(b)) == len(set(zip(a, b)))

        return filter(is_iso, words)
    # def findAndReplacePattern(self, words, p):
    #     def F(w):
    #         m = {}
    #         return [m.setdefault(c, len(m)) for c in w]
    #     return [w for w in words if F(w) == F(p)]