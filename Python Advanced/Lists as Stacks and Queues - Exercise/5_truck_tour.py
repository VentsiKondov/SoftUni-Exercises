from collections import deque

number_of_pumps = int(input())
gas_stations = deque([[int(x) for x in input().split()] for _ in range(number_of_pumps)])

start_pos = 0
stops = 0
i=0

while stops < number_of_pumps:
    full_petrol = 0
    for i in range(number_of_pumps):
        petrol = gas_stations[i][0]
        distance = gas_stations[i][1]
        full_petrol += petrol
        if full_petrol < distance:
            gas_stations.rotate(-1)
            start_pos += 1
            stops = 0
            break
        full_petrol -= distance
        stops += 1


print(start_pos)

