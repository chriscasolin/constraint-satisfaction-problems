#!/usr/bin/env python3

#   SEND
# + MORE
# ------
#  MONEY

class State():
    def __init__(self):
        self.letters = {
            'S': None,
            'E': None,
            'N': None,
            'D': None,
            'M': 1, # This is acceptable because we know it must be True
            # 'M': None,
            'O': None,
            'R': None,
            'Y': None
        }

    def is_valid(self):
        l = self.letters
        if None in l.values():
            # Still working out
            return True 
        
        if l['M'] == 0 or l['S'] == 0:
            return False
        
        if len(set(l.values())) != 8:
            return False
        
        x1 = l['D'] + l['E'] >= 10
        x2 = l['N'] + l['R'] + x1 >= 10
        x3 = l['E'] + l['O'] + x2 >= 10
        x4 = l['S'] + l['M'] + x3 >= 10

        return (
        l['D'] + l['E'] - 10 * x1 == l['Y'] and
        l['N'] + l['R'] + x1 - 10 * x2 == l['E'] and
        l['E'] + l['O'] + x2 - 10 * x3 == l['N'] and
        l['S'] + l['M'] + x3 - 10 * x4 == l['O'] and
        x4 == l['M']
    )

def solve(state):
    stack = [(state.letters.copy(), list(state.letters.keys()))]

    while stack:
        current_state, letters_left = stack.pop()
        state.letters = current_state
        if not letters_left:
            if state.is_valid():
                return state.letters
            continue

        letter = letters_left[0]
        for digit in range(10):
            if digit in current_state.values():
                continue
            current_state[letter] = digit
            stack.append((current_state.copy(), letters_left[1:]))
            current_state[letter] = None

    return None


initial_state = State()
solution = solve(initial_state)
print(solution)

print(' ', solution['S'], solution['E'], solution['N'], solution['D'], sep='')
print(' ', solution['M'], solution['O'], solution['R'], solution['E'], sep='')
print(solution['M'], solution['O'], solution['N'], solution['E'], solution['Y'], sep='')

