""" 
#This is the code i tried but got wrong 
class Solution(object):
    def kidsWithCandies(candies, extraCandies):

        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]


        results = []
        for i in range(len(candies)):
            #kidCandies = candies[i] + extraCandies
            for j in range(len(candies)):
                if candies[i] + extraCandies > candies[j]:
                    print("Kid Candy: "+ str(candies[i] + extraCandies)  +"\n Candies[" ,j ,"]: ", candies[j])
                    results.append(True)
                else: 
                    results.append(False)

        return results

    print(kidsWithCandies([2,3,5,1,3], 3))

"""

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        #This is the part of the code that i didnt thought of, when i saw i cried a little
        max_candies = max(candies)
        
        result = []
        for candy in candies:
            if candy + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        
        return result