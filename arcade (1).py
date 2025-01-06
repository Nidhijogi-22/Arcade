import tkinter as tk
import random
import turtle

# Set up the main application window
root = tk.Tk()
root.title("Arcade: RPS, Guess the Number, Tic-Tac-Toe, Coin Flip & Turtle Racing")

# Enable fullscreen mode
root.attributes('-fullscreen', True)
root.config(bg="lightblue")

# Global variables for all games
user_score = 0
computer_score = 0
secret_number = random.randint(1, 100)
attempts = 0
choices = ['Rock', 'Paper', 'Scissors']
coin_options = ['Heads', 'Tails']
tic_tac_toe_board = [""] * 9
player_turn = "X"

# --------------------- Rock, Paper, Scissors -------------------------
def update_score(winner):
    global user_score, computer_score
    if winner == 'User':
        user_score += 1
    elif winner == 'Computer':
        computer_score += 1
        update_score.config(text=f"User: {user_score}  Computer: {computer_score}")

def play_rps(user_choice):
    computer_choice = random.choice(choices)
    result = check_rps_winner(user_choice, computer_choice)
    rps_result_label.config(text=f"Computer chose {computer_choice}. {result}")
    update_score(result)

def check_rps_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'Rock' and computer == 'Scissors') or \
         (user == 'Scissors' and computer == 'Paper') or \
         (user == 'Paper' and computer == 'Rock'):
        return "User"
    else:
        return "Computer"

# --------------------- Guess the Number -------------------------
def check_guess():
    global attempts
    try:
        guess = int(guess_entry.get())
        attempts += 1
        if guess < secret_number:
            guess_result_label.config(text="Too low! Try again.")
        elif guess > secret_number:
            guess_result_label.config(text="Too high! Try again.")
        else:
            guess_result_label.config(text=f"Correct! You guessed it in {attempts} attempts!")
            guess_button.config(state="disabled")
    except ValueError:
        guess_result_label.config(text="Please enter a valid number.")

def reset_guess_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    guess_result_label.config(text="")
    guess_entry.delete(0, tk.END)
    guess_button.config(state="normal")

# --------------------- Tic-Tac-Toe -------------------------
def ttt_button_click(button, index):
    global player_turn
    if tic_tac_toe_board[index] == "" and button["text"] == "":
        button.config(text=player_turn)
        tic_tac_toe_board[index] = player_turn
        if check_ttt_winner():
            ttt_result_label.config(text=f"Player {player_turn} wins!")
            disable_ttt_buttons()
        elif "" not in tic_tac_toe_board:
            ttt_result_label.config(text="It's a tie!")
        else:
            player_turn = "O" if player_turn == "X" else "X"
            ttt_result_label.config(text=f"Player {player_turn}'s turn")

def check_ttt_winner():
    win_conditions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for condition in win_conditions:
        if tic_tac_toe_board[condition[0]] == tic_tac_toe_board[condition[1]] == tic_tac_toe_board[condition[2]] != "":
            return True
    return False

def disable_ttt_buttons():
    for button in ttt_buttons:
        button.config(state="disabled")

def reset_ttt_game():
    global tic_tac_toe_board, player_turn
    tic_tac_toe_board = [""] * 9
    player_turn = "X"
    for button in ttt_buttons:
        button.config(text="", state="normal")
    ttt_result_label.config(text="Player X's turn")

# --------------------- Coin Flip -------------------------
def play_coin_flip(user_choice):
    computer_choice = random.choice(coin_options)
    if user_choice == computer_choice:
        flip_result_label.config(text=f"It's {computer_choice}. You win!")
    else:
        flip_result_label.config(text=f"It's {computer_choice}. You lose!")

