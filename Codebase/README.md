# Bus Route Management System

A console program in Python 3 that stores a bus network and finds the route with the fewest stops between two stops, along with the distance and fare.

**Project:** PS No. 70, B.Tech CSE, First Semester

**University:** Rungta International Skills University

**Student:** Atul Kumar Sahu (RU-26-02275)

## Features

- Stores the bus network as a dictionary of dictionaries (stop -> neighbours -> distance in km)
- Shows all stops
- Shows the direct connections of a chosen stop
- Finds the route with the fewest stops using BFS
- Shows number of stops, total distance and fare (Rs. 1.50 per km)
- Handles unknown stops and stops with no route

## Concepts used

Lists, dictionaries, loops, functions and graph basics (BFS).

## How to run

1. Install Python 3.
2. Download `bus_route.py`.
3. Run it from the console:

```
python bus_route.py
```

## Menu

```
1. Show all stops
2. Show connections
3. Find route
4. Exit
```

## Example

```
From: Bhilai
To: Bilaspur
Route: Bhilai -> Raipur -> Bilaspur
Stops: 3 | Distance: 140 km | Fare: Rs. 210.00
```

## Files

- `bus_route.py`: the program
- `Bus_Route_Management_System_Project_Report.pdf`: the project report with test cases and screenshots
