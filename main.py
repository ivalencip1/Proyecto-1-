# Step 1: Create the table of all pair unmarked
def create_table(states):
    # Initialize the table with "*"
    table = [["*" for _ in range(states)] for _ in range(states)]
    
    for i in range(states):
        for j in range(states):
            if i == j:
                table[i][j] = i
            elif i > j:
                table[i][j] = "-" 
    return table


# Step 2: Mark the final and non-final states
def second_step(table, final_states):
    for i in range(len(table)):
        for j in range(i+1, len(table)):
            if table[i][i] in final_states and table[j][j] not in final_states or table[i][i] not in final_states and table[j][j] in final_states:
                table[j][i] = "✓"
    
    return table


# Step 3: Mark the remain pairs that are not equivalent
def third_step(table,transition_table,final_states):
    flag = True
    while flag:
        flag = False
        for i in range(len(table)):
            for j in range(i+1, len(table)):
                if table[j][i] == "-":
                    new_transition_table_i = []
                    new_transition_table_j = []
                    for row in transition_table:
                        if row[0] == table[i][i]:
                            new_transition_table_i.append(row[1:]) # Exclude the state itself
                        elif row[0] == table[j][j]:
                            new_transition_table_j.append(row[1:])  
                    
                    # iterate over the transitions
                    for transition_i, transition_j in zip(new_transition_table_i, new_transition_table_j): 
                        # iterate over the states of each transition
                        for ti, tj in zip(transition_i, transition_j): 
                            # The max and min function was implemented by ChatGPT to solve the case with the alphabet ['a']
                            if table[max(ti, tj)][min(ti, tj)] == "✓": 
                                table[j][i] = "✓"
                                flag = True
                                break
                        if flag:
                            break

    return table

def identify_equivalent_pairs(table):
    equivalent_pairs = []
    for i in range(len(table)):
        for j in range(i+1, len(table)):
            if table[j][i] == "-":
                equivalent_pairs.append("(" + str(table[i][i]) + ", " + str(table[j][j]) + ")")
    print(" ".join(map(str, equivalent_pairs)))

def minimization_algorithm(cases):
    for i in range(cases):

        states = int(input())
        alphabet = list(input().split())
        final_states = list(map(int, input().split()))
        transition_table = [[int(x) for x in input().split()] for _ in range(states)]

        table = create_table(states)
        second_step(table, final_states)
        third_step(table, transition_table, final_states)
        identify_equivalent_pairs(table)



def main():
    cases = int(input())

    minimization_algorithm(cases)

if __name__ == "__main__":
    main()