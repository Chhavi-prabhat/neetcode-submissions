class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final={}
        for word in strs:
            char_count={}
            for char in word:
                char_count[char]=char_count.get(char,0)+1
            # final.append(char_count)
            key=tuple(sorted(char_count.items())) 
            if key in final:
                final[key].append(word)
            else:
                final[key]=[word]
        return list(final.values())

   