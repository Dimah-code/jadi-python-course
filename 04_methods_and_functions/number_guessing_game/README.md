## Number Guessing Game

A simple Python console game where you try to guess a randomly chosen number.
You can choose between three difficulty levels, each with its own score, range, and hint limit.

### How to Play

#### 1.Run the program:
```bash
python guess_game.py
```

#### 2.Choose a difficulty level:

1. Easy: Range 1–64, Score 500, Hints 3

2. Normal: Range 1–128, Score 1000, Hints 5

3. Hard: Range 1–256, Score 2000, Hints 7

The game will think of a random number — your goal is to guess it!
Each wrong guess costs 50 points.

You can ask for a hint, but it will:

Use up one of your remaining hints.

Deduct 20 points from your score.

Tell you whether your guess is smaller or larger than the secret number.

The game ends when:

You guess the number correctly

Or your score drops below 200

### Example Output:
```bash
Choose difficulty level
1. easy (1 <= x <= 64, score: 500)
2. normal (1<= x <= 128, score: 1000)
3. hard (1<= x <= 256, score: 2000)
Enter 1, 2 or 3 1
Easy mode:
Score: 500, hints: 3, range: 1 <= 64
I make a random number in my mind can you guess that? :)
Guess a number between 1 and 64: 30
Nah! It isn't my number
Do you need a hint? (You have 3) (y/n) y
HINT!!!: 30 < random number
```

### Features:

- Adjustable difficulty levels

- Scoring and penalty system

- Hint mechanic for guided guessing

- Simple and interactive command-line interface