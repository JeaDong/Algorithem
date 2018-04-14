#804. Unique Morse Code Words
class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        key = [chr(i) for i in range(97,123)]
        
        value = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        dic = {}
        
        for i in range(len(key)):
            dic[key[i]] = value[i]
        fina = []
        
        for i in words:
            cur = ''
            for j in i:
                cur += dic[j]
            fina.append(cur)
            
        return len(set(fina))