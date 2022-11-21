print("Rock, Paper, Scissors! - Riley Gribbon")
playAgain = input("Begin Game? ")
playAgain = playAgain.lower()
while playAgain == 'yes':
  p1Move = input(str("Player 1 - Make a move: "))
  p1Move = p1Move.lower()
  p2Move = input(str("Player 2 - Make a move: "))
  p2Move = p2Move.lower()
  if p1Move == "rock" and p2Move == "rock":
    print("Tie - Both Players Picked Rock")
    playAgain = input('Play Again? ')
    playAgain = playAgain.lower()
  elif p1Move == "paper" and p2Move == "paper":
    print("Tie - Both Players Picked Paper")
    playAgain = input('Play Again? ')
    playAgain = playAgain.lower()
  elif p1Move == "scissors" and p2Move == "scissors":
    print("Tie - Both Players Picked Scissors")
    playAgain = input('Play Again? ')
    playAgain = playAgain.lower()
  elif p1Move == "rock" and p2Move == "scissors":
    print("Player 1 Wins - Rock Crushes Scissors")
    playAgain = input('Play Again? ')
    playAgain = playAgain.lower()
  elif p1Move == "scissors" and p2Move == "paper":
    print("Player 1 Wins - Scissors Cuts Paper")
    playAgain = input('Play Again? ')
    playAgain = playAgain.lower()
  elif p1Move == "paper" and p2Move == "rock":
    print("Player 1 Wins - Paper Covers Rock!")
    playAgain = input('Play Again? ')
    playAgain = playAgain.lower()

  elif p2Move == "rock" and p1Move == "scissors":
    print("Player 2 Wins - Rock Crushes Scissors!")
    playAgain = input('Play Again? ')
    playAgain = playAgain.lower()
  elif p2Move == "scissors" and p1Move == "paper":
    print("Player 2 Wins - Scissors Cuts Paper!")
    playAgain = input('Play Again? ')
    playAgain = playAgain.lower()
  elif p2Move == "paper" and p1Move == "rock":
    print("Player 2 Wins - Paper Covers Rock")
    playAgain = input('Play Again? ')
    playAgain = playAgain.lower()
  if (p1Move == "rock") or (p1Move == "paper") or (p1Move == "scissors"):
    print("")
  else:
    print("Player 1 made an invalid move! Restarting Game")
    print("")

  if (p2Move == "rock") or (p2Move == "paper") or (p2Move == "scissors"):
    print("")
  else:
    print("Player 2 made an invalid move! Restarting Game")
    print("")

print("Thanks for playing! - Riley")
input("Press any key to exit...")
exit()

  
