
def carFleetFunctionality(target, position, speed):
    if not position:
        return 0
        
    pairs = [(p, s) for p, s in zip(position, speed)]
    pairs.sort(reverse=True)
    
    carFleets = 1
    if len(pairs) == 1:
        return 1
        
    prevTime = (target - pairs[0][0]) / pairs[0][1]  # time for first car closest to target
    for i in range(1, len(pairs)):
        currCar = pairs[i]
        currTime = (target - currCar[0]) / currCar[1]
        if currTime > prevTime:
            prevTime = currTime
            carFleets += 1
    return carFleets

def main(target, position, speed):
    result = carFleetFunctionality(target, position, speed)
    print(f"Target: {target}")
    print(f"Positions: {position}")
    print(f"Speeds: {speed}")
    print(f"Number of car fleets: {result}")
    
    # Show the calculation process
    pairs = [(p, s) for p, s in zip(position, speed)]
    pairs.sort(reverse=True)
    
    print("\nCar analysis (sorted by position, closest to target first):")
    for i, (pos, spd) in enumerate(pairs):
        time_to_target = (target - pos) / spd
        print(f"  Car {i+1}: Position {pos}, Speed {spd}, Time to reach target: {time_to_target:.2f}")
    
    print("\nFleet formation:")
    if len(pairs) == 0:
        return
    
    fleets = 1
    fleet_time = (target - pairs[0][0]) / pairs[0][1]
    print(f"  Fleet 1: Car at position {pairs[0][0]} (time: {fleet_time:.2f})")
    
    for i in range(1, len(pairs)):
        pos, spd = pairs[i]
        time_to_target = (target - pos) / spd
        
        if time_to_target > fleet_time:
            fleets += 1
            fleet_time = time_to_target
            print(f"  Fleet {fleets}: Car at position {pos} (time: {time_to_target:.2f}) - forms new fleet")
        else:
            print(f"  Car at position {pos} (time: {time_to_target:.2f}) - joins previous fleet")

# EXAMPLE
# main(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3])
# main(10, [3], [3])
