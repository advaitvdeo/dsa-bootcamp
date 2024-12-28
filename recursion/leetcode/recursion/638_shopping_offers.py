# https://leetcode.com/problems/shopping-offers/?envType=problem-list-v2&envId=backtracking&difficulty=MEDIUM
"""
In LeetCode Store, there are n items to sell. Each item has a price. However, there are some special offers, and a special offer consists of one or more different kinds of items with a sale price.

You are given an integer array price where price[i] is the price of the ith item, and an integer array needs where needs[i] is the number of pieces of the ith item you want to buy.

You are also given an array special where special[i] is of size n + 1 where special[i][j] is the number of pieces of the jth item in the ith offer and special[i][n] (i.e., the last integer in the array) is the price of the ith offer.

Return the lowest price you have to pay for exactly certain items as given, where you could make optimal use of the special offers. You are not allowed to buy more items than you want, even if that would lower the overall price. You could use any of the special offers as many times as you want.
"""
class Solution:
    def shoppingOffers(self, price, special, needs):

        def solve(needs):
            curr_cost = 0
            for i in range(len(needs)):
                curr_cost += price[i] * needs[i]

            for s in special:
                possible = True
                curr_needs = needs[:]
                for j in range(len(curr_needs)):
                    diff = curr_needs[j] - s[j]
                    if diff < 0:
                        possible = False
                        break
                    curr_needs[j] = diff

                if possible:
                    curr_cost = min(curr_cost, s[-1] + solve(curr_needs))
            return curr_cost

        return solve(needs)


price = [2,5]
special = [[3,0,5],[1,2,10]]
needs = [3,2]
a = Solution()
print(a.shoppingOffers(price, special, needs))