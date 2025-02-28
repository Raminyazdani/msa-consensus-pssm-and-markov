import numpy as np

# Define the transition matrix

#TODO

#Hint: You can use np.array to define the transition matrix
transitionMatrix = np.array([[0.5,0.3,0.2],[0.4,0.4,0.2],[0.1,0.4,0.5]])

# Define the states
states = ['Berlin', 'Munich', 'Hamburg']

# Simulate the traveler's journey
def simulate_markov_chain(transition_matrix, states, start_state, steps=100):
    """
    Simulates a Markov chain.
    
    Parameters:
        transition_matrix (np.ndarray): Transition probabilities.
        states (list): List of states.
        start_state (str): Starting state.
        steps (int): Number of steps to simulate.
        
    Returns:
        list: Sequence of states visited.
    """
    sequence = []

    #TODO
    while steps > 0:
        sequence.append(start_state)
        # get the next state with the transition matrix possibilities
        start_state = np.random.choice(states, p=transition_matrix[states.index(start_state)])
        steps -= 1
    return sequence

# Run the simulation
#TODO
seq = simulate_markov_chain(transitionMatrix,states,"Berlin")

# Print the results

#TODO
print("total number of cities visited:",len(seq))

print("Time  in each city visited:")
print("Berlin:", seq.count("Berlin"))
print("Munich:", seq.count("Munich"))
print("Hamburg:", seq.count("Hamburg"))