import random
import math
def gruc(model,
         numNewCoords = 1,
         save = True): #use this to handle new coords added to the model smoothly
    maxX = model.gridWidth
    maxY = model.gridHeight

    # for i in range(numOfCoords):
    # listOfCoords.append(generateCoordinate(listOfCoords,maxX,maxY))


    randintsX = range(0, maxX)
    randintsY = range(0, maxY)
    fullCoords = set(model.fullCoords)
    newCoord = []


    x = len(fullCoords) #needs to be hear since while loop would iterate forever otherwise

    while len(fullCoords) < (numNewCoords+x):
        coord = (random.choice(randintsX), random.choice(randintsY))
        fullCoords.add(coord)

        newCoord.append(coord)
    if save == True:
        model.fullCoords = fullCoords

    return newCoord

def rotatePoint(centerPoint,point,angle):
    """Rotates a point around another centerPoint. Angle is in degrees.
    Rotation is counter-clockwise"""
    angle = math.radians(angle)
    temp_point = point[0]-centerPoint[0] , point[1]-centerPoint[1]
    temp_point = ( temp_point[0]*math.cos(angle)-temp_point[1]*math.sin(angle) , temp_point[0]*math.sin(angle)+temp_point[1]*math.cos(angle))
    temp_point = temp_point[0]+centerPoint[0] , temp_point[1]+centerPoint[1]
    return temp_point

def rotateRandomly(shape):

    switcher = {
        1: 0,
        2: 90,
        3: 180,
        4: 270
    }
    degree = switcher.get(random.randint(1,4))
    x = [p[0] for p in shape]
    y = [p[1] for p in shape]
    centeroid = (round(sum(x)/len(shape)),round(sum(y)/len(shape)))
    newShape = []

    for i in shape:
        newShape.append(rotatePoint(centeroid,i,degree))
    return [(round(i[0]),round(i[1])) for i in newShape]

def straight(coord):
    return [coord, (coord[0] + 1, coord[1]), (coord[0] + 2, coord[1]), (coord[0] + 3, coord[1])]

def square(coord):
    return [coord, (coord[0] + 1, coord[1]), (coord[0], coord[1] + 1), (coord[0] + 1, coord[1] + 1)]

def tShape(coord):
    return [coord, (coord[0] + 1, coord[1]), (coord[0] + 2, coord[1]), (coord[0] + 1, coord[1] - 1)]

def lShape(coord):#not working for some reason
    return [coord, (coord[0], coord[1] - 1), (coord[0], coord[1] - 2), (coord[0] + 1, coord[1] - 2)]

def skew(coord):
    return [coord, (coord[0], coord[1] + 1), (coord[0] + 1, coord[1] + 1), (coord[0] + 2, coord[1] + 1)]

def offsetCoords(shape,model):
    maxX = max([i[0] for i in shape])
    maxY = max([i[1] for i in shape])
    print(shape)

    if maxX + 1 > model.gridWidth:
        shape = [i[0]-1 for i in shape]
    else:
        shape = [i[0]+1 for i in shape]

    if maxY + 1 > model.gridHeight:
        shape = [i[1] - 1 for i in shape]
    else:
        shape = [i[1] + 1 for i in shape]

    return shape

def tetromino(model): #thought this sounded catchier than grucLarge xd
    x = random.randint(1,5)

    switcher = {
        1:rotateRandomly(straight(gruc(model,save=False)[0])),
        2:rotateRandomly(square(gruc(model,save=False)[0])),
        3:rotateRandomly(tShape(gruc(model,save=False)[0])),
        4:rotateRandomly(lShape(gruc(model,save=False)[0])),
        5:rotateRandomly(skew(gruc(model,save=False)[0]))
    }

    coordSet = switcher.get(x)

    #now going to go through a phase of shifting the cells to check if we are clear of any obstructions
    while True:
        if [True if i not in model.fullCoords else False for i in coordSet] == [True,True,True,True]:
            break
        else:
            coordSet = offsetCoords(coordSet,model)
            continue

    for i in coordSet:
        model.fullCoords.append(i)
    return coordSet


