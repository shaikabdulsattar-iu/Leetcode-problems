from collections import deque
from typing import List


class Solution:

  def minMoves(self, classroom: List[str], energy: int) -> int:
    m, n = len(classroom), len(classroom[0])
    litter_map = {}
    sx, sy = 0, 0

    # Locate starting point and index all litter positions
    for r in range(m):
      for c in range(n):
        if classroom[r][c] == "S":
          sx, sy = r, c
        elif classroom[r][c] == "L":
          litter_map[(r, c)] = len(litter_map)

    target_mask = (1 << len(litter_map)) - 1
    if target_mask == 0:
      return 0

    # best_energy[r][c][mask] stores the maximum energy recorded for that state
    best_energy = [[[-1] * (1 << len(litter_map)) for _ in range(n)] for _ in range(m)]

    # Queue holds: (row, col, mask, current_energy, steps)
    queue = deque([(sx, sy, 0, energy, 0)])
    best_energy[sx][sy][0] = energy

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
      r, c, mask, e, steps = queue.popleft()

      # If we have no energy left to move out of the current cell, skip
      if e == 0:
        continue

      for dr, dc in directions:
        nr, nc = r + dr, c + dc

        # Check grid boundaries and obstacle
        if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != "X":
          ne = e - 1
          nmask = mask

          # Pick up litter if present
          if (nr, nc) in litter_map:
            nmask |= 1 << litter_map[(nr, nc)]

          # Check completion
          if nmask == target_mask:
            return steps + 1

          # Recharge at reset station
          if classroom[nr][nc] == "R":
            ne = energy

          # Prune if visited with higher or equal energy
          if ne > best_energy[nr][nc][nmask]:
            best_energy[nr][nc][nmask] = ne
            queue.append((nr, nc, nmask, ne, steps + 1))

    return -1