# --------------------- Quiz game -------------------------    
quiz_questions = [
    {"question": "What is the capital of France?", "choices": ["Paris", "London", "Berlin", "Rome"], "answer": "Paris"},
    {"question": "What is 5 + 7?", "choices": ["10", "11", "12", "13"], "answer": "12"},
    {"question": "Which planet is known as the Red Planet?", "choices": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars"},
    {"question": "How many continents are there?", "choices": ["5", "6", "7", "8"], "answer": "7"},
    {"question": "Who wrote 'Harry Potter'?", "choices": ["J.K. Rowling", "Tolkien", "Mark Twain", "Agatha Christie"], "answer": "J.K. Rowling"},
    {"question": "What is the boiling point of water?", "choices": ["90°C", "100°C", "110°C", "120°C"], "answer": "100°C"},
    {"question": "Which ocean is the largest?", "choices": ["Atlantic", "Indian", "Arctic", "Pacific"], "answer": "Pacific"},
    {"question": "Who was the first president of the USA?", "choices": ["George Washington", "Abraham Lincoln", "John Adams", "Thomas Jefferson"], "answer": "George Washington"},
    {"question": "What is the largest mammal?", "choices": ["Elephant", "Blue Whale", "Giraffe", "Shark"], "answer": "Blue Whale"},
    {"question": "How many states are there in the USA?", "choices": ["50", "48", "52", "46"], "answer": "50"}
]
current_question_index = 0
quiz_score = 0

def display_question():
    global current_question_index
    if current_question_index < len(quiz_questions):
        question = quiz_questions[current_question_index]["question"]
        choices = quiz_questions[current_question_index]["choices"]
        quiz_question_label.config(text=question)
        for i, choice in enumerate(choices):
            quiz_buttons[i].config(text=choice, state="normal")
        quiz_feedback_label.config(text="")
    else:
        end_quiz()

def check_answer(selected_choice):
    global current_question_index, quiz_score
    correct_answer = quiz_questions[current_question_index]["answer"]
    if selected_choice == correct_answer:
        quiz_feedback_label.config(text="Correct!", fg="green")
        quiz_score += 1
    else:
        quiz_feedback_label.config(text=f"Wrong! The correct answer was {correct_answer}.", fg="red")
    current_question_index += 1
    quiz_next_button.config(state="normal")

def next_question():
    quiz_next_button.config(state="disabled")
    display_question()

def end_quiz():
    quiz_question_label.config(text=f"Quiz Over! Your score: {quiz_score}/{len(quiz_questions)}")
    for button in quiz_buttons:
        button.config(state="disabled")
    quiz_next_button.config(state="disabled")

def reset_quiz():
    global current_question_index, quiz_score
    current_question_index = 0
    quiz_score = 0
    display_question()
    
# Main loop
# --------------------- Menu Navigation -------------------------
def hide_all_frames():
    rps_frame.pack_forget()
    guess_frame.pack_forget()
    ttt_frame.pack_forget()
    flip_frame.pack_forget()
    menu_frame.pack_forget()

def show_rps_game():
    hide_all_frames()
    rps_frame.pack(fill="both", expand=True)

def show_guess_game():
    hide_all_frames()
    guess_frame.pack(fill="both", expand=True)

def show_ttt_game():
    hide_all_frames()
    ttt_frame.pack(fill="both", expand=True)

def show_flip_game():
    hide_all_frames()
    flip_frame.pack(fill="both", expand=True)

def show_quiz_game():
    hide_all_frames()
    quiz_frame.pack(fill="both", expand=True)
    reset_quiz()    

def show_menu():
    hide_all_frames()
    menu_frame.pack(fill="both", expand=True)
  
def exit_fullscreen():
    root.attributes('-fullscreen', False)

# --------------------- UI Setup -------------------------
# Menu Frame
menu_frame = tk.Frame(root, bg="lightblue")
menu_title_label = tk.Label(menu_frame, text="Welcome to the Arcade!", font=("Arial", 30), bg="lightblue")
menu_title_label.pack(pady=50)

rps_menu_button = tk.Button(menu_frame, text="Play Rock, Paper, Scissors", font=("Arial", 20), command=show_rps_game)
rps_menu_button.pack(pady=10)

guess_menu_button = tk.Button(menu_frame, text="Play Guess the Number", font=("Arial", 20), command=show_guess_game)
guess_menu_button.pack(pady=10)

ttt_menu_button = tk.Button(menu_frame, text="Play Tic-Tac-Toe", font=("Arial", 20), command=show_ttt_game)
ttt_menu_button.pack(pady=10)

flip_menu_button = tk.Button(menu_frame, text="Play Coin Flip", font=("Arial", 20), command=show_flip_game)
flip_menu_button.pack(pady=10)

quiz_menu_button = tk.Button(menu_frame, text="Play Quiz Game", font=("Arial", 20), command=show_quiz_game)
quiz_menu_button.pack(pady=10)

exit_menu_button = tk.Button(menu_frame, text="Exit Fullscreen", font=("Arial", 20), command=exit_fullscreen)
exit_menu_button.pack(pady=10)

# --------------------- RPS Frame -------------------------
rps_frame = tk.Frame(root, bg="lightgreen")
rps_title_label = tk.Label(rps_frame, text="Rock, Paper, Scissors", font=("Arial", 24), bg="lightgreen")
rps_title_label.pack(pady=10)

rps_button_frame = tk.Frame(rps_frame, bg="lightgreen")
rps_button_frame.pack(pady=20)

rock_button = tk.Button(rps_button_frame, text="Rock", font=("Arial", 16), command=lambda: play_rps('Rock'))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(rps_button_frame, text="Paper", font=("Arial", 16), command=lambda: play_rps('Paper'))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(rps_button_frame, text="Scissors", font=("Arial", 16), command=lambda: play_rps('Scissors'))
scissors_button.grid(row=0, column=2, padx=10)

rps_result_label = tk.Label(rps_frame, text="", font=("Arial", 16), bg="lightgreen")
rps_result_label.pack(pady=20)

back_to_menu_button1 = tk.Button(rps_frame, text="Back to Menu", font=("Arial", 16), command=show_menu)
back_to_menu_button1.pack(pady=20)

# --------------------- Guess Frame -------------------------
guess_frame = tk.Frame(root, bg="lightblue")
guess_title_label = tk.Label(guess_frame, text="Guess the Number", font=("Arial", 24), bg="lightblue")
guess_title_label.pack(pady=10)

guess_instruction_label = tk.Label(guess_frame, text="Enter a number between 1 and 100:", font=("Arial", 16), bg="lightblue")
guess_instruction_label.pack(pady=10)

guess_entry = tk.Entry(guess_frame, font=("Arial", 16))
guess_entry.pack(pady=10)

guess_button = tk.Button(guess_frame, text="Submit Guess", font=("Arial", 16), command=check_guess)
guess_button.pack(pady=10)

guess_result_label = tk.Label(guess_frame, text="", font=("Arial", 16), bg="lightblue")
guess_result_label.pack(pady=20)

reset_guess_button = tk.Button(guess_frame, text="Reset Game", font=("Arial", 16), command=reset_guess_game)
reset_guess_button.pack(pady=10)

back_to_menu_button2 = tk.Button(guess_frame, text="Back to Menu", font=("Arial", 16), command=show_menu)
back_to_menu_button2.pack(pady=20)

# --------------------- Tic-Tac-Toe Frame -------------------------
ttt_frame = tk.Frame(root, bg="lightyellow")
ttt_title_label = tk.Label(ttt_frame, text="Tic-Tac-Toe", font=("Arial", 24), bg="lightyellow")
ttt_title_label.pack(pady=10)

ttt_button_frame = tk.Frame(ttt_frame)
ttt_button_frame.pack(pady=20)

ttt_buttons = []
for i in range(9):
    button = tk.Button(ttt_button_frame, text="", font=("Arial", 20), width=5, height=2, command=lambda i=i: ttt_button_click(ttt_buttons[i], i))
    button.grid(row=i//3, column=i%3)
    ttt_buttons.append(button)

ttt_result_label = tk.Label(ttt_frame, text="Player X's turn", font=("Arial", 16), bg="lightyellow")
ttt_result_label.pack(pady=20)

reset_ttt_button = tk.Button(ttt_frame, text="Reset Game", font=("Arial", 16), command=reset_ttt_game)
reset_ttt_button.pack(pady=10)

back_to_menu_button3 = tk.Button(ttt_frame, text="Back to Menu", font=("Arial", 16), command=show_menu)
back_to_menu_button3.pack(pady=20)

# --------------------- Coin Flip Frame -------------------------
flip_frame = tk.Frame(root, bg="lightpink")
flip_title_label = tk.Label(flip_frame, text="Coin Flip", font=("Arial", 24), bg="lightpink")
flip_title_label.pack(pady=10)

flip_instruction_label = tk.Label(flip_frame, text="Choose Heads or Tails.", font=("Arial", 16), bg="lightpink")
flip_instruction_label.pack(pady=10)

flip_button_frame = tk.Frame(flip_frame, bg="lightpink")
flip_button_frame.pack(pady=20)

heads_button = tk.Button(flip_button_frame, text="Heads", font=("Arial", 16), width=10, command=lambda: play_coin_flip('Heads'))
heads_button.grid(row=0, column=0, padx=10)

tails_button = tk.Button(flip_button_frame, text="Tails", font=("Arial", 16), width=10, command=lambda: play_coin_flip('Tails'))
tails_button.grid(row=0, column=1, padx=10)

flip_result_label = tk.Label(flip_frame, text="", font=("Arial", 16), bg="lightpink")
flip_result_label.pack(pady=20)

back_to_menu_button4 = tk.Button(flip_frame, text="Back to Menu", font=("Arial", 16), command=show_menu)
back_to_menu_button4.pack(pady=20)

# --------------------- Quiz Frame -------------------------
quiz_frame = tk.Frame(root, bg="lightgreen")
quiz_title_label = tk.Label(quiz_frame, text="Quiz Game", font=("Arial", 24), bg="lightgreen")
quiz_title_label.pack(pady=10)

quiz_question_label = tk.Label(quiz_frame, text="", font=("Arial", 18), bg="lightgreen")
quiz_question_label.pack(pady=20)

quiz_button_frame = tk.Frame(quiz_frame, bg="lightgreen")
quiz_button_frame.pack(pady=10)

quiz_buttons = []
for i in range(4):
    button = tk.Button(quiz_button_frame, text="", font=("Arial", 16), width=20, command=lambda i=i: check_answer(quiz_buttons[i].cget("text")))
    button.grid(row=i, column=0, pady=5)
    quiz_buttons.append(button)

quiz_feedback_label = tk.Label(quiz_frame, text="", font=("Arial", 16), bg="lightgreen")
quiz_feedback_label.pack(pady=10)

quiz_next_button = tk.Button(quiz_frame, text="Next Question", font=("Arial", 16), state="disabled", command=next_question)
quiz_next_button.pack(pady=20)

back_to_menu_button5 = tk.Button(quiz_frame, text="Back to Menu", font=("Arial", 16), command=show_menu)
back_to_menu_button5.pack(pady=20)

# Start by showing the main menu
show_menu()

# Main loop
root.mainloop()
