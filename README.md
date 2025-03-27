# Escape the Island - Adventure Game in Python

## Project Overview

"Escape the Island" is an adventure game where you must escape an island by navigating through an N x N terrain map. Starting from the center of the island, you will explore the map to find a path leading to the ocean, located along the borders of the map. The challenge is to reach the ocean while respecting elevation differences that dictate whether movement between adjacent squares is possible.

The game utilizes a **Breadth-First Search (BFS)** algorithm to explore the map and determine whether an escape route to the ocean exists. The ocean is represented by an elevation of 0 and surrounds the island, making it the target destination. You can only move to adjacent squares if the elevation difference is at most 1.

## Game Flow

1. The user provides the path to a map file, which represents the island terrain.
2. The map is loaded, and the starting position is set at the center of the map.
3. The BFS algorithm is used to explore the map and check if a path to the ocean is possible.
4. If a valid path exists, the player "escapes" the island; otherwise, they are stuck.

## Problem Objective

You're dropped onto an island, starting at the very middle of an N by N terrain grid. You have a raft and a map showing the elevation of each square plot of land. The ocean at elevation 0 surrounds the island and lies all along the borders of the map.

You can move directly north, south, east, or west to an adjacent plot, provided the difference in elevation is at most one. Larger differences indicate steep terrain which cannot be traversed with your raft.

Your task is to determine if it's possible to reach the ocean and escape the island.

### Input / Output

#### Input

You are given 10 files with different maps. The first line contains the size N of the map (N is odd). The next N lines contain N space-separated integers representing the elevation of each cell in the grid. The last line contains the expected answer (either "yes" or "no") to help with development. This last line should not be used in your solution.

#### Output

Your program should output "yes" if it's possible to reach the ocean, and "no" otherwise.

### Example Input:
5
0 0 0 0 0
0 1 1 0 0
0 1 1 1 0
0 0 1 1 0
0 0 0 0 0
yes

### Example output:

N = 5, the map is 5x5!
Map matrix loaded:
   [0, 0, 0, 0, 0]
   [0, 1, 1, 0, 0]
   [0, 1, 1, 1, 0]
   [0, 0, 1, 1, 0]
   [0, 0, 0, 0, 0]
The center of the map is at: (3.0, 3.0) and its altitude is 1m.
Oh no... I can't find the way out 🧭 My altimeter shows 1 meters.
Let's try to reach the ocean from my central position... 🌊
🧭 I'm at (2, 2), altitude 1m. Trying to reach (1, 2) at 1m...
🧭 I'm at (2, 2), altitude 1m. Trying to reach (3, 2) at 1m...
🧭 I'm at (2, 2), altitude 1m. Trying to reach (2, 1) at 1m...
🧭 I'm at (2, 2), altitude 1m. Trying to reach (2, 3) at 1m...
🧭 I'm at (1, 2), altitude 1m. Trying to reach (0, 2) at 0m...
🧭 I'm at (1, 2), altitude 1m. Trying to reach (1, 1) at 1m...
🧭 I'm at (1, 2), altitude 1m. Trying to reach (1, 3) at 0m...
🧭 I'm at (3, 2), altitude 1m. Trying to reach (4, 2) at 0m...
🧭 I'm at (3, 2), altitude 1m. Trying to reach (3, 1) at 0m...
🧭 I'm at (3, 2), altitude 1m. Trying to reach (3, 3) at 1m...
🧭 I'm at (2, 1), altitude 1m. Trying to reach (2, 0) at 0m...
🧭 I'm at (2, 3), altitude 1m. Trying to reach (2, 4) at 0m...
🌊 Victory! I reached the ocean at position (0, 2)!
✅ Yes! You reached the beach... Suddenly, you spot a boat approaching on the horizon 🚤✨
You wave your arms, shouting with hope — they're coming to rescue you!
The long journey is over. You're going home... 🌊🏝️🏠
