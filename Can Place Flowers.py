class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        #If there is no flower being put, it returns true 
        if n == 0:
            return True
        
        for i in range(len(flowerbed)):
            
            #So in this line works like this:
            #If there is no flower AND
            #the position is 0 - in other words, the first flower in the flowerbed - or the previous flower AND 
            #the position is the quantity of flowers in the flowerbed OR the flower in the next position is empty 
         
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1]==0):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return False



        