def find_cube_pairs(target):
    # Added a colon (:) at the end of the function definition.

    solutions = []  
    max_num = round(target ** (1/3))  
    # Fixed exponentiation from '***' to '**' and corrected 'targ' to 'target'.

    for a in range(1, max_num + 1):  
        # Changed 'ranges' to 'range' and added a colon at the end.
        
        for b in range(a, max_num + 1):  
            # Same fix for 'ranges' to 'range' and added a colon.

            if a**3 + b**3 == target:
                # Fixed incorrect exponentiation from '***' to '**' and corrected 'targ' to 'target'.
                
                solutions.append((a, b))  
                # Changed 'sol' to 'solutions' (to match the initialized list).

    return solutions  
    # Corrected 'return sol' to 'return solutions' to return the correct list.

# Function call
pairs = find_cube_pairs(1729)  
# Removed the trailing comma to avoid creating a tuple instead of a list.

print("Valid cube pairs for 1729:")  
# Changed 'printf' to 'print' since Python does not have 'printf'.

for a, b in pairs:  
    # Changed 'pair' to 'pairs' (corrected iteration variable) and added a colon.

    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729")  
    # Changed 'printf' to 'print'.
    # Fixed the exponentiation formatting '{a**2} + {b**2}' to '{a**3} + {b**3}'.
    # Corrected '1728' to '1729' to match the target number.
