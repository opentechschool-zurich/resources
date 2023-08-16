# Pick a random item from a list without using random()

Topics:

- How to create a very simple random generator?
  - How good is an implementation based on the current second? (hint: with 4 items, 5 items, 6 items, 7 items...)
- What does it mean, that a random number is good enough?
  - Distribution
  - Predictability
  - Reproductibility (pseudo-randoms)
- When should we worry if a random number is good enough?
- How good is this Python implementation?

  ```py
  import random
  
  foo = ['a', 'b', 'c', 'd', 'e']
  print(random.choice(foo))
  ```
