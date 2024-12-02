#This is a code of LeetCode
#This is the version that i thought but i lasted too long in this 

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        #Check if the concatenated strings are different the return is null, i.e. str1 = "murilo" and str2 = "lopes"
        if str1 + str2 != str2 + str1:
            return ""
        
        #And if the they are the same length, return anyone of them
        if len(str1) == len(str2):
            return str1

        #And if the first is larger than the second, you call the function again and pass as parameters: 
        #str1 with the index with the start as the length of str2 until the end and str2 
        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)

        #This returns the function itself being called with the parameters str2 with the index with the start as the length of str2 until the end and str1
        return self.gcdOfStrings(str1, str2[len(str1):])
        