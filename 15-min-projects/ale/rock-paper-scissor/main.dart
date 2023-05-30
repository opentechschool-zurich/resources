import 'dart:math';
import 'dart:io';

enum Move { rock, paper, scissors }

void main() {
  final rng = Random();
  while (true) {
    stdout.write('rock, paper or scissors? (r/p/s/q[uit])');
    final input = stdin.readLineSync();
    if (input == 'r' || input == 'p' || input == 's') {
      var playerMove;
      if (input == 'r') {
        playerMove = Move.rock;
      }   else if (input == 'p') {
        playerMove = Move.paper;
      }  else {
        playerMove = Move.scissors;
      }
      final random = rng.nextInt(3);
      final aiMove = Move.values[random];
      print('you played: $playerMove');
      print('AI played: $aiMove');
      if (playerMove == aiMove) {
        print('it is a draw');
      } else if (playerMove == Move.rock && aiMove == Move.scissors ||
          playerMove == Move.paper && aiMove == Move.rock ||
          playerMove == Move.scissors && aiMove == Move.paper) {
        print('you win');
      } else {
        print('you lose');
      }
    } else if (input == 'q') {
      break;
    } else {
      print('invalid input');
    }
  }
}
