

def next_state(is_alive, num_neightbouts_alive):
    if num_neightbouts_alive < 2:
        return 0
    if is_alive == 1:
        if num_neightbouts_alive in [2, 3]:
            return 1
        elif num_neightbouts_alive > 3:
            return 0

    return is_alive
