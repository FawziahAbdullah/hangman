def hangman():
	stage = 0
	wrong_guesses=["","__________","|  |","|  0   ","|   /|/   ","|  //  ","|        "]
	word="cat"
	score_board=['_']*len(word)
	win=False
	print("Welcome to hangman")
	while stage<len(wrong_guesses)-1:
		print('\n')
		guess=input("Guess a letter ")
		if guess in word :
			score_board[word.index(guess)]=guess
		else:
			stage+=1
			print(''.join(score_board))
			print('\n'.join(wong_guesses[0:stage+1]))
		if '_'not in score_board:
			print("You win , the word was :")
			win=True
			break
		print('\n'.join(wong_guesses[0:stage]))
		print("You lose!")
