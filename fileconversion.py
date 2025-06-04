
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
    
# -------------------------------------------------------------------------------------------------------------