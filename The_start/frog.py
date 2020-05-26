# There are N stones, numbered 1,2,…,N.
#
# There is a frog who is initially on Stone 1.
#
# Frog on Stone i can jump to Stone i+1 or Stone i+2
# He will repeat the following action some number of times to reach Stone N
#
# Each stone has given value.
# Find the minimum possible total cost incurred before the frog reaches Stone N.


# input: number of stones
#        value of each stone
# Example: 4 stones given
#          start  2  3  fin
#              10 30 40 20


values = [10, 30, 40, 20]
# values = [10, 10]
# values = [30, 10, 60, 10, 60, 50]

graph = {}
for stone_number in range(len(values)):
    # shold work for all inputs
    graph[str(stone_number)] = {}
    # should stop here on last input
    if stone_number + 1 != len(values):
        graph[str(stone_number)][str(stone_number + 1)] = abs(
            values[stone_number + 1] - values[stone_number]
        )
        # should stop here if this is the stone before last one
        if stone_number + 2 != len(values):
            graph[str(stone_number)][str(stone_number + 2)] = abs(
                values[stone_number + 2] - values[stone_number]
            )


infinity = float("inf")
costs = {}
for stone_number in range(len(values)):
    # it should stop here on the last stone
    if stone_number + 1 == len(values):
        break
    costs[str(stone_number + 1)] = abs(values[stone_number + 1] - values[0])
if len(values) > 2:
    costs[str(len(values) - 1)] = infinity


parents = {}
parents["1"] = "0"
parents["2"] = "0"
parents[str(len(values))] = None

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print(
    "To reach the stone number:\n"
    + str(len(values))
    + "\n"
    + "Minimum possible cost will be:\n"
    + str(costs[str(len(values) - 1)])
)
