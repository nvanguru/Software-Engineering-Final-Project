import pygame
from random import choice
from sys import exit

pygame.init()
screen_width = 1680
screen_height = 1050
screen_size = (screen_width, screen_height-55)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Art Dealer")
clock = pygame.time.Clock()
background = pygame.Surface(screen_size)
background.fill('gray74')

text_50 = pygame.font.Font(None, 50)
text_70 = pygame.font.Font(None, 70)
text_100 = pygame.font.Font(None, 100)

spade_ace = pygame.image.load('card/spade_ace.png').convert()
spade_two = pygame.image.load('card/spade_two.png').convert()
spade_three = pygame.image.load('card/spade_three.png').convert()
spade_four = pygame.image.load('card/spade_four.png').convert()
spade_five = pygame.image.load('card/spade_five.png').convert()
spade_six = pygame.image.load('card/spade_six.png').convert()
spade_seven = pygame.image.load('card/spade_seven.png').convert()
spade_eight = pygame.image.load('card/spade_eight.png').convert()
spade_nine = pygame.image.load('card/spade_nine.png').convert()
spade_ten = pygame.image.load('card/spade_ten.png').convert()
spade_jack = pygame.image.load('card/spade_jack.png').convert()
spade_queen = pygame.image.load('card/spade_queen.png').convert()
spade_king = pygame.image.load('card/spade_king.png').convert()

club_ace = pygame.image.load('card/club_ace.png').convert()
club_two = pygame.image.load('card/club_two.png').convert()
club_three = pygame.image.load('card/club_three.png').convert()
club_four = pygame.image.load('card/club_four.png').convert()
club_five = pygame.image.load('card/club_five.png').convert()
club_six = pygame.image.load('card/club_six.png').convert()
club_seven = pygame.image.load('card/club_seven.png').convert()
club_eight = pygame.image.load('card/club_eight.png').convert()
club_nine = pygame.image.load('card/club_nine.png').convert()
club_ten = pygame.image.load('card/club_ten.png').convert()
club_jack = pygame.image.load('card/club_jack.png').convert()
club_queen = pygame.image.load('card/club_queen.png').convert()
club_king = pygame.image.load('card/club_king.png').convert()

heart_ace = pygame.image.load('card/heart_ace.png').convert()
heart_two = pygame.image.load('card/heart_two.png').convert()
heart_three = pygame.image.load('card/heart_three.png').convert()
heart_four = pygame.image.load('card/heart_four.png').convert()
heart_five = pygame.image.load('card/heart_five.png').convert()
heart_six = pygame.image.load('card/heart_six.png').convert()
heart_seven = pygame.image.load('card/heart_seven.png').convert()
heart_eight = pygame.image.load('card/heart_eight.png').convert()
heart_nine = pygame.image.load('card/heart_nine.png').convert()
heart_ten = pygame.image.load('card/heart_ten.png').convert()
heart_jack = pygame.image.load('card/heart_jack.png').convert()
heart_queen = pygame.image.load('card/heart_queen.png').convert()
heart_king = pygame.image.load('card/heart_king.png').convert()

diamond_ace = pygame.image.load('card/diamond_ace.png').convert()
diamond_two = pygame.image.load('card/diamond_two.png').convert()
diamond_three = pygame.image.load('card/diamond_three.png').convert()
diamond_four = pygame.image.load('card/diamond_four.png').convert()
diamond_five = pygame.image.load('card/diamond_five.png').convert()
diamond_six = pygame.image.load('card/diamond_six.png').convert()
diamond_seven = pygame.image.load('card/diamond_seven.png').convert()
diamond_eight = pygame.image.load('card/diamond_eight.png').convert()
diamond_nine = pygame.image.load('card/diamond_nine.png').convert()
diamond_ten = pygame.image.load('card/diamond_ten.png').convert()
diamond_jack = pygame.image.load('card/diamond_jack.png').convert()
diamond_queen = pygame.image.load('card/diamond_queen.png').convert()
diamond_king = pygame.image.load('card/diamond_king.png').convert()
card_back = pygame.image.load('card/card_back.png').convert()

