class FA:
    def __init__(self, states, alphabet, delta, initial_state, final_states, is_deterministic):
        self.states = states
        self.alphabet = alphabet
        self.delta = delta
        self.initial_state = initial_state
        self.final_states = final_states
        self.is_deterministic = is_deterministic

    def printStates(self):
        return str(self.states)

    def printAlphabet(self):
        return str(self.alphabet)

    def printTransitions(self):
        transitionsString = ""
        for key in self.delta:
            transitionsString += "(" + str(key[0]) + ", " + str(key[1]) + ") -> "
            for value in self.delta[key]:
                if self.delta[key].index(value) < len(self.delta[key]) - 1:
                    transitionsString += value + ", "
                else:
                    transitionsString += value + "\n"
        return transitionsString

    def printInitialState(self):
        return str(self.initial_state)

    def printFinalStates(self):
        return str(self.final_states[0]) if len(self.final_states) == 0 else str(self.final_states)

    def verifySequence(self, sequence):
        if not self.is_deterministic:
            return "The finite automata is nondeterministic"
        current_state = self.initial_state
        for letter in sequence:
            if (current_state, letter) in self.delta:
                current_state = self.delta[(current_state, letter)][0]
            else:
                return "The sequence " + sequence + " is not accepted by the FA"
        if current_state in self.final_states:
            return "The sequence " + sequence + " is accepted by the FA"
        else:
            return "The sequence " + sequence + " is not accepted by the FA"
