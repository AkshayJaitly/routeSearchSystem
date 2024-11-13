from collections import deque

class Order:
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination

    def get_origin(self):
        return self.origin

    def get_destination(self):
        return self.destination

class Network:
    def __init__(self):
        self.network = {}

    def add_route(self, origin, destination):
        if origin not in self.network:
            self.network[origin] = []
        if destination not in self.network[origin]:
            self.network[origin].append(destination)

    def get_network(self):
        return self.network

def can_route(order, network):
    if order.get_origin() == order.get_destination():
        return True

    visited = set()
    queue = deque([order.get_origin()])

    while queue:
        current = queue.popleft()
        if current == order.get_destination():
            return True

        for neighbor in network.get_network().get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return False

# Example usage
network = Network()
network.add_route("IND", "USA")
network.add_route("USA", "IND")
network.add_route("FRA", "CHI")
network.add_route("CHI", "IND")
network.add_route("HON", "USA")
network.add_route("IND", "CHI")

order = Order("FRA", "USA")
print(can_route(order, network))  # Output: True
