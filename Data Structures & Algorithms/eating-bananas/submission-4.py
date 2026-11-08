class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def canEat(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            return hours <= h

        while l < r:
            mid = (l + r) // 2

            if canEat(mid):
                r = mid

            else:
                l = mid + 1

        return l