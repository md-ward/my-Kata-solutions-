class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
        answer = -1
        man_distance = float("inf")
        
        count = 0 
        
        for point in points:
            if point[0] == x or point[1] == y:
                current_man_distance = abs(point[0] - x) + abs(point[1] - y)
                if current_man_distance < man_distance:
                    man_distance = current_man_distance
                    answer = count
            
            count = count + 1
        
        return answer
x=2
y=2
points=[[5,4],[3,4],[1,3],[3,2],[1,7],[4,2]]
print( Solution.nearestValidPoint(self=1,x=x,y=y,points=points))       