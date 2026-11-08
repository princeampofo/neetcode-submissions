class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        l = 0
        res = []
        for r in range(len(nums)):
            
            while deq and nums[r] > deq[-1][1]:
                deq.pop()
  
            deq.append((r, nums[r]))
       
            if r - l + 1 == k:
                res.append(deq[0][1])
                if deq and l == deq[0][0]:
                    deq.popleft()
        
                l += 1
           
        return res