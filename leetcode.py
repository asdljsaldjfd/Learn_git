
# -------------------------------------------------------------------------
# Two Sum

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         a=[]
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]+nums[j] == target :
#                     a.append(i)
#                     a.append(j)
#         return a
    
# ---------------------------------------------------------------------------------------------------------

# 121. Best Time to Buy and Sell Stock


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         profit = 0
#         for i in range(len(prices)):
#             for j in range(i+1,len(prices)):
#                 if prices[j] - prices[i] > profit:
#                     profit = prices[j] - prices[i] 
        
#         buy_price = prices[0]
#         for i in prices[1:]:
#             if buy_price > i :
#                 buy_price = i

#             profit = max(profit,i - buy_price) 

#         return profit     
    

# learning the qn now so now first in the buy price we are finding the lowest price we can buy and assign it to the buy_price .. from that indext afterwards
# check the highest profit and check weather they are and assign it to the profit variable .. so we subtract with i because we need to get the mmost progit right the buy_price
# also changes accordingly if the price gets lower  
# -------------------------------------------------------------------------------------------------------------