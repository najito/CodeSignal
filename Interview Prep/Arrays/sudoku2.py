def sudoku2(grid):
    seen = sum(
        (
            [(i, ch), (ch, j), (i // 3, ch, j // 3)]
            for i, r in enumerate(grid)
            for j, ch in enumerate(r)
            if ch != "."
        ),
        [],
    )
    return len(seen) == len(set(seen))