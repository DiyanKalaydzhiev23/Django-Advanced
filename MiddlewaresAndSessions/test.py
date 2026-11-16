class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1) - 1
        s1_dict = {}

        for l in s1:
            s1_dict[l] = s1_dict.get(l, 0) + 1

        while right < len(s2):
            s1_copy = s1_dict.copy()

            for l in s2[left:right+1]:
                if l in s1_copy and s1_copy[l] > 0:
                    s1_copy[l] -= 1
                else:
                    break
            else:
                return True

            left += 1
            right += 1

        return False


s = Solution()
print(s.checkInclusion("ab", "eidboaoo"))