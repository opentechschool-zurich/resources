# Collaborating with git

## Preparation

- Create two repositories with a README.md and [main.py](main.py).

## Preconditions

- All participants have git and a text editor installed on their machine.
- All participants have followed a basic introductory course on git
- All partipants have (rather) basic skills of Python
- The moderator has created two repositories for the exercises:
  - One that where everybody can push.
  - One that will managed through pull requests.
- Add the tasks below as tickets for each of the repositories.

# The exercise

- All participants create an account on the same Git platform (Github, Gitlab, ...)
- Each partipant clones the repository
- Each participant gets a different task (from the simplest to the most complicated):
  - Add the subtraction  
    `calculate(a, op, c)` should also perform subtractions.
  - Add multiplication and division  
    Extend `calculate(a, op, c)` to support multiplications and division. Add `assert` based tests.
  - Add `print_calculation(a, op, b)`  
    `print_calculation(a, op, b)` prints the calculation and the result (by using `calculate(a, op, b)`):  
    `print_calculation(3, '+', 2)` prints `3 + 2 = 5`.
  - Add user input  
    Perform calculations typed by the user, until an empty line is entered
  - Add `calculate_list([3, '+', 2, '-', 1])`:
    - It uses `calculation(a, op, b)`.  
    - It does not respect the operators priorities.
- In a first round:
  - all the participants get write rights to the same repository.
  - they all push (and pull) to the same repository as soon as they are over with the task.
  - they will probably have to learn about `git stash` and resolving the conflicts.
- In a second round:
  - All the participants write pull requests
  - The pull requests are accepted when everybody is ready (and the conflicts worked out together)
