import random
import clear

print("Blackjack ")
def deal_card():
    """returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    return sum(cards)

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# compare() abd pass the user_score and computer score and see black jack 0 or > 21 and who won the game

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack!"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "you went over. You lose"
    elif computer_score > 21:
        return "opponent went over. you win"
    elif user_score > computer_score:
        return "you win"
    else:
        return "you lose"

# deal the user and computer 2 cards each using deal_card()
def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint
# need to be repeated until the game ends.

    while not is_game_over:

        user_Score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"your cards : {user_cards}, current score : {user_Score}")
        print(f"computer's first card : {computer_cards[0]}")

    if user_Score == 0 or computer_score == 0 or user_Score >21:
        is_game_over = True
    else:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass:")
        if user_should_deal == "y":
          user_cards.append(deal_card())
        else:
            is_game_over = True

# now time to play computer. the computer should keep drawing cards as long as it has a score less than 17

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        print(f"your final hand:{user_cards}, score: {user_Score}")
        print(f"computer's final hand: {computer_cards}, final score: {computer_score}")
#  if the game has not ended, ask the user if they want to draw another card. if yes, then use the
#  deal_card() to add another card to the user_cards list. if no, then game ended.

# Hint 14 - ask user want to restart the game clear console and start new game

while input("Do you want to play a game of Blackjack? 'y' or 'n': ") == "Y":
    clear()
    play_game()