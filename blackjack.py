import random

def deal_card(): 
    """ turns a random card from cards"""   
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2: 
        return 0
    
    elif 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare_fucntion(user_score, computer_score):
    if user_score == computer_score:
        return "draw"
    elif computer_score == 0:
        return "Lose, opponent has blackjack"
    elif user_score == 0:
        return "win with a blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    
    user_cards = []
    computer_cards = []
    computer_score = -1
    is_game_over = False
    user_score = -1

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"your cards: {user_cards}, current score: {user_score}")
        print(f"computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
         is_game_over = True
        else :
            user_should_deal = input("type 'y' to get the another card, tyoe 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
             is_game_over = True


    while computer_score == 0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score = computer_score(computer_cards)

    print(f"You final hard: {user_cards}, final score: {user_score}")    
    print(f"Computer's final hard: {computer_cards}, final score: {computer_score}") 
    print(compare_fucntion(user_score, computer_score))

print("\n" * 50)
while input("Dou you wanna play of Blackjack? type 'y' or type 'n': "):
    play_game()

