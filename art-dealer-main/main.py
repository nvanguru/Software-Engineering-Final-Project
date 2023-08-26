import pygame
from sys import exit
from player import Player, Dealer
from button import blit_text_with_center, InflatableButton, ColorChangeButton, SettingsButton


def settings_screen():
    # button variables
    help_menu_button_pos = (WIDTH // 2, HEIGHT // 10 * 3)
    help_menu_button = InflatableButton(50, 'Help Menu', help_menu_button_pos)
    title_screen_button_pos = (WIDTH // 2, HEIGHT // 10 * 5)
    title_screen_button = InflatableButton(50, 'Title Screen', title_screen_button_pos)
    resume_button_pos = (WIDTH // 2, HEIGHT // 10 * 7)
    resume_button = InflatableButton(50, 'Resume', resume_button_pos)

    while True:
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.quit()
                exit()

            # mouse input
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if help_menu_button.is_clicked():
                    help_menu_screen()

                elif title_screen_button.is_clicked():
                    return False

                elif resume_button.is_clicked():
                    return True

        # generate screen
        screen.blit(background, (0, 0))
        help_menu_button.draw(screen)
        title_screen_button.draw(screen)
        resume_button.draw(screen)

        pygame.display.update()
        clock.tick(FPS)


def help_menu_screen() -> None:
    while True:
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.quit()
                exit()

            # exit help menu
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] \
                    or event.type == pygame.KEYDOWN and event.key == pygame.K_h \
                    or event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return

        # generate screen
        screen.blit(background, (0, 0))
        screen.blit(text[50].render("New game: left click / space", False, 'Black'), (WIDTH // 5, HEIGHT // 10 + 50))
        screen.blit(text[50].render("Hit: left click / space", False, 'Black'), (WIDTH // 5, HEIGHT // 10 + 150))
        screen.blit(text[50].render("Stand: right click / S", False, 'Black'), (WIDTH // 5, HEIGHT // 10 + 250))
        screen.blit(text[50].render("Help: H", False, 'Black'), (WIDTH // 5, HEIGHT // 10 + 350))
        screen.blit(text[50].render("Split: V", False, 'Black'), (WIDTH // 5, HEIGHT // 10 + 450))
        screen.blit(text[50].render("Double Down: D", False, 'Black'), (WIDTH // 5, HEIGHT // 10 + 550))
        screen.blit(text[50].render("Quit: Q", False, 'Black'), (WIDTH // 5, HEIGHT // 10 + 650))

        pygame.display.update()
        clock.tick(FPS)


def title_screen() -> None:
    # button variables
    start_game_button_pos = (WIDTH // 2, HEIGHT // 40 * 19)
    start_game_button = InflatableButton(50, 'Start Game', start_game_button_pos)
    help_menu_button_pos = (WIDTH // 2, HEIGHT // 40 * 19 + 150)
    help_menu_button = InflatableButton(50, 'Help', help_menu_button_pos)
    quit_button_pos = (WIDTH // 2, HEIGHT // 40 * 19 + 300)
    quit_button = InflatableButton(50, 'Quit Game', quit_button_pos)

    while True:
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # mouse input
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_game_button.is_clicked():
                    return

                elif help_menu_button.is_clicked():
                    help_menu_screen()

                elif quit_button.is_clicked():
                    pygame.quit()
                    exit()

            # keyboard input
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()

                elif event.key == pygame.K_h:
                    help_menu_screen()

        # generate screen
        screen.blit(background, (0, 0))
        blit_text_with_center(screen, 100, "BLACKJACK", (WIDTH // 2, HEIGHT // 5))
        start_game_button.draw(screen)
        help_menu_button.draw(screen)
        quit_button.draw(screen)

        pygame.display.update()
        clock.tick(FPS)


def choose_player_num_screen() -> int:
    player_num = 3  # default player number

    # button variables
    plus_player_num_button_pos = (WIDTH // 2 + 100, HEIGHT // 2)
    plus_player_num_button = ColorChangeButton(100, '+', plus_player_num_button_pos)
    minus_player_num_button_pos = (WIDTH // 2 - 100, HEIGHT // 2)
    minus_player_num_button = ColorChangeButton(100, '-', minus_player_num_button_pos)
    start_game_button_pos = (WIDTH // 2, HEIGHT // 4 * 3)
    start_game_button = InflatableButton(70, "Start Game", start_game_button_pos)

    while True:
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # keyboard input
            elif event.type == pygame.KEYDOWN:
                # choose player number
                if event.key == pygame.K_1:
                    return 1
                elif event.key == pygame.K_2:
                    return 2
                elif event.key == pygame.K_3:
                    return 3
                elif event.key == pygame.K_4:
                    return 4
                elif event.key == pygame.K_5:
                    return 5
                elif event.key == pygame.K_6:
                    return 6
                elif event.key == pygame.K_7:
                    return 7

                # to help screen
                elif event.key == pygame.K_h:
                    help_menu_screen()

                # quit game
                elif event.key == pygame.K_q:
                    pygame.quit()
                    exit()

            # mouse input
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if plus_player_num_button.is_clicked() and player_num < 7:
                    player_num += 1

                elif minus_player_num_button.is_clicked() and player_num > 1:
                    player_num -= 1

                elif start_game_button.is_clicked():
                    return player_num

        # generate screen
        screen.blit(background, (0, 0))
        blit_text_with_center(screen, 80, "Choose number of players", (WIDTH // 2, HEIGHT // 5))
        blit_text_with_center(screen, 150, str(player_num), (WIDTH // 2, HEIGHT // 2))
        plus_player_num_button.draw(screen)
        minus_player_num_button.draw(screen)
        start_game_button.draw(screen)

        pygame.display.update()
        clock.tick(FPS)


def game_screen(player_num):
    # game variables
    game_stage = 0  # 0: betting stage, 1: hit/stand stage, 2: result stage
    player_list: [Player] = []
    for i in range(player_num):
        player_list.append(Player(screen, i, player_num, WIDTH, HEIGHT))
    player_turn = 0
    card_deck = list(range(1, 52 * 4 + 1))
    dealer = Dealer(screen, (WIDTH // 2, HEIGHT // 6))

    # button variables
    settings_button = SettingsButton((70, 70), 45)

    while True:
        # betting stage
        if game_stage == 0:
            for event in pygame.event.get():
                # quit game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                # keyboard input
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h:
                        help_menu_screen()

                    elif event.key == pygame.K_q:
                        pygame.quit()
                        exit()

                # mouse input
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if settings_button.is_clicked():
                        if not settings_screen():  # if player clicked title screen button in settings screen
                            return 1
                        break

                # take turn betting
                player_turn = player_list[player_turn].choose_bet_size(event, player_turn, game_stage)
                if player_turn == player_num:  # when every player is done
                    player_turn = 0
                    game_stage += 1

                    # deal
                    for player in player_list:
                        player.initial_deal(card_deck)
                    dealer.initial_deal(card_deck)

            # generate screen
            screen.blit(background, (0, 0))
            settings_button.draw(screen, background_color)
            blit_text_with_center(screen, 50, "Choose your bet size", (dealer.position[0], dealer.position[1] - 40))
            blit_text_with_center(screen, 30, "1: $500", (dealer.position[0], dealer.position[1] + 30))
            blit_text_with_center(screen, 30, "2: $1000", (dealer.position[0], dealer.position[1] + 100))
            blit_text_with_center(screen, 30, "3: $2000", (dealer.position[0], dealer.position[1] + 170))

            for player in player_list:  # draw players
                player.draw(game_stage, dealer, player_turn)

            pygame.display.update()
            clock.tick(FPS)

        # hit/stand stage
        elif game_stage == 1:
            for event in pygame.event.get():
                # quit game
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    pygame.quit()
                    exit()

                # keyboard input
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h:
                        help_menu_screen()

                # mouse input
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if settings_button.is_clicked():
                        if not settings_screen():
                            return 1
                        break

                # player action
                player_turn = player_list[player_turn].hit_stand(event, player_turn, card_deck, game_stage)
                if player_turn == player_num:  # when every player is done
                    player_turn = 0
                    game_stage += 1

                    try:  # if every player is busted --> no dealer deal
                        for player in player_list:
                            if not player.is_bankrupted():
                                for hand in player.hand:
                                    if hand.value < 22:
                                        dealer.final_deal(card_deck)
                                        raise AssertionError
                    except AssertionError:
                        pass

                    for player in player_list:  # players get result
                        player.bet_result(dealer.hand[0].card)

            # generate screen
            screen.blit(background, (0, 0))
            settings_button.draw(screen, background_color)
            for player in player_list:  # draw players
                player.draw(game_stage, dealer, player_turn)
            dealer.draw(game_stage, player_list)  # draw dealer

            pygame.display.update()
            clock.tick(FPS)

        # result stage
        elif game_stage == 2:
            for event in pygame.event.get():
                # quit game
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    pygame.quit()
                    exit()

                # keyboard input
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h:
                        help_menu_screen()

                # mouse input
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if settings_button.is_clicked():
                        if not settings_screen():
                            return 1
                        break

                # to next game, initialize
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] \
                        or event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_stage = 0
                    card_deck = list(range(1, 52 * 4 + 1))
                    for player in player_list:
                        player.initialize()
                    dealer.initialize()

                    for player in player_list:
                        if not player.is_bankrupted():
                            break
                    else:  # if every player is bankrupted
                        game_over_screen()
                        return 1  # go to title screen

            # generate screen
            screen.blit(background, (0, 0))
            settings_button.draw(screen, background_color)
            for player in player_list:  # draw players
                player.draw(game_stage, dealer, player_turn)
            dealer.draw(game_stage, player_list)  # draw dealer

            pygame.display.update()
            clock.tick(FPS)


def game_over_screen():
    # button variables
    title_screen_button_pos = (WIDTH // 2, HEIGHT // 10 * 5)
    title_screen_button = InflatableButton(50, 'Title Screen', title_screen_button_pos)
    quit_button_pos = (WIDTH // 2, HEIGHT // 10 * 7)
    quit_button = InflatableButton(50, 'Quit Game', quit_button_pos)

    while True:
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # mouse input
            if event.type == pygame.MOUSEBUTTONDOWN:
                if title_screen_button.is_clicked():
                    return
                elif quit_button.is_clicked():
                    pygame.quit()
                    exit()

            # keyboard input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()

                elif event.key == pygame.K_h:
                    help_menu_screen()

        # generate screen
        screen.blit(background, (0, 0))
        blit_text_with_center(screen, 100, "Game Over", (WIDTH // 2, HEIGHT // 4))
        title_screen_button.draw(screen)
        quit_button.draw(screen)

        pygame.display.update()
        clock.tick(FPS)


def main():
    # game variables
    run_screen = {
        1: title_screen,
        2: choose_player_num_screen,
        3: game_screen
    }
    game_screen_num = 1
    player_num = 0

    # event loop
    while True:
        # title_screen
        if game_screen_num == 1:
            run_screen[1]()
            game_screen_num += 1

        # choose_player_num_screen
        elif game_screen_num == 2:
            player_num = run_screen[2]()
            game_screen_num += 1

        # game_screen
        elif game_screen_num == 3:
            game_screen_num = run_screen[3](player_num)


if __name__ == '__main__':
    pygame.init()

    # set screen size
    WIDTH = 1680
    HEIGHT = 1050
    screen_size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(screen_size)

    # set caption
    pygame.display.set_caption("BLACKJACK")

    # set frame rate
    FPS = 100
    clock = pygame.time.Clock()

    # set background
    background = pygame.Surface(screen_size)
    background_color = 'gray74'
    background.fill(background_color)

    # text with different sizes
    text = {}
    for font_size in range(10, 210, 10):
        text[font_size] = pygame.font.SysFont('Comic Sans MS', font_size)

    main()
