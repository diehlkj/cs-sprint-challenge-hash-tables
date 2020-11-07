#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    order = {}
    route = []
    for ticket in tickets:
        order[ticket.source] = ticket.destination

    
    source = order["NONE"]
    
    for i in range(0, length):
        route.append(source)
        source = order[source]
    
    # for source in order:
        # print(source, order[source])
    print(route)
    return route
