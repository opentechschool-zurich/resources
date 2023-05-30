import 'dart:math';
import 'dart:io';

enum GameResult { win, lose, draw }

enum Move {
  rock,
  paper,
  scissors;

  /// Create a [Move] from the string [s]. Returns [null] if [s]
  /// does not refer to a valid move.
  static Move? from(String? s) {
    return switch (s?.toLowerCase()) {
      "r" => Move.rock,
      "p" => Move.paper,
      "s" => Move.scissors,
      _ => null
    };
  }

  /// Play this move against [other], returns the result from
  /// this move's perspective.
  GameResult play(Move other) {
    if (this == other) return GameResult.draw;

    return switch ((this, other)) {
      (paper, rock) => GameResult.win,
      (scissors, paper) => GameResult.win,
      (rock, scissors) => GameResult.win,
      _ => GameResult.lose
    };
  }

  String emoji() {
    return switch (this) {
        rock => "🪨",
        paper => "📃",
        scissors => "✂️"
    };
  }

  static final rng = Random();
  static Move random() {
    return Move.values[rng.nextInt(Move.values.length)];
  }
}

void main() {

  print("R, P, S?");

  final input = stdin.readLineSync();
  final move = Move.from(input);

  if (move == null) {
    print("Invalid move");
    return;
  }

  final computerMove = Move.random();

  print("Your move: ${move.emoji()}");
  print("Computer move: ${computerMove.emoji()}");

  final result = move.play(computerMove);
  switch (result) {
    case GameResult.win:
      print("You win, ${move.emoji()} beats ${computerMove.emoji()}");
    case GameResult.lose:
      print("You lose, ${computerMove.emoji()} beats ${move.emoji()}");
    case GameResult.draw:
      print("It's a draw");
  }
}
