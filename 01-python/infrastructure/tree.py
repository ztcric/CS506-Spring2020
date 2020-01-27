def draw_tree(height = 5):
    """
        Draw a tree
        Parameters:
        height (int): trunk height of the tree
        Returns: void
    """
    for level in range(2*height):
        """Drawing tree crown"""
        for _ in range(2*height-level):
            print(" ", end="")
        for _ in range(level):
            print("--", end="")
        print()

    for level in range(height):
        """Drawing tree trunk"""
        for _ in range(2*height - 2):
            print(" ",end="")
        print("||||")
    return

