def can_complete_circuit(water, cost):
    if sum(water) < sum(cost):
        return -1
current_surplus = 0
start_index = 0
n = len(water)
    for i in range(n):
        current_surplus += water[i] - cost[i]
    if current_surplus < 0:
        current_surplus = 0
        start_index = i + 1
return start_index
