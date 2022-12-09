import numpy as np

def is_visible(
    tree_height: int,
    tree_line_heights: np.array
) -> bool:
    try:
        return tree_height > tree_line_heights.max()
    except ValueError:
        return True

def compute_score(
    tree_height: int,
    tree_line_heights: np.array
) -> int:
    count = 0
    for h in tree_line_heights:
        count += 1
        if tree_height <= h:
            break
    return count

with open('puzzle8_input') as input:
    trees_matrix = np.array(
        [ [ int(column) for column in row ] for row in input.read().splitlines() ]
    )
    # i_length, j_length = trees_matrix.shape
    visible_count = 0
    max_score = 0
    for i, row in enumerate(trees_matrix):
        for j, height in enumerate(row):
            right_line = trees_matrix[i,j+1:] # returns empty array when j+1 > j_length
            left_line = trees_matrix[i,:j] if j - 1 >= 0 else np.array([])
            bottom_col = trees_matrix[i+1:,j] # returns empty array when i+1 > i_length
            upper_col = trees_matrix[:i,j] if i - 1 >= 0 else np.array([])
            if (
                is_visible(height, right_line)
                or is_visible(height, left_line)
                or is_visible(height, bottom_col)
                or is_visible(height, upper_col)
            ):
                visible_count += 1
            scenic_score = (
                compute_score(height, right_line)
                * compute_score(height, np.flip(left_line))
                * compute_score(height, bottom_col)
                * compute_score(height, np.flip(upper_col))
            )
            if scenic_score > max_score:
                max_score = scenic_score

print(visible_count)
print(max_score)

