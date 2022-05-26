'''Assignment 2

This assignment covers your proficiency with Python's data structures.
It engages your ability to manipulate and evaluate data stored in lists and dictionaries.
'''
import importlib
sample_data = importlib.import_module("assignment-2-sample-data")
def relationship_status(from_member, to_member, social_graph):
    '''
    Item 1.
    Relationship Status. 10 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-2-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Write your code below this line
    if to_member in social_graph[from_member]["following"] and \
        from_member in social_graph[to_member]["following"]:
        return "friends"
    elif to_member in social_graph[from_member]["following"]:
        return "follower"
    elif from_member in social_graph[to_member]["following"]:
        return "followed by"
    else:
        return "no relationship"


def tic_tac_toe(board):
    '''
    Item 2.
    Tic Tac Toe. 10 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-2-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Write your code below this line
    # Check rows
    for idx, row in enumerate(board):
        # Use set to get all the unique values
        # If the number of unique values is only 1 this means that the all the columns
        # in that row contains the unique symbol
        if len(set(row))==1:
            return list(set(row))[0] #Get the first element in the set
    # Check columns
    for col_idx in range(len(board)):
        column_values = []
        for row in board:
            column_values.append(row[col_idx])
        if len(set(column_values))==1:
            return list(set(column_values))[0] #Get the first element in the set

    # Check diagonals
    down_diagonal_pointer = 0
    up_diagonal_pointer = len(board)-1
    down_diagonal_values = []
    up_diagonal_values = []
    for idx, row in enumerate(board):
        down_diagonal_values.append(row[down_diagonal_pointer])
        up_diagonal_values.append(row[up_diagonal_pointer])
        down_diagonal_pointer+=1
        up_diagonal_pointer-=1


    if len(set(down_diagonal_values)) == 1:
        return list(set(down_diagonal_values))[0]
    if len(set(up_diagonal_values))==1:
        return list(set(up_diagonal_values))[0]

    return "NO WINNER"




def eta(first_stop, second_stop, route_map):
    '''
    Item 3.
    ETA. 10 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "assignment-2-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Write your code below this line

    time = 0
    first_stop_passed = False
    for route in route_map:
        if first_stop_passed:
            time += route_map[route]["travel_time_mins"]

        if route[0]==first_stop:
            time+= route_map[route]["travel_time_mins"]
            first_stop_passed =True

        # Destination reached without going in circle
        if route[1]==second_stop and first_stop_passed:
            return time

    for route in route_map:
        if route[1]==second_stop:
            return time+route_map[route]["travel_time_mins"]
        else:
            time+= route_map[route]["travel_time_mins"]

