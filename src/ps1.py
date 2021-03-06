###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_animals(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated animal name, weight pairs, and return a
    dictionary containing animal names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of animal name (string), weight (int) pairs
    """

    animal_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        animal_dict[line_data[0]] = int(line_data[1])
    return animal_dict


# Problem 1
def greedy_animal_transport(animals,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of animals that attempts to
    minimize the number of spaceship trips needed to transport all the animals. The
    returned allocation of animals may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another animal, add the largest animal that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining animals

    Does not mutate the given dictionary of animals.

    Parameters:
    animals - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of animals
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    pass


# Problem 2
def brute_force_animal_transport(animals,limit=10):
    """
    Finds the allocation of animals that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the animals can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of animals.

    Parameters:
    animals - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of animals
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    pass

        
# Problem 3
def compare_animal_transport_algorithms():
    """
    Using the data from ps1_animal_data.txt and the specified weight limit, run your
    greedy_animal_transport and brute_force_animal_transport functions here. Use the
    default weight limits of 10 for both greedy_animal_transport and
    brute_force_animal_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

animals = load_animals("ps1_animal_data.txt")
limit=10
print(animals)

print(greedy_animal_transport(animals, limit))
print(brute_force_animal_transport(animals, limit))


