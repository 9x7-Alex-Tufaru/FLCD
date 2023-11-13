from FA import FA


def readFAFromFile():
    file = open("FA.in", 'r')
    lines = [line.strip() for line in file.readlines()]
    initial_state = lines[0]
    final_states = lines[1].split()
    transitions = dict()
    states = []
    alphabet = []
    is_deterministic = True
    for i in range(2, len(lines)):
        source_state, letter, dest_state = lines[i].split(None, 2)
        if (source_state, letter) in transitions:
            is_deterministic = False
            transitions[(source_state, letter)].append(dest_state)
        else:
            transitions[(source_state, letter)] = [dest_state]
        if source_state not in states:
            states.append(source_state)
        if dest_state not in states:
            states.append(dest_state)
        if letter not in alphabet:
            alphabet.append(letter)
    fa = FA(states, alphabet, transitions, initial_state, final_states, is_deterministic)
    return fa


def menu():
    print("1. Display the set of states\n2. Display the alphabet\n3. Display the transitions\n"
          "4. Display the initial state\n5. Display the final states\n6. Verify sequence\n7. Exit")


if __name__ == '__main__':
    fa = readFAFromFile()
    while True:
        menu()
        option = input("Choose one: ")
        if option == "1":
            print(fa.printStates())
        elif option == "2":
            print(fa.printAlphabet())
        elif option == "3":
            print(fa.printTransitions())
        elif option == "4":
            print(fa.printInitialState())
        elif option == "5":
            print(fa.printFinalStates())
        elif option == "6":
            sequence = input("Enter the sequence to verify: ")
            print(fa.verifySequence(sequence))
        elif option == "7":
            break
        else:
            print("Invalid choice")