card_value = {
    1: spade_ace, 2: spade_two, 3: spade_three, 4: spade_four, 5: spade_five,
    6: spade_six, 7: spade_seven, 8: spade_eight, 9: spade_nine, 10: spade_ten,
    11: spade_jack, 12: spade_queen, 13: spade_king,
    14: diamond_ace, 15: diamond_two, 16: diamond_three, 17: diamond_four, 18: diamond_five,
    19: diamond_six, 20: diamond_seven, 21: diamond_eight, 22: diamond_nine, 23: diamond_ten,
    24: diamond_jack, 25: diamond_queen, 26: diamond_king,
    27: heart_ace, 28: heart_two, 29: heart_three, 30: heart_four, 31: heart_five,
    32: heart_six, 33: heart_seven, 34: heart_eight, 35: heart_nine, 36: heart_ten,
    37: heart_jack, 38: heart_queen, 39: heart_king,
    40: club_ace, 41: club_two, 42: club_three, 43: club_four, 44: club_five,
    45: club_six, 46: club_seven, 47: club_eight, 48: club_nine, 49: club_ten,
    50: club_jack, 51: club_queen, 0: club_king
}
game_stage = 0  
player_hand = 0
player_card = []
dealer_hand = 0
dealer_card = []
help_menu = True
card_deck = [i + 1 for i in range(52 * 4)]
bet_size = 0
player_money = 10000


def deal(person_card):
    dealt_card = choice(card_deck)
    card_deck.remove(dealt_card)
    person_card.append(dealt_card % 52)


def calculate_hand(all_card):
    hand = 0
    ace_in_hand = False

    for card in all_card:
        if 0 < card % 13 < 11:
            hand += card % 13
        else:
            hand += 10

    for card in all_card:
        if card % 13 == 1:
            ace_in_hand = True

    if ace_in_hand and hand < 12:
        return hand + 10
    else:
        return hand


def initial_deal():
    for f_i in range(2):
        deal(dealer_card)
    initial_dealer_hand = calculate_hand(dealer_card)

    for f_i in range(2):
        deal(player_card)
    initial_player_hand = calculate_hand(player_card)

    return initial_dealer_hand, initial_player_hand


def dealer_deal():
    while True:
        if calculate_hand(dealer_card) > 16:
            return calculate_hand(dealer_card)

        deal(dealer_card)


def player_hit():
    deal(player_card)
    f_player_hand = calculate_hand(player_card)

    return f_player_hand


def player_double_down(dd_player_money, dd_bet_size):
    dd_player_money -= dd_bet_size
    dd_bet_size *= 2
    dd_player_hand = player_hit()

    return dd_player_hand, dd_player_money, dd_bet_size


