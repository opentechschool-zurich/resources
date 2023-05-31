from enum import Enum
from typing import Self, Optional
from random import choice

class GameResult(Enum):
  win = 1
  lose = 2
  draw = 3

class Move(Enum):
  rock = 1
  paper = 2
  scissor = 3

  @staticmethod
  def fromInput(s: str) -> Optional[Self]: # from is a keyword in python...
    match s.lower():
      case 'r':
        return Move.rock
      case 'p':
        return Move.paper
      case 's':
        return Move.scissors
      case _:
        return None

  def play(self, other: Self) -> GameResult:
    if self == other:
      return GameResult.draw
    match (self, other):
      case (paper, rock):
        return GameResult.win
      case (scissors, paper):
        return GameResult.win
      case (rock, scissor):
        return GameResult.win
      case _:
        return GameResult.lose

  def emoji(self, ascii: Optional[bool] = False) -> str:
    match self:
      case Move.rock:
        return 'o' if ascii else "🪨"
      case Move.paper:
        # return '[]'
        return '[]' if ascii else "📃"
      case Move.scissor:
        # return 'o<'
        return 'o<' if ascii else "✂️"

  @staticmethod
  def random() -> Self:
    return choice(list(Move))
 
def main():
  print('R, P, S?')
  playerMove = Move.fromInput(input())
  computerMove = Move.random()

  if playerMove == None:
    print('Invalid move')
    return;

  print(f'Player move: {playerMove.emoji()}')
  print(f'Computer move: {computerMove.emoji()}')

  match playerMove.play(computerMove):
    case GameResult.win:
      print('you win')
    case GameResult.lose:
      print('you lose')
    case GameResult.draw:
      print('it\'s a draw')

if __name__ == '__main__':
  main()
