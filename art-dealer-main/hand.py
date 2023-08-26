import pygame
from random import choice
import os

pygame.init()


def deal(card_deck, person_card):
    dealt_card = choice(card_deck)
    card_deck.remove(dealt_card)
    person_card.append(dealt_card % 52)


class Hand:
    # load images
    card_value = {
        1: pygame.image.load(os.path.join('card', 'spade_ace.png')),
        2: pygame.image.load(os.path.join('card', 'spade_two.png')),
        3: pygame.image.load(os.path.join('card', 'spade_three.png')),
        4: pygame.image.load(os.path.join('card', 'spade_four.png')),
        5: pygame.image.load(os.path.join('card', 'spade_five.png')),
        6: pygame.image.load(os.path.join('card', 'spade_six.png')),
        7: pygame.image.load(os.path.join('card', 'spade_seven.png')),
        8: pygame.image.load(os.path.join('card', 'spade_eight.png')),
        9: pygame.image.load(os.path.join('card', 'spade_nine.png')),
        10: pygame.image.load(os.path.join('card', 'spade_ten.png')),
        11: pygame.image.load(os.path.join('card', 'spade_jack.png')),
        12: pygame.image.load(os.path.join('card', 'spade_queen.png')),
        13: pygame.image.load(os.path.join('card', 'spade_king.png')),

        14: pygame.image.load(os.path.join('card', 'club_ace.png')),
        15: pygame.image.load(os.path.join('card', 'club_two.png')),
        16: pygame.image.load(os.path.join('card', 'club_three.png')),
        17: pygame.image.load(os.path.join('card', 'club_four.png')),
        18: pygame.image.load(os.path.join('card', 'club_five.png')),
        19: pygame.image.load(os.path.join('card', 'club_six.png')),
        20: pygame.image.load(os.path.join('card', 'club_seven.png')),
        21: pygame.image.load(os.path.join('card', 'club_eight.png')),
        22: pygame.image.load(os.path.join('card', 'club_nine.png')),
        23: pygame.image.load(os.path.join('card', 'club_ten.png')),
        24: pygame.image.load(os.path.join('card', 'club_jack.png')),
        25: pygame.image.load(os.path.join('card', 'club_queen.png')),
        26: pygame.image.load(os.path.join('card', 'club_king.png')),

        27: pygame.image.load(os.path.join('card', 'heart_ace.png')),
        28: pygame.image.load(os.path.join('card', 'heart_two.png')),
        29: pygame.image.load(os.path.join('card', 'heart_three.png')),
        30: pygame.image.load(os.path.join('card', 'heart_four.png')),
        31: pygame.image.load(os.path.join('card', 'heart_five.png')),
        32: pygame.image.load(os.path.join('card', 'heart_six.png')),
        33: pygame.image.load(os.path.join('card', 'heart_seven.png')),
        34: pygame.image.load(os.path.join('card', 'heart_eight.png')),
        35: pygame.image.load(os.path.join('card', 'heart_nine.png')),
        36: pygame.image.load(os.path.join('card', 'heart_ten.png')),
        37: pygame.image.load(os.path.join('card', 'heart_jack.png')),
        38: pygame.image.load(os.path.join('card', 'heart_queen.png')),
        39: pygame.image.load(os.path.join('card', 'heart_king.png')),

        40: pygame.image.load(os.path.join('card', 'diamond_ace.png')),
        41: pygame.image.load(os.path.join('card', 'diamond_two.png')),
        42: pygame.image.load(os.path.join('card', 'diamond_three.png')),
        43: pygame.image.load(os.path.join('card', 'diamond_four.png')),
        44: pygame.image.load(os.path.join('card', 'diamond_five.png')),
        45: pygame.image.load(os.path.join('card', 'diamond_six.png')),
        46: pygame.image.load(os.path.join('card', 'diamond_seven.png')),
        47: pygame.image.load(os.path.join('card', 'diamond_eight.png')),
        48: pygame.image.load(os.path.join('card', 'diamond_nine.png')),
        49: pygame.image.load(os.path.join('card', 'diamond_ten.png')),
        50: pygame.image.load(os.path.join('card', 'diamond_jack.png')),
        51: pygame.image.load(os.path.join('card', 'diamond_queen.png')),
        0: pygame.image.load(os.path.join('card', 'diamond_king.png'))
    }
    player_cursor = pygame.image.load(os.path.join('card', 'player_cursor.png'))
    player_cursor.set_colorkey((255, 255, 255))

    # text
    text = {}
    for font_size in range(10, 210, 10):
        text[font_size] = pygame.font.SysFont('Comic Sans MS', font_size)

    def __init__(self, screen, split: int, position: tuple[int, int], bet_size: int, card_deck: list,
                 num: int = 0, split_card: int = -1):
        self.screen = screen
        self.split = split
        self.position = position
        self.x_pos = position[0]
        self.y_pos = position[1] - num * 200
        self.bet_size = bet_size

        self.card: [int] = []
        if self.split == 0 or self.split == -1:  # split not done (0) or dealer (-1)
            self.deal(card_deck)
            self.deal(card_deck)
        elif split > 0:  # split hand
            self.card.append(split_card)
            self.deal(card_deck)
        self.value = self.calculate_hand(self.card)

    def draw(self, game_stage, dealer_cards, hand_turn: bool):
        if game_stage >= 1:
            if hand_turn:  # cursor to show which hand's turn
                self.screen.blit(self.player_cursor, (self.x_pos - 130, self.y_pos + 20))
            # cards
            self.draw_card()
            # hand value
            self.screen.blit(self.text[40].render(f"{self.value}", False, 'Black'),
                             (-105 + self.x_pos, -55 + self.y_pos))
            # bet size
            self.screen.blit(self.text[30].render(f"Bet: {self.bet_size}", False, 'Black'),
                             (self.x_pos - 100, self.y_pos + 100))

            # busted
            if self.value > 21:
                self.screen.blit(self.text[40].render("BUSTED!", False, 'Black'),
                                 (-45 + self.x_pos, -55 + self.y_pos))
                return
            # bet result
            if game_stage >= 2:
                dealer_hand = Hand.calculate_hand(dealer_cards)

                # player got blackjack
                if self.value == 21 and len(self.card) == 2:
                    if dealer_hand == 21 and len(dealer_cards) == 2:  # dealer also blackjack --> tie
                        self.screen.blit(self.text[40].render("DRAW!", False, 'Black'),
                                         (-45 + self.x_pos, -55 + self.y_pos))
                    else:  # dealer not blackjack, player won
                        self.screen.blit(self.text[40].render("BLACKJACK!!!", False, 'Black'),
                                         (-45 + self.x_pos, -55 + self.y_pos))

                # player not blackjack (possibly 21), dealer got blackjack
                elif dealer_hand == 21 and len(dealer_cards) == 2:
                    self.screen.blit(self.text[40].render("Lose", False, 'Black'),
                                     (-45 + self.x_pos, -55 + self.y_pos))

                # both player and dealer don't have blackjack
                else:
                    if dealer_hand == self.value:  # tie
                        self.screen.blit(self.text[40].render("DRAW!", False, 'Black'),
                                         (-45 + self.x_pos, -55 + self.y_pos))
                    elif dealer_hand > 21 or dealer_hand < self.value < 22:  # player win
                        self.screen.blit(self.text[40].render("WIN!", False, 'Black'),
                                         (-45 + self.x_pos, -55 + self.y_pos))
                    else:  # player lost
                        self.screen.blit(self.text[40].render("Lose", False, 'Black'),
                                         (-45 + self.x_pos, -55 + self.y_pos))

    def draw_card(self):
        card_num = len(self.card)
        for i, card in enumerate(self.card):
            self.screen.blit(self.card_value[card], (134 / card_num * i - 105 + self.x_pos, self.y_pos))

    def deal(self, card_deck):
        deal(card_deck, self.card)
        self.value = self.calculate_hand(self.card)

    def double_down(self, money, card_deck):
        self.bet_size *= 2
        self.deal(card_deck)
        return money - self.bet_size // 2

    def can_be_split(self) -> bool:  # return whether the hand can be split
        return len(self.card) == 2 and self.split < 2 \
               and (self.card[0] % 13 == self.card[1] % 13 or (not 0 < self.card[0] % 13 < 10
                                                               and not 0 < self.card[1] % 13 < 10))

    def bet_result(self, dealer_card) -> int:
        dealer_value = self.calculate_hand(dealer_card)
        if self.value > 21:  # if busted
            return 0
        else:
            if self.value == 21 and len(self.card) == 2:  # player got blackjack
                if dealer_value == 21 and len(dealer_card) == 2:  # dealer also got blackjack --> tie
                    return self.bet_size
                else:  # win 1.5 bet
                    return self.bet_size // 2 * 5

            elif not (dealer_value == 21 and len(dealer_card) == 2):  # dealer not blackjack
                if dealer_value == self.value:  # tie
                    return self.bet_size
                elif dealer_value > 21 or dealer_value < self.value < 22:  # win
                    return self.bet_size * 2
                else:  # lost
                    return 0
            else:  # player not blackjack (possibly 21), dealer blackjack
                return 0

    @staticmethod
    # calculate hand value
    def calculate_hand(cards):
        hand = 0
        ace_in_hand = False

        for card in cards:
            if 0 < card % 13 < 11:
                hand += card % 13
            else:
                hand += 10

        for card in cards:
            if card % 13 == 1:
                ace_in_hand = True

        if ace_in_hand and hand < 12:
            return hand + 10
        else:
            return hand
