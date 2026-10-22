from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        word_len = len(words[0])
        total = len(words)
        need = Counter(words)
        result = []

        for offset in range(word_len):
            left = offset
            count = 0
            seen = Counter()

            for right in range(offset, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in need:
                    seen[word] += 1
                    count += 1

                    while seen[word] > need[word]:
                        seen[s[left:left + word_len]] -= 1
                        left += word_len
                        count -= 1

                    if count == total:
                        result.append(left)
                        seen[s[left:left + word_len]] -= 1
                        left += word_len
                        count -= 1
                else:
                    seen.clear()
                    count = 0
                    left = right + word_len

        return result