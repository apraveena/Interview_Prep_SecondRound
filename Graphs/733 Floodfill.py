def flood_fill_bfs(pixel_row, pixel_column, new_color, image):
    """
    Args:
     pixel_row(int32)
     pixel_column(int32)
     new_color(int32)
     image(list_list_int32)
    Returns:
     list_list_int32
    """
    from collections import deque
    if not len(image) or not len(image[0]):
        return image

    if image[pixel_row][pixel_column] == new_color:
        return image

    def get_neighbors_with_same_color(x, y):
        rows = [0, -1, 0, 1]
        cols = [1, 0, -1, 0]
        results = []
        for i in range(len(rows)):
            row_val = x + rows[i]
            col_val = y + cols[i]
            if row_val >= 0 and row_val < len(image) \
                    and col_val >= 0 and col_val < len(image[0]) \
                    and image[row_val][col_val] == old_color:
                results.append((row_val, col_val))

        return results

    old_color = image[pixel_row][pixel_column]
    q = deque()
    q.append((pixel_row, pixel_column))
    while q:
        curr_row, curr_col = q.pop()
        image[curr_row][curr_col] = new_color
        for nei in get_neighbors_with_same_color(curr_row, curr_col):
            q.append(nei)

    return image


def flood_fill_dfs(pixel_row, pixel_column, new_color, image):
    """
    Args:
     pixel_row(int32)
     pixel_column(int32)
     new_color(int32)
     image(list_list_int32)
    Returns:
     list_list_int32
    """
    if not len(image) or not len(image[0]):
        return image

    if image[pixel_row][pixel_column] == new_color:
        return image

    old_color = image[pixel_row][pixel_column]

    def get_neighbors_with_same_color(x, y):
        rows = [0, -1, 0, 1]
        cols = [1, 0, -1, 0]
        results = []
        for i in range(len(rows)):
            row_val = x + rows[i]
            col_val = y + cols[i]
            if row_val >= 0 and row_val < len(image) \
                    and col_val >= 0 and col_val < len(image[0]) \
                    and image[row_val][col_val] == old_color:
                results.append((row_val, col_val))

        return results

    def dfs(x, y):
        image[x][y] = new_color
        for r, c in get_neighbors_with_same_color(x, y):
            dfs(r, c)

    dfs(pixel_row, pixel_column)
    return image



