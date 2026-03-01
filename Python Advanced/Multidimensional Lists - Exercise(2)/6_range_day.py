size = 5
matrix = []
shooter_pos = None
targets_total = 0
hit_targets = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

# Read field
for r in range(size):
    row = input().split()
    matrix.append(row)
    for c in range(size):
        if row[c] == "A":
            shooter_pos = (r, c)
        elif row[c] == "x":
            targets_total += 1

def in_bounds(r, c):
    return 0 <= r < size and 0 <= c < size

def move(direction, steps):
    global shooter_pos
    dr, dc = directions[direction]
    r, c = shooter_pos
    nr = r + dr * steps
    nc = c + dc * steps

    # validate destination only
    if in_bounds(nr, nc) and matrix[nr][nc] == ".":
        shooter_pos = (nr, nc)

def shoot(direction):
    dr, dc = directions[direction]
    r, c = shooter_pos
    r += dr
    c += dc

    while in_bounds(r, c):
        if matrix[r][c] == "x":
            matrix[r][c] = "."
            return [r, c]
        r += dr
        c += dc

    return None

commands = int(input())
targets_hit = 0

for _ in range(commands):
    parts = input().split()
    if parts[0] == "move":
        move(parts[1], int(parts[2]))
    else:  # shoot
        pos = shoot(parts[1])
        if pos:
            hit_targets.append(pos)
            targets_hit += 1
            if targets_hit == targets_total:
                print(f"Training completed! All {targets_total} targets hit.")
                break
else:
    print(f"Training not completed! {targets_total - targets_hit} targets left.")

for p in hit_targets:
    print(p)