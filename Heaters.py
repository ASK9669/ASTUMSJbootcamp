class Solution:
    def findRadius(self, houses, heaters):
        heaters.sort()
        ans = 0

        for house in houses:
            left = 0
            right = len(heaters) - 1

            # Find the first heater >= house
            while left <= right:
                mid = (left + right) // 2
                if heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid - 1

            # left is the insertion position
            dist1 = float("inf")
            dist2 = float("inf")

            if left < len(heaters):
                dist1 = heaters[left] - house

            if left > 0:
                dist2 = house - heaters[left - 1]

            nearest = min(dist1, dist2)
            ans = max(ans, nearest)

        return ans
