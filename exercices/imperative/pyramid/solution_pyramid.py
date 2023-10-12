def print_pyramid(height: int):
    """in the following example for height = 4, we see that
       *    > 3 spaces + 1 stone (+ 3 spaces optional)
      ***   > 2 spaces + 3 stones + (2 spaces optional)
     *****  > 1 space + 5 stones + (1 space optional)
    ******* > 0 space + 7 stones
    with current_height starting at 0
    we add 2 'stones' for each new line, so 2 * current_height + 1
    those stones have (height - current_height - 1) * spaces on the left
    """
    for current_height in range(height):
        stones = "*" * (2 * current_height + 1)
        space = " " * (height - current_height - 1)
        print(f"{space}{stones}{space}")


height = 4
print_pyramid(height)
