class State:
    def __init__(self, name):
        self.name = name
        self.transitions = {}

    def add_transition(self, input_symbol, next_state, output_symbol=None):

        self.transitions[input_symbol] = (next_state, output_symbol)

    def next_state(self, input_symbol):

        return self.transitions.get(input_symbol, (None, None))


class MooreMachine:
    def __init__(self):
        self.states = {}
        self.current_state = None

    def add_state(self, state_name):

        state = State(state_name)
        self.states[state_name] = state
        return state

    def set_initial_state(self, state_name):

        self.current_state = self.states.get(state_name)

    def process_input(self, input_symbol):

        if self.current_state:
            next_state_name, _ = self.current_state.next_state(input_symbol)
            if next_state_name:
                self.current_state = self.states.get(next_state_name)

    def get_current_state(self):

        return self.current_state.name if self.current_state else None


if __name__ == "__main__":
    # Moore
    moore = MooreMachine()

    # Define states
    state_a = moore.add_state("A")
    state_b = moore.add_state("B")
    state_c = moore.add_state("C")

    # Add transitions
    state_a.add_transition("0", "A")  # Stay in A on input 0
    state_a.add_transition("1", "B")  # Go to B on input 1

    state_b.add_transition("0", "A")  # Return to A on input 0
    state_b.add_transition("1", "C")  # Go to C on input 1

    state_c.add_transition("0", "C")  # Stay in C on input 0
    state_c.add_transition("1", "A")  # Return to A on input 1

    # Set initial state
    moore.set_initial_state("A")

    # Process inputs
    inputs = "101010"
    print("Initial State:", moore.get_current_state())
    for symbol in inputs:
        moore.process_input(symbol)
        print(f"After input {symbol}: {moore.get_current_state()}")
