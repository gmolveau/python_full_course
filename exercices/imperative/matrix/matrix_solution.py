def print_matrix(n1: int, n2: int) -> None:
    if not 0 <= n1 <= 9:
        raise ValueError("n1 should be between 0 and 9")
    if not 0 <= n2 <= 9:
        raise ValueError("n2 should be between 0 and 9")
    for i in range(10):
        for j in range(10):
            if i == n2 or j == n1:
                print("**", end=" ")
            else:
                print(f"{i}{j}", end=" ")
        print()


print_matrix(n1=3, n2=6)
