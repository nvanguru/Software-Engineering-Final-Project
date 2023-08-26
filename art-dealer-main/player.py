import pygame
import math
import os
from hand import Hand

pygame.init()


class Person:
    # image variable
    player_cursor = pygame.image.load(os.path.join('card', 'player_cursor.png'))
    player_cursor.set_colorkey((255, 255, 255))

    # text variable
    text = {}
    for font_size in range(10, 210, 10):
        text[font_size] = pygame.font.SysFont('Comic Sans MS', font_size)

    def __init__(self, screen, position):
        self.screen = screen
        self.hand: list[Hand] = []
        self.position = position
        self.x_pos = position[0]
        self.y_pos = position[1]


class Player(Person):
    def __init__(self, screen, player, total_player, width, height):
        deg = math.pi * 3 / 4 - (math.pi / (total_player * 4)) - (math.pi / (total_player * 4)) * player * 2
        diagonal = (width**2 + height**2)**(1/2)
        super().__init__(screen, (width//2 + diagonal*5*math.cos(deg) // 9, -height//3 + diagonal*5*math.sin(deg) // 9))
        self.player_num = player
        self.money = 10000
        self.bet_size = 0
        self.hand_turn = 0
        self.bankrupted = False

    def draw(self, game_stage, dealer, player_turn):
        # money
        self.screen.blit(self.text[30].render(f"Money: {self.money}", False, 'Black'),
                         (self.x_pos - 100, self.y_pos + 150))

        # bankrupted
        if self.is_bankrupted():
            self.screen.blit(self.text[50].render('Bankrupted', False, 'Black'), (self.x_pos - 105, 35 + self.y_pos))

        else:
            if game_stage == 0:  # betting stage
                if player_turn == self.player_num:  # cursor to show which hand's turn
                    self.screen.blit(self.player_cursor, (self.x_pos - 130, self.y_pos + 140))
                # bet size
                self.screen.blit(self.text[30].render(f"Bet: {self.bet_size}", False, 'Black'),
                                 (self.x_pos - 100, self.y_pos + 100))

            if game_stage >= 1:  # hit/stand, result stage
                for hand_num, hand in enumerate(self.hand):
                    hand_turn = self.player_num == player_turn and self.hand_turn == hand_num
                    hand.draw(game_stage, dealer.hand[0].card, hand_turn)

    def choose_bet_size(self, event, player_turn, game_stage):
        if not game_stage == 0:  # if not betting stage
            return player_turn

        elif self.is_bankrupted():
            return player_turn + 1

        else:
            # keyboard input
            if event.type == pygame.KEYDOWN:
                # bet size 500 selected
                if event.key == pygame.K_1:
                    if self.money >= 500:
                        self.bet_size = 500
                        self.money -= self.bet_size
                        return player_turn + 1
                    else:  # not enough money --> all in
                        self.bet_size = self.money
                        self.money -= self.bet_size
                        return player_turn + 1

                # bet size 1000 selected
                elif event.key == pygame.K_2 and self.money >= 1000:
                    self.bet_size = 1000
                    self.money -= self.bet_size
                    return player_turn + 1

                # bet size 2000 selected
                elif event.key == pygame.K_3 and self.money >= 2000:
                    self.bet_size = 2000
                    self.money -= self.bet_size
                    return player_turn + 1
                else:
                    return player_turn
            else:
                return player_turn

    def initial_deal(self, card_deck):
        if self.money >= 0:
            self.hand.append(Hand(self.screen, 0, self.position, self.bet_size, card_deck))

    def turn_end(self, player_turn):
        if self.hand_turn >= len(self.hand):  # action done for all hands
            self.hand_turn = 0
            return player_turn + 1
        else:
            return player_turn

    def hit_stand(self, event, player_turn, card_deck, game_stage):
        if not game_stage == 1:  # if not hit/stand stage
            return player_turn

        elif self.is_bankrupted():
            return player_turn + 1

        elif self.hand[self.hand_turn].value >= 21:  # if this hand value is 21
            self.hand_turn += 1
            return self.turn_end(player_turn)

        else:
            # hit
            if pygame.mouse.get_pressed()[0] or event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.hand[self.hand_turn].deal(card_deck)
                return self.turn_end(player_turn)

            # stand
            elif pygame.mouse.get_pressed()[2] or event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                self.hand_turn += 1
                return self.turn_end(player_turn)

            # double down
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_d \
                    and len(self.hand[self.hand_turn].card) == 2 \
                    and self.money >= self.bet_size:
                self.money = self.hand[self.hand_turn].double_down(self.money, card_deck)
                self.hand_turn += 1
                return self.turn_end(player_turn)

            # split
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_v \
                    and self.hand[self.hand_turn].can_be_split()\
                    and self.money >= self.bet_size:
                self.hand.append(Hand(self.screen, self.hand[self.hand_turn].split + 1, self.position,
                                      self.bet_size, card_deck, num=len(self.hand),
                                      split_card=self.hand[self.hand_turn].card.pop(1)))
                self.hand[self.hand_turn].split += 1
                self.hand[self.hand_turn].deal(card_deck)
                self.money -= self.bet_size
                return self.turn_end(player_turn)

            else:
                return self.turn_end(player_turn)

    def bet_result(self, dealer_card):
        for hand in self.hand:
            self.money += hand.bet_result(dealer_card)

    def is_bankrupted(self):
        return self.bankrupted

    def initialize(self):
        self.hand = []
        self.bet_size = 0
        self.hand_turn = 0

        if self.money <= 0:
            self.bankrupted = True


class Dealer(Person):
    card_back = pygame.image.load(os.path.join('card', 'card_back.png'))

    def __init__(self, screen, position):
        super().__init__(screen, position)
        self.hand: [Hand] = []

    def draw(self, game_stage, player_list):
        if game_stage >= 1:
            # cards
            self.hand[0].draw_card()

            # betting stage, hide first card
            if game_stage == 1:
                self.screen.blit(self.card_back, (134 / len(self.hand[0].card) - 105 + self.x_pos, self.y_pos))

            # hit/stand, result stage
            elif game_stage >= 2:
                if len(self.hand[0].card) == 2:  # if dealer have only two cards, hide first card
                    self.screen.blit(self.card_back, (134 / len(self.hand[0].card) - 105 + self.x_pos, self.y_pos))

                    # draw front and show dealer hand value, if one of the players is not busted
                    for player in player_list:
                        if not player.is_bankrupted():
                            for hand in player.hand:
                                if hand.value < 22:
                                    self.screen.blit(Hand.card_value[self.hand[0].card[1]],
                                                     (134 / len(self.hand[0].card) - 105 + self.x_pos, self.y_pos))
                                    self.screen.blit(self.text[40].render(f"{self.hand[0].value}", False, 'Black'),
                                                     (-105 + self.x_pos, -55 + self.y_pos))

                else:  # if dealer have more than 3 cards, no need to hide first card, just show dealer hand value
                    self.screen.blit(self.text[40].render(f"{self.hand[0].value}", False, 'Black'),
                                     (-105 + self.x_pos, -55 + self.y_pos))

    def initial_deal(self, card_deck):
        self.hand.append(Hand(self.screen, -1, self.position, -1, card_deck))

    def final_deal(self, card_deck):
        while True:
            if self.hand[0].value > 16:
                return self.hand[0].value

            self.hand[0].deal(card_deck)

    def initialize(self):
        self.hand = []
