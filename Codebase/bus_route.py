bus_network = {
    "Durg": {"Bhilai": 10, "Raipur": 40, "Rajnandgaon": 45},
    "Bhilai": {"Durg": 10, "Raipur": 30},
    "Raipur": {"Bhilai": 30, "Bilaspur": 110, "Dhamtari": 80, "Durg": 40},
    "Bilaspur": {"Raipur": 110},
    "Dhamtari": {"Raipur": 80},
    "Rajnandgaon": {"Durg": 45},
    "Jagdalpur": {"Kondagaon": 75},
    "Kondagaon": {"Jagdalpur": 75},
}

fare_per_km = 1.50


def show_connections(stop):
    if stop not in bus_network:
        print("Stop '" + stop + "' not found.")
    else:
        text = ""
        for neighbour in bus_network[stop]:
            distance = bus_network[stop][neighbour]
            item = neighbour + " (" + str(distance) + " km)"
            if text == "":
                text = item
            else:
                text = text + ", " + item
        print(stop + " connects to: " + text)

def find_route(source, destination):
    queue = [[source]]
    visited = [source]
    answer = None

    while len(queue) > 0 and answer == None:
        path = queue.pop(0)
        current = path[len(path) - 1]

        if current == destination:
            answer = path
        else:
            for neighbour in bus_network[current]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(path + [neighbour])

    return answer


def show_route(source, destination):
    if source not in bus_network:
        print("Stop '" + source + "' not found.")
    elif destination not in bus_network:
        print("Stop '" + destination + "' not found.")
    elif source == destination:
        print("Source and destination are the same. Distance: 0 km.")
        print("Fare: Rs. 0.00")
    else:
        path = find_route(source, destination)

        if path == None:
            print("No route available between " + source + " and " + destination + ".")
        else:
            total_distance = 0
            for i in range(len(path) - 1):
                total_distance = total_distance + bus_network[path[i]][path[i + 1]]

            fare = total_distance * fare_per_km

            route_text = ""
            for stop in path:
                if route_text == "":
                    route_text = stop
                else:
                    route_text = route_text + " -> " + stop

            print("Route: " + route_text)
            print("Stops:", len(path), "| Distance:", total_distance, "km | Fare: Rs.", format(fare, ".2f"))

while True:
    print("--- Bus Route Management System ---")
    print("1. Show all stops")
    print("2. Show connections")
    print("3. Find route")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        for stop in bus_network:
            print(stop)
    elif choice == "2":
        stop = input("Stop: ").title()
        show_connections(stop)
    elif choice == "3":
        source = input("From: ").title()
        destination = input("To: ").title()
        show_route(source, destination)
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice")
        # print("No Such option are available")