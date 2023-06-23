class Solution:
    # https://leetcode.com/problems/furthest-building-you-can-reach/editorial/
    # min heap, allocate ladder first, when you run out of ladders pop
    # and use bricks for the smallest ladder climb
    def furthestBuildingHeap(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladder_allocations = [] # min - heap
        for i in range(len(heights) - 1): # go till n-2, since we compare i and i+1
            climb  = heights[i+1] - heights[i]
            if climb <=0:
                continue
            heapq.heappush(ladder_allocations, climb)
            if len(ladder_allocations) <= ladders:
                continue
            # otherwise, pop the smallest ladder allocation and use bricks for that instead
            bricks -= heapq.heappop(ladder_allocations)
            if bricks < 0:
                return i
        return len(heights) - 1
    # OR Use max heap for bricks, assign bricks until we run out
    # once you run out of bricks assign th elargest climb with bricks to ladders

    # Approach 3 - use binary search to find the reachable building
    # heights here is sorted in the manner that buildings are reachable until they aren't

    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        # Helper function to check whether or not the specified building is reachable
        # from the first building with the bricks and ladders we have.
        def is_reachable(building_index):
            # Make a sorted list of all the climbs needed to get to the given building.
            climbs = []
            for h1, h2 in zip(heights[:building_index], heights[1:building_index + 1]):
                if h2 - h1 > 0:
                    climbs.append(h2 - h1)
            climbs.sort()
            # Check whether or not we have enough bricks and ladders to cover all
            # of these climbs. Bricks will be used before ladders.
            bricks_remaining = bricks
            ladders_remaining = ladders
            for climb in climbs:
                # If there are enough bricks left, use those.
                if climb <= bricks_remaining:
                    bricks_remaining -= climb
                # Otherwise, you'll have to use a ladder.
                elif ladders_remaining >= 1:
                    ladders_remaining -= 1
                # And if there are no ladders either, we can't reach buildingIndex.
                else:
                    return False
            return True
         
        # Do the binary search to find the final reachable building.
        lo = 0
        hi = len(heights) - 1
        ans = 0
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if is_reachable(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid -1
        return ans # Note that return lo would be equivalent.    

        # Finding upper middle also works!
        # lo = 0
        # hi = len(heights) - 1
        # while lo < hi:
        #     mid = lo + (hi - lo + 1) // 2
        #     if is_reachable(mid):
        #         lo = mid
        #     else:
        #         hi = mid - 1
        # return hi # Note that return lo would be equivalent.      

