import numpy as np

def euclidean(tup1,tup2):
    distance = np.sqrt(((tup2[0]-tup1[0])**2) + ((tup2[1]-tup1[1])**2))
    return distance

def manhattan(tup1,tup2):
    distance = abs(tup1[0]-tup2[0]) + abs(tup1[1]-tup2[1])
    return distance

def chebyshev(tup1,tup2):
    distance = max(abs(tup1[0]-tup2[0]),abs(tup1[1]-tup2[1]))
    return distance

def closest_cities(target,cities,K,distance):
    if distance == 'Manhattan':
        dist_city = [(i,manhattan(target,tup)) for i,tup in enumerate(cities)]
        dist_city.sort(key=lambda tup: tup[1]) # sorted list of tuples (index,distance)
    elif distance == "Chebyshev":
        dist_city = [(i,chebyshev(target,tup)) for i,tup in enumerate(cities)]
        dist_city.sort(key=lambda tup: tup[1]) # sorted list of tuples (index,distance)
    else:
        dist_city = [(i,euclidean(target,tup)) for i,tup in enumerate(cities)]
        dist_city.sort(key=lambda tup: tup[1]) # sorted list of tuples (index,distance)
        
    return dist_city
      
cities = [(-1, 5), (1, -1), (0, 1), (4, 6), (-1, -2), (4, 3)]
target = (1, 1)
K = 3
distances = ["Euclidean","Chebyshev", "Manhattan" ]

for distance in distances :
    city_distances = closest_cities(target,cities,K,distance)
    print('{distance} Distance'.format(distance=distance).center(30,'-'))
    print('The {} closest cities to {} are:'.format(K,target))
    for i in range (K):
        print(cities[city_distances[i][0]], end=' ')
    print('\\n')



