class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        total_profit = 0
        min_id = -1
        min_value = prices[min_id]
        found_min = False

        for i in range(len(prices) - 1):

            current_element = prices[i]
            next_element = prices[i + 1]

            if not found_min:
                if current_element < next_element:
                    min_value = current_element
                    found_min = True

            else:
                if current_element > next_element:
                    profit = current_element - min_value
                    min_value = current_element

                    total_profit += profit
                    found_min = False

        if found_min: # Check whether we should sell on the last day
            total_profit += prices[-1] - min_value

        return total_profit