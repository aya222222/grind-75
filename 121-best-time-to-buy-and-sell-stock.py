
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # nested for loop (time exceeded)
        # keep = 0
  
        # for inx, num in enumerate(prices):
        #     for inx2, num2 in enumerate(prices):
           
                    
                
        #         if (num >= num2 and inx <= inx2) or (inx2 <= inx):
        #             continue

        #         else:
        #             price = num2 - num

        #             # keep.append(price)
        #             if price > keep:
        #                 keep = price
       
        # # if keep == 0:
        # #     return 0
        # # else:
        # #     return max(keep)  
        # return keep


        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            price = prices[i]
            if price < min_price:
                min_price = price

            if max_profit < price - min_price:
                max_profit = price - min_price

        return max_profit            