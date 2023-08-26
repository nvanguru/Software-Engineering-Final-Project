import pygame
from random import choice
from sys import exit
import math

pygame.init()


class Player:
    def __init__(self, f_player, f_total_player):
        self.card = []
        self.hand = 0
        self.money = 10000
        self.bet_size = 0

        # FIXME: use WIDTH and HEIGHT for x_pos and y_pos
        deg = math.pi * 3 / 4 - (math.pi / (f_total_player * 4)) - (math.pi / (f_total_player * 4)) * f_player * 2
        self.x_pos = 840 + 1120 * math.cos(deg) // 1
        self.y_pos = -370 + 1120 * math.sin(deg) // 1

    def deal(self):
        deal(self.card)

    def hit(self):
        self.deal()
        self.hand = calculate_hand(self.card)

    def double_down(self):
        self.money -= self.bet_size
        self.bet_size *= 2
        self.deal()
        self.hand = calculate_hand(self.card)

    def choose_bet_size(self, f_player_turn):
        if self.money >= 0:
            if event.type == pygame.KEYDOWN \
                    and (event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3):
                if event.key == pygame.K_1:
                    self.bet_size = 500
                elif event.key == pygame.K_2:
                    self.bet_size = 1000
                elif event.key == pygame.K_3:
                    self.bet_size = 2000
                self.money -= self.bet_size

                return f_player_turn + 1
            else:
                return f_player_turn  # If there is no constant return even when there is no input, player_turn == None in the event loop.
        else:
            return f_player_turn + 1

    def initial_deal(self):
        if self.money >= 0:
            self.deal()
            self.deal()
            self.hand = calculate_hand(self.card)

    def hit_stand(self, f_player_turn):
        if self.money >= 0:
            if self.hand >= 21:
                return f_player_turn + 1

            else:
                # hit
                if pygame.mouse.get_pressed()[0] or event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.hit()
                    return f_player_turn

                # stand
                elif pygame.mouse.get_pressed()[2] or event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    return f_player_turn + 1

                # double down
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_d and len(self.card) == 2:
                    self.double_down()
                    return f_player_turn + 1

                else:
                    return f_player_turn
        else:
            return f_player_turn + 1

    def bet_result(self, f_dealer_card):
        if self.money >= 0:
            f_dealer_hand = calculate_hand(f_dealer_card)

            if self.hand < 22:
                if self.hand == 21 and len(self.card) == 2: # player blackjack
                    if f_dealer_hand == 21 and len(f_dealer_card) == 2:  # Dealer Blackjack --> Draw
                        self.money += self.bet_size
                    else:
                        self.money += self.bet_size // 2 * 5
                elif not (f_dealer_hand == 21 and len(f_dealer_card) == 2):  # If the dealer is not blackjack
                    if f_dealer_hand == self.hand:
                        self.money += self.bet_size
                    elif f_dealer_hand > 21 or f_dealer_hand < self.hand < 22:
                        self.money += self.bet_size * 2

    def initialize(self):
        self.card = []
        self.bet_size = 0
        self.hand = 0

    # def set_xy_pos(self, f_player, f_total_player):  # For mid-player add-ons
    #     deg = math.pi * 3 / 4 - (math.pi / (f_total_player * 4)) - (math.pi / (f_total_player * 4)) * f_player * 2
    #     self.x_pos = 840 + 1120 * math.cos(deg)
    #     self.y_pos = -370 + 1120 * math.sin(deg)


def deal(person_card):
    dealt_card = choice(card_deck)
    card_deck.remove(dealt_card)
    person_card.append(dealt_card % 52)


def calculate_hand(all_card):
    f_hand = 0
    ace_in_hand = False

    for card in all_card:
        if 0 < card % 13 < 11:
            f_hand += card % 13
        else:
            f_hand += 10

    for card in all_card:
        if card % 13 == 1:
            ace_in_hand = True

    if ace_in_hand and f_hand < 12:
        return f_hand + 10
    else:
        return f_hand


def dealer_deal(f_dealer_card):
    while True:
        if calculate_hand(f_dealer_card) > 16:
            return calculate_hand(f_dealer_card)

        deal(f_dealer_card)


def print_player_card(f_player_list, f_player_num):
    player_card = f_player_list[f_player_num].card
    total_card = len(player_card)
    for i in range(total_card):
        screen.blit(card_value[player_card[i]],
                    (134 / total_card * i - 105 + f_player_list[f_player_num].x_pos, f_player_list[f_player_num].y_pos))


