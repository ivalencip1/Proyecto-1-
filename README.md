# DFA Minimization Algorithm

# Description

This project is an algorithm provided by "Automata and Computability, Kozen, 1997".

Given a Deterministic Finite Automaton with no inaccessible states, the algorithm returns the states that are equivalent.
Therefore, such states can be collapsed and we shall obtain a minimized automaton.

# Programming Language

- Python 3.12+

# Running Instructions

To run the algorithm, it must be the following input:
1. Number of cases (How many DFA you want to test at the same time)
2. Number of states
3. Alphabet characters in order
4. Final states
5. Transition rows (each row must start with the state and continue with the states to which it moves according to the order and characters used and written in step 3)

We'll show you some examples of the use:

**Example**
```
4
6
a b
1 2 5
0 1 2 
1 3 4
2 4 3
3 5 5
4 5 5
5 5 5 
6
a b
3 4 5
0 1 2
1 3 4
2 4 3
3 5 5
4 5 5
5 5 5
6
a
1 4
0 1
1 2
2 3
3 4
4 5
5 0
4
a b
0 1
0 1 2
1 1 2
2 3 1
3 3 3
```
# Output
```
(1, 2) (3, 4)
(1, 2) (3, 4) (3, 5) (4, 5)
(0, 3) (1, 4) (2, 5)
(0, 1)
```

# Authors
- Isabela Valencia Pino

# Class Number
 C2566-SI2002-5465
 