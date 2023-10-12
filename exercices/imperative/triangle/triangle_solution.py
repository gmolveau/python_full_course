def print_triangle(n: int) -> None:
    if n < 1:
        raise ValueError("n should be positive")
    for i in range(1, n + 1):
        print("#" * i)


print_triangle(4)

"""
#
##
###
####
"""
