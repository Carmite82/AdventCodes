def safe_password(start: int, moves: list) -> tuple[int, int]:
    """
    Simulates movements on a safe's dial and counts how many times the dial is set to zero.
    
    Inputs: start, a non-negative integer representing the starting position of the safe's dial (0-99).
            moves, a list of tuples (direction, amount), where direction is 'L' or 'R' and amount is a non-negative integer.

    Preconditions: start and end are integers between 0 and 99, inclusive. 
                   direction is either 'L' (left) or 'R' (right), and amount is a non-negative integer.

    Outputs: tuple[int, int]:
                            - final_position: the dial's position after all moves (0-99)
                            - zero_count: the number of times the dial was set to zero during the moves

    Postconditions:
                    final_position is an integer between 0 and 99, inclusive
                    zero_count is a non-negative integer
                    zero_count is the number of times the dial was set to zero during the moves
    
    """

    zero_count = 0
    position = start

    for direction, amount in moves:
        if direction == 'L':
            position = (position - amount) % 100
        elif direction == 'R':
            position = (position + amount) % 100

        if position == 0:
            zero_count += 1

    return position, zero_count

print(safe_password(50, [('L', 50), ('R', 100), ('L', 100)])) # remember that input is starting position and moves, so start position in this case is 50!

# test cases
print(safe_password(0, [('L', 0), ('R', 0), ('L', 100)])) # starting at zero should not automatically count as a zero move
print(safe_password(50, [('R', 250), ('L', 350), ('R', 450)])) # moves bigger than 100 should wrap around correctly
print(safe_password(1, [('L', 1), ('R', 99), ('L', 100)])) # alternating wrap-around, forces the dial to wrap around zero repeatedly
print(safe_password(75, [])) # no moves should return the starting position and zero count of 0
print(safe_password(10, [('R', 0), ('L', 0)])) # negative behaviour with zero moves should not change the position or count as a zero move
print(safe_password(1, [('L', 1), ('R', 100), ('L', 100)])) # hitting zero exactly three times should count correctly