def bet_result(f_player_money, f_bet_size, f_dealer_hand, f_player_hand):
    if f_player_hand == 21 and len(player_card) == 2: 
        if f_dealer_hand == 21 and len(dealer_card) == 2: 
            f_player_money += f_bet_size
        else:
            f_player_money += f_bet_size // 2 * 5
    elif not (f_dealer_hand == 21 and len(dealer_card) == 2):  
        if f_dealer_hand == f_player_hand:
            f_player_money += f_bet_size
        elif f_dealer_hand > 21 or f_dealer_hand < f_player_hand < 22:
            f_player_money += f_bet_size * 2

    return f_player_money


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            pygame.quit()
            exit()

        if help_menu:
            if (event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]) \
                    or (event.type == pygame.KEYDOWN and event.key == pygame.K_h):
                help_menu = False

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_h:
                help_menu = True
                break

            if game_stage == 0:
                if event.type == pygame.KEYDOWN \
                        and (event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3):
                    if event.key == pygame.K_1:
                        bet_size = 500
                    elif event.key == pygame.K_2:
                        bet_size = 1000
                    elif event.key == pygame.K_3:
                        bet_size = 2000

                    player_money -= bet_size
                    dealer_hand, player_hand = initial_deal()
                    game_stage += 1

            elif game_stage == 1:
                # hit
                if pygame.mouse.get_pressed()[0]:
                    player_hand = player_hit()

                    if player_hand > 21:
                        game_stage += 1

                    if player_hand == 21:
                        dealer_hand = dealer_deal()
                        player_money = bet_result(player_money, bet_size, dealer_hand, player_hand)
                        game_stage += 1

                # stand
                elif pygame.mouse.get_pressed()[2]:
                    dealer_hand = dealer_deal()
                    player_money = bet_result(player_money, bet_size, dealer_hand, player_hand)
                    game_stage += 1

                # double down
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_d and len(player_card) == 2:
                    player_hand, player_money, bet_size = player_double_down(player_money, bet_size)
                    dealer_hand = dealer_deal()
                    player_money = bet_result(player_money, bet_size, dealer_hand, player_hand)
                    game_stage += 1

            elif game_stage == 2:
                if pygame.mouse.get_pressed()[0]:
                    game_stage = 0
                    player_hand = 0
                    player_card = []
                    dealer_hand = 0
                    dealer_card = []
                    bet_size = 0
                    card_deck = [i + 1 for i in range(52 * 4)]

                    if player_money < 0 or player_money > 30000:
                        game_stage = 3

    screen.blit(background, (0, 0))
    if game_stage == 3:
        if player_money < 0:
            screen.blit(text_100.render("You have no money!", False, 'Black'), (350, 300))
            screen.blit(text_100.render("Stop playing and go sleep", False, 'Black'), (270, 400))
        elif player_money > 30000:
            screen.blit(text_100.render("You are a god of blackjack!", False, 'Black'), (260, 300))
            screen.blit(text_100.render("Stop playing and go sleep", False, 'Black'), (270, 400))

    elif help_menu:
        screen.blit(text_70.render("Start new game: mouse right", False, 'Black'), (300, 50))
        screen.blit(text_70.render("Hit: mouse right", False, 'Black'), (300, 150))
        screen.blit(text_70.render("stand: mouse left", False, 'Black'), (300, 250))
        screen.blit(text_70.render("Help: h", False, 'Black'), (300, 350))
        screen.blit(text_70.render("Split: To be updated in V2", False, 'Black'), (300, 450))
        screen.blit(text_70.render("Double Down: d", False, 'Black'), (300, 550))
        screen.blit(text_70.render("Quit: q", False, 'Black'), (300, 650))

    else:
        screen.blit(text_50.render("Money: " + str(player_money), False, 'Black'), (900, 600))
        screen.blit(text_50.render("Bet: " + str(bet_size), False, 'Black'), (900, 700))

        if game_stage == 0:
            screen.blit(text_70.render("Choose your bet size", False, 'Black'), (300, 100))
            screen.blit(text_70.render("1: $500", False, 'Black'), (300, 200))
            screen.blit(text_70.render("2: $1000", False, 'Black'), (300, 300))
            screen.blit(text_70.render("3: $2000", False, 'Black'), (300, 400))
        else:
            for i in range(len(dealer_card)):
                screen.blit(card_value[dealer_card[i]], (300 + i * 70, 100))
            for i in range(len(player_card)):
                screen.blit(card_value[player_card[i]], (300 + i * 70, 500))


            if game_stage == 1:
                screen.blit(text_50.render(str(player_hand), False, 'Black'), (300, 450))
                screen.blit(card_back, (300, 100))

            if game_stage == 2:
                screen.blit(text_50.render(str(dealer_hand), False, 'Black'), (300, 50))
                screen.blit(text_50.render(str(player_hand), False, 'Black'), (300, 450))

                if player_hand > 21:
                    screen.blit(text_70.render("YOU ARE BUSTED!", False, 'Black'), (300, 250))
                elif player_hand == 21 and len(player_card) == 2: 
                    if dealer_hand == 21 and len(dealer_card) == 2:  
                        screen.blit(text_70.render("DRAW!", False, 'Black'), (300, 250))
                    else:
                        screen.blit(text_70.render("BLACKJACK!!!", False, 'Black'), (300, 250))
                elif dealer_hand == 21 and len(dealer_card) == 2:  
                    screen.blit(text_70.render("DEALER WIN", False, 'Black'), (300, 250))
                else: 
                    if dealer_hand == player_hand:
                        screen.blit(text_70.render("DRAW!", False, 'Black'), (300, 250))
                    elif dealer_hand > 21 or dealer_hand < player_hand < 22:
                        screen.blit(text_70.render("YOU WIN!", False, 'Black'), (300, 250))
                    else:
                        screen.blit(text_70.render("DEALER WIN", False, 'Black'), (300, 250))

    pygame.display.update()

    clock.tick(30)
