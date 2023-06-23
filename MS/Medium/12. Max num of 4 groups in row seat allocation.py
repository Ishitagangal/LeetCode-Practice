class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # store which rows have all three possibilities occupied
        # family can be together in 2,3,4,5 or 4,5,6,7 or 6,7,8,9
        occupied = collections.defaultdict(set)
        for row, seat, in reservedSeats:
            if seat in (2,3,4,5):
                occupied[row].add('left')
            if seat in (4,5,6,7):
                occupied[row].add('middle')
            if seat in (6,7,8,9):
                occupied[row].add('right')
        
        result = 2 * n # max possible families, each row can have 1 or 2 families
        for row in occupied:
            if len(occupied[row]) == 3:
                result -= 2
            else:
                result -=1
        return result