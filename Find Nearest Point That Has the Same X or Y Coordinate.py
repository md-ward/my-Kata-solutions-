def nearestValidPoint(x: int, y: int, points: list[list[int]]) -> int:
    valid = []
    distance = []
    for i, j in points:
        if i == x or j == y:
            valid.append([i, j])
            distance.append(abs(x-i)+abs(y-j))
    print('valid is {}'.format(valid),'dis is {}'.format(distance),'min : {}'.format( valid[distance.index(min(distance))]))        
    if valid.__len__()==0:
        return -1
    if valid[distance.index(min(distance))][0] == x:
        return 0

    else: return valid[distance.index(min(distance))][0]

x=2
y=2
points=[[5,4],[3,4],[1,3],[3,2],[1,7],[4,2]]


x = 3
y = 4
points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
x = 3
y = 4
points = [[2,3]]
x=1
y=1
points=[[1,2],[3,3],[3,3]]

x=3
y=6
points=[[1,3],[9,8],[3,8],[3,9],[7,4],[3,1],[8,1]]

print(nearestValidPoint(x=x, y=y, points=points))