if __name__ == '__main__':
    # screen settings
    WIDTH = 1680
    HEIGHT = 1050
    screen_size = (WIDTH, HEIGHT - 55)
    screen = pygame.display.set_mode(screen_size)

    # Set screen title
    pygame.display.set_caption("Art Dealer")

    # set frame rate
    FPS = 30
    clock = pygame.time.Clock()

    # Set wallpaper
    background = pygame.Surface(screen_size)
    background.fill('gray74')

    # Set the text font
    text_30 = pygame.font.Font(None, 30)
    text_40 = pygame.font.Font(None, 40)
    text_50 = pygame.font.Font(None, 50)
    text_70 = pygame.font.Font(None, 70)
    text_100 = pygame.font.Font(None, 100)

    # image variable
    card_value = {
        1: pygame.image.load('card/spade_ace.png').convert(),
        2: pygame.image.load('card/spade_two.png').convert(),
        3: pygame.image.load('card/spade_three.png').convert(),
        4: pygame.image.load('card/spade_four.png').convert(),
        5: pygame.image.load('card/spade_five.png').convert(),
        6: pygame.image.load('card/spade_six.png').convert(),
        7: pygame.image.load('card/spade_seven.png').convert(),
        8: pygame.image.load('card/spade_eight.png').convert(),
        9: pygame.image.load('card/spade_nine.png').convert(),
        10: pygame.image.load('card/spade_ten.png').convert(),
        11: pygame.image.load('card/spade_jack.png').convert(),
        12: pygame.image.load('card/spade_queen.png').convert(),
        13: pygame.image.load('card/spade_king.png').convert(),

        14: pygame.image.load('card/club_ace.png').convert(),
        15: pygame.image.load('card/club_two.png').convert(),
        16: pygame.image.load('card/club_three.png').convert(),
        17: pygame.image.load('card/club_four.png').convert(),
        18: pygame.image.load('card/club_five.png').convert(),
        19: pygame.image.load('card/club_six.png').convert(),
        20: pygame.image.load('card/club_seven.png').convert(),
        21: pygame.image.load('card/club_eight.png').convert(),
        22: pygame.image.load('card/club_nine.png').convert(),
        23: pygame.image.load('card/club_ten.png').convert(),
        24: pygame.image.load('card/club_jack.png').convert(),
        25: pygame.image.load('card/club_queen.png').convert(),
        26: pygame.image.load('card/club_king.png').convert(),

        27: pygame.image.load('card/heart_ace.png').convert(),
        28: pygame.image.load('card/heart_two.png').convert(),
        29: pygame.image.load('card/heart_three.png').convert(),
        30: pygame.image.load('card/heart_four.png').convert(),
        31: pygame.image.load('card/heart_five.png').convert(),
        32: pygame.image.load('card/heart_six.png').convert(),
        33: pygame.image.load('card/heart_seven.png').convert(),
        34: pygame.image.load('card/heart_eight.png').convert(),
        35: pygame.image.load('card/heart_nine.png').convert(),
        36: pygame.image.load('card/heart_ten.png').convert(),
        37: pygame.image.load('card/heart_jack.png').convert(),
        38: pygame.image.load('card/heart_queen.png').convert(),
        39: pygame.image.load('card/heart_king.png').convert(),

        40: pygame.image.load('card/diamond_ace.png').convert(),
        41: pygame.image.load('card/diamond_two.png').convert(),
        42: pygame.image.load('card/diamond_three.png').convert(),
        43: pygame.image.load('card/diamond_four.png').convert(),
        44: pygame.image.load('card/diamond_five.png').convert(),
        45: pygame.image.load('card/diamond_six.png').convert(),
        46: pygame.image.load('card/diamond_seven.png').convert(),
        47: pygame.image.load('card/diamond_eight.png').convert(),
        48: pygame.image.load('card/diamond_nine.png').convert(),
        49: pygame.image.load('card/diamond_ten.png').convert(),
        50: pygame.image.load('card/diamond_jack.png').convert(),
        51: pygame.image.load('card/diamond_queen.png').convert(),
        0: pygame.image.load('card/diamond_king.png').convert()
    }
    card_back = pygame.image.load('card/card_back.png').convert()
    player_cursor = pygame.image.load('card/player_cursor.png').convert()
    player_cursor.set_colorkey((255, 255, 255))

    # game variable
    game_stage = 0 # 0: Select number of players, 1: Bet, 2: hit/stand 3: Dealer stage and settlement 4: End of game
    dealer_hand = 0
    dealer_card = []
    player_list = []
    total_player = 0
    player_turn = 0
    help_menu = True
    card_deck = [i + 1 for i in range(52 * 4)]

    # event loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.quit()
                exit()

            if help_menu:
                # Exit help
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] \
                        or event.type == pygame.KEYDOWN and event.key == pygame.K_h \
                        or event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    help_menu = False

            else:
                # Help
                if event.type == pygame.KEYDOWN and event.key == pygame.K_h:
                    help_menu = True

                # Select number of players
                elif game_stage == 0:
                    if event.type == pygame.KEYDOWN \
                            and (event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3
                                 or event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6
                                 or event.key == pygame.K_7):
                        if event.key == pygame.K_1:
                            total_player = 1
                        elif event.key == pygame.K_2:
                            total_player = 2
                        elif event.key == pygame.K_3:
                            total_player = 3
                        elif event.key == pygame.K_4:
                            total_player = 4
                        elif event.key == pygame.K_5:
                            total_player = 5
                        elif event.key == pygame.K_6:
                            total_player = 6
                        elif event.key == pygame.K_7:
                            total_player = 7

                        for i in range(total_player):
                            player_list.append(Player(i, total_player))
                        game_stage += 1

                # Betting step
                elif game_stage == 1:
                    player_turn = player_list[player_turn].choose_bet_size(player_turn)

                    if player_turn == total_player:
                        player_turn = 0
                        game_stage += 1

                        # Deal when betting is complete
                        for i in range(total_player):
                            player_list[i].initial_deal()

                        deal(dealer_card)
                        deal(dealer_card)

                # hit/stand steps
                elif game_stage == 2:
                    player_turn = player_list[player_turn].hit_stand(player_turn)

                    if player_turn == total_player:
                        player_turn = 0
                        game_stage += 1

                # Dealer phase, bet settlement
                elif game_stage == 3:
                    for i in range(total_player):  # All players burst --> Deal X
                        if player_list[i].hand < 22:
                            dealer_hand = dealer_deal(dealer_card)
                            break
                    for i in range(total_player):
                        player_list[i].bet_result(dealer_card)

                    game_stage += 1

                # end game, start new game
                elif game_stage == 4:
                    if pygame.mouse.get_pressed()[0] or event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        game_stage = 1
                        dealer_hand = 0
                        dealer_card = []
                        card_deck = [i + 1 for i in range(52 * 4)]
                        for i in range(total_player):
                            player_list[i].initialize()

        # screen output
        screen.blit(background, (0, 0))
        if help_menu:
            screen.blit(text_70.render("New game: left click / space", False, 'Black'), (WIDTH // 5, HEIGHT // 10 + 50))
            screen.blit(text_70.render("Hit: left click / space", False, 'Black'), (WIDTH // 5, HEIGHT // 10 + 150))
            screen.blit(text_70.render("Stand: right click / s", False, 'Black'), (WIDTH // 5, HEIGHT // 10 + 250))
            screen.blit(text_70.render("Help: h", False, 'Black'), (WIDTH // 5, HEIGHT // 10 + 350))
            screen.blit(text_70.render("Split: TBD", False, 'Black'), (WIDTH // 5, HEIGHT // 10 + 450))
            screen.blit(text_70.render("Double Down: d", False, 'Black'), (WIDTH // 5, HEIGHT // 10 + 550))
            screen.blit(text_70.render("Quit: q", False, 'Black'), (WIDTH // 5, HEIGHT // 10 + 650))

        elif game_stage == 0:  # 0: Select number of people
            screen.blit(text_70.render("# of players (3-5)", False, 'Black'), (WIDTH // 5, HEIGHT // 10))

        else:
            # non-player output
            if game_stage == 1:  # 1: Betting
                screen.blit(text_50.render("Choose your bet size", False, 'Black'), (WIDTH // 2 - 200, HEIGHT // 10))
                screen.blit(text_50.render("1: $500", False, 'Black'), (WIDTH // 2 - 200, HEIGHT // 10 + 70))
                screen.blit(text_50.render("2: $1000", False, 'Black'), (WIDTH // 2 - 200, HEIGHT // 10 + 140))
                screen.blit(text_50.render("3: $2000", False, 'Black'), (WIDTH // 2 - 200, HEIGHT // 10 + 210))

            # dealer
            if game_stage >= 2:
                # dealer card
                for i in range(len(dealer_card)):
                    screen.blit(card_value[dealer_card[i]],
                                (134 // len(dealer_card) * i + WIDTH // 2 - 100, HEIGHT // 10))
                    # Dealer Hidden Card
                    if i == 0:
                        if game_stage == 2:
                            screen.blit(card_back, (WIDTH // 2 - 100, HEIGHT // 10))
                        elif game_stage >= 3:  # Draw the back of the card once and draw again if there is someone who is not a burst
                            screen.blit(card_back, (WIDTH // 2 - 100, HEIGHT // 10))
                            for j in range(total_player):
                                if player_list[j].hand < 22:
                                    screen.blit(card_value[dealer_card[0]], (WIDTH // 2 - 100, HEIGHT // 10))
                                    break

                # dealer hand
                if game_stage >= 3:
                    for j in range(total_player):
                        if player_list[j].hand < 22:
                            screen.blit(text_50.render(f"{dealer_hand}", False, 'Black'),
                                        (WIDTH // 2 - 100, HEIGHT // 10 - 50))

            # Cursor
            if game_stage >= 1:
                screen.blit(player_cursor, (player_list[player_turn].x_pos - 120, player_list[player_turn].y_pos + 107))

            # player output
            for i in range(total_player):
                screen.blit(text_50.render(f"Money: {player_list[i].money}", False, 'Black'),
                            (player_list[i].x_pos - 100, player_list[i].y_pos + 100))
                screen.blit(text_50.render(f"Bet: {player_list[i].bet_size}", False, 'Black'),
                            (player_list[i].x_pos - 100, 50 + player_list[i].y_pos + 100))

                # Bankruptcy
                if player_list[i].money < 0:
                    screen.blit(text_50.render('Bankrupted', False, 'Black'),
                                (player_list[i].x_pos - 100, 50 + player_list[i].y_pos))

                elif game_stage >= 2:
                    # card
                    print_player_card(player_list, i)
                    screen.blit(text_50.render(f"{player_list[i].hand}", False, 'Black'),
                                (-100 + player_list[i].x_pos, -50 + player_list[i].y_pos))

                    #burst
                    if player_list[i].hand > 21:
                        screen.blit(text_50.render("BUSTED!", False, 'Black'),
                                    (-50 + player_list[i].x_pos, -50 + player_list[i].y_pos))

                    # Betting result
                    elif game_stage >= 3:
                        if player_list[i].hand == 21 and len(player_list[i].card) == 2:  # player blackjack
                            if dealer_hand == 21 and len(dealer_card) == 2:  # Dealer Blackjack --> Draw
                                screen.blit(text_50.render("DRAW!", False, 'Black'),
                                            (-50 + player_list[i].x_pos, -50 + player_list[i].y_pos))
                            else:
                                screen.blit(text_50.render("WIN!!!", False, 'Black'),
                                            (-50 + player_list[i].x_pos, -50 + player_list[i].y_pos))
                        elif dealer_hand == 21 and len(dealer_card) == 2:  # Not Player Blackjack, Dealer Blackjack
                            screen.blit(text_50.render("Lose", False, 'Black'),
                                        (-50 + player_list[i].x_pos, -50 + player_list[i].y_pos))
                        else:  # Player, Dealer is not blackjack
                            if dealer_hand == player_list[i].hand:
                                screen.blit(text_50.render("DRAW!", False, 'Black'),
                                            (-50 + player_list[i].x_pos, -50 + player_list[i].y_pos))
                            elif dealer_hand > 21 or dealer_hand < player_list[i].hand < 22:
                                screen.blit(text_50.render("WIN!", False, 'Black'),
                                            (-50 + player_list[i].x_pos, -50 + player_list[i].y_pos))
                            else:
                                screen.blit(text_50.render("Lose", False, 'Black'),
                                            (-50 + player_list[i].x_pos, -50 + player_list[i].y_pos))

        pygame.display.update()

        clock.tick(FPS)  # frame rate

# to do
# 1. Player hand output
# 2. Output result messages separately for each player
# 3. Don't deal with the dealer when all players are busted
# 5. Cursor showing whose turn it is
# 9. Stop when player bankruptcy


# 4. Split
# 4.1. Can overlap up to 3 splits, split A only once
# 4.2. 21 Blackjack disallowed after A-10 split
# 6. Make the Start Menu and Help Button Neat
# 7. Check if the bug occurs when the keys are pressed at the same time
# 8. Using get_x_pos, get_y_pos: WIDTH, HEIGHT
# 10. Player Intermediate Add-on