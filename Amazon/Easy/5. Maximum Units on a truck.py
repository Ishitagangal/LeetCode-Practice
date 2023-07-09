class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse = True)
        boxes = 0
        for box, units in boxTypes:
            if truckSize > box:
                truckSize -= box
                boxes += box * units
            else:
                boxes += truckSize * units
                return boxes
        return boxes
    
    # counting sort for linear solution without using inbuilt sort func
    def maximumUnits2(self, boxTypes, truckSize) -> int:
        boxes, cur_units, count = 0, 1000, Counter()
        for box, units in boxTypes:
            count[units] += box
        
        while cur_units > 0:
            if count[cur_units] > 0:
                amount = min(truckSize, count[cur_units]) # what fits into the truck
                boxes += amount * cur_units
                truckSize -= amount
                if truckSize == 0:
                    return boxes
        return boxes