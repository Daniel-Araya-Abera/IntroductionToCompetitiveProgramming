class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        collection4s = {}
        collection4t = {}
        
        for each in s:
            if each not in collection4s:
                collection4s[each] = 1
            else:
                collection4s[each] += 1

        print('collections for s')

        print(collection4s)
           
        for each in t:
            if each not in collection4t:
                collection4t[each] = 1
            else:
                collection4t[each] += 1

   

        print('collections for 5')        
        print(collection4t)
        for i in range(len(collection4s)):
            try:
                if collection4s[each] == collection4t[each]:
                    pass
            except:
                print("a")
                print(each)
                return False
        for i in range(len(collection4t)):
            try:
                if collection4s[each] == collection4t[each]:
                    pass
            except:
                print("b")
                return False
        return True

first = "anagram"
second = "nagaram"

s = Solution()
print( s.isAnagram(first,second) )
