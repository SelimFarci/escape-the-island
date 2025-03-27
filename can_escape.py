import argparse
from pathlib import Path
from collections import deque


class Map:
    from pathlib import Path
from collections import deque


class Map:
    def __init__(self):
        # 💬 Message d'accueil
        print("🌴 Welcome to *Escape the Island*!")
        print("📜 To begin your adventure, please enter the path to your map file.")
        print("💡 Tip: You can right-click your map file and select 'Copy relative path' to paste it here!")
        print("👉 Example: maps/maps/01_vanishing_island.map")

        # Demande à l'utilisateur de saisir le chemin de la map
        map_input = input("🗺️ Enter map path: ").strip()
        map_file = Path(map_input)

        # Vérifie si le fichier existe
        if not map_file.exists():
            print("❌ Map file not found. Please check the path and try again.")
            exit(1)

        # Lecture de la carte
        with open(map_file, "r") as f:
            lines = f.read().strip().splitlines()

        self.N = int(lines[0].split()[0])
        print(f"N = {self.N}, the map is {self.N}x{self.N}!")

        self.grid = [
            list(map(int, line.strip().split()))
            for line in lines[1:self.N+1]
        ]

        print("Map matrix loaded:")
        for row in self.grid:
            print("  ", row)

        cx = self.N / 2 + 0.5
        cy = self.N / 2 + 0.5
        ix = int(cx - 1/2)
        iy = int(cy - 1/2)

        altitude_centre = self.grid[ix][iy]
        print(f"The center of the map is at: ({cx}, {cy}) and its altitude is {altitude_centre}m.")

        self.start = (ix, iy)

    def can_escape(self) -> bool:
        from collections import deque  # pour la file d'attente (BFS)

        # Position de départ (centre)
        x, y = self.start
        current_alt = self.grid[x][y]

        # Affichage initial
        print(f"Oh no... I can't find the way out 🧭 My altimeter shows {current_alt} meters.")
        print("Let's try to reach the ocean from my central position... 🌊")


        # Initialisation de la file d'exploration et des cases visitées
        visited = set()
        queue = deque()
        queue.append((x, y))
        visited.add((x, y))

        # Parcours en largeur
        while queue:
            x, y = queue.popleft()
            current_alt = self.grid[x][y]

            # Vérifie si on atteint une case océan sur les bords
            if (x == 0 or x == self.N - 1 or y == 0 or y == self.N - 1) and current_alt == 0:
                print(f"🌊 Victory! I reached the ocean at position ({x}, {y})!")
                return True

            # Exploration des 4 directions
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < self.N and 0 <= ny < self.N:
                    if (nx, ny) not in visited:
                        neighbor_alt = self.grid[nx][ny]

                        # Autoriser le mouvement si la différence d'altitude est ≤ 1
                        if abs(neighbor_alt - current_alt) <= 1:
                            print(f"🧭 I'm at ({x}, {y}), altitude {current_alt}m. Trying to reach ({nx}, {ny}) at {neighbor_alt}m...")
                            queue.append((nx, ny))
                            visited.add((nx, ny))

        # Aucun chemin possible
        print("🛑 No path to the ocean was found. You're stuck in the jungle.")
        return False



if __name__ == "__main__":
    island_map = Map()
    
    if island_map.can_escape():
        print("✅ Yes! You reached the beach... Suddenly, you spot a boat approaching on the horizon 🚤✨")
        print("You wave your arms, shouting with hope — they're coming to rescue you!")
        print("The long journey is over. You're going home... 🌊🏝️🏠")
    else:
        print("❌ No... you're stuck here. Maybe write 'SOS' with palm leaves... 🆘🌴")


