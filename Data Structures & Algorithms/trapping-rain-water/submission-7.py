class Solution:
    def trap(self, height: List[int]) -> int:
        # maxLeft = []
        # maxRight = [0] * len(height)
        # curr_max = 0
        # res = 0
        # for num in height:
        #     maxLeft.append(curr_max)
        #     curr_max = max(num, curr_max)

        # curr_max = 0
        # for i in range(len(height) - 1, -1, -1):
        #     maxRight[i] = curr_max
        #     curr_max = max(curr_max, height[i])

        # for i in range(len(height)):
        #     trapped = min(maxLeft[i], maxRight[i]) - height[i]
        #     if trapped > 0:
        #         res += trapped
        
        # return res

        maxLeft, maxRight = 0, 0
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            if height[l] < height[r]:
                if height[l] > maxLeft:
                    maxLeft = height[l]
                else:
                    res += maxLeft - height[l]
                l += 1
            
            else:
                if height[r] > maxRight:
                    maxRight = height[r]
                else:
                    res += maxRight - height[r]
                r -= 1

        return res




