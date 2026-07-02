import time
import random

# Traffic lanes
lanes = {
    "North": 0,
    "South": 0,
    "East": 0,
    "West": 0
}

def generate_traffic():
    """Generate random vehicle counts"""
    for lane in lanes:
        lanes[lane] = random.randint(0, 50)

def display_traffic():
    print("\nCurrent Vehicle Density")
    print("-" * 30)
    for lane, count in lanes.items():
        print(f"{lane}: {count} vehicles")

def choose_green_signal():
    """AI Logic: Select lane with maximum vehicles"""
    busiest_lane = max(lanes, key=lanes.get)
    return busiest_lane

def traffic_controller():
    cycle = 1

    while cycle <= 10:
        print(f"\n===== Traffic Cycle {cycle} =====")

        generate_traffic()
        display_traffic()

        green_lane = choose_green_signal()

        print("\nTraffic Signal Status")
        for lane in lanes:
            if lane == green_lane:
                print(f"{lane}: GREEN")
            else:
                print(f"{lane}: RED")

        print(f"\nAI Decision: Green signal assigned to {green_lane}")

        time.sleep(3)
        cycle += 1

print("SMART TRAFFIC LIGHT CONTROLLER")
traffic_controller()
