import pygame
import math

text = {}
for font_size in range(10, 210, 10):
    text[font_size] = pygame.font.SysFont('Comic Sans MS', font_size)


class SettingsButton:
    def __init__(self, position: tuple[int, int], radius):
        self.position = position
        self.radius = radius
        self.left = position[0] - radius
        self.right = position[0] + radius
        self.top = position[1] - radius
        self.bottom = position[1] + radius
        self.width = self.height = 2 * radius

    def draw(self, screen, background_color, color='black'):
        # draw four rectangle with 45 degree difference and circle at center
        for i in range(4):
            rect = math.pi / 4 * i
            thick = math.pi / 11.5
            pygame.draw.polygon(screen, color, [(math.cos(rect + thick) * self.radius + self.position[0],
                                                 math.sin(rect + thick) * self.radius + self.position[1]),
                                                (math.cos(rect - thick) * self.radius + self.position[0],
                                                 math.sin(rect - thick) * self.radius + self.position[1]),
                                                (-math.cos(rect + thick) * self.radius + self.position[0],
                                                 -math.sin(rect + thick) * self.radius + self.position[1]),
                                                (-math.cos(rect - thick) * self.radius + self.position[0],
                                                 -math.sin(rect - thick) * self.radius + self.position[1])])
        pygame.draw.circle(screen, background_color, self.position, self.radius / 2.7)

    def mouse_hovering(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.left <= mouse_pos[0] <= self.right and self.top <= mouse_pos[1] <= self.bottom

    def is_clicked(self): return self.mouse_hovering() and pygame.mouse.get_pressed()[0]


class TextButton:
    def __init__(self, text_size: int, message: str, position: tuple[int, int], color='Black'):
        self.text_size = text_size
        self.message = message
        self.color = color
        self.text = text[text_size].render(message, False, color)
        self.position = position
        self.rect = self.text.get_rect(center=(position[0], position[1]))

    def mouse_hovering(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.x <= mouse_pos[0] <= self.rect.x + self.rect.width and \
            self.rect.y <= mouse_pos[1] <= self.rect.y + self.rect.height

    def is_clicked(self): return self.mouse_hovering() and pygame.mouse.get_pressed()[0]


class ColorChangeButton(TextButton):
    def __init__(self, text_size: int, message: str, position: tuple[int, int]):  # x,y is the center of the text
        super().__init__(text_size, message, position)

    def draw(self, screen):
        if self.mouse_hovering():
            blit_text_with_center(screen, self.text_size, self.message, self.position, 'blue')
        else:
            blit_text_with_center(screen, self.text_size, self.message, self.position, 'Black')


class InflatableButton(TextButton):
    def __init__(self, text_size: int, message: str, position: tuple[int, int]):  # x,y is the center of the text
        super().__init__(text_size, message, position)
        self.is_inflated = False

    def draw(self, screen):
        self.change_size()
        blit_text_with_center(screen, self.text_size, self.message, self.position)

    def change_size(self):
        if self.mouse_hovering() and not self.is_inflated:
            self.is_inflated = True
            self.inflate()

        elif not self.mouse_hovering() and self.is_inflated:
            self.is_inflated = False
            self.deflate()

    def inflate(self):
        self.text_size += 10
        self.text = text[self.text_size + 10].render(self.message, False, self.color)
        self.rect = self.text.get_rect(center=self.position)

    def deflate(self):
        self.text_size -= 10
        self.text = text[self.text_size].render(self.message, False, self.color)
        self.rect = self.text.get_rect(center=self.position)


def blit_text_with_center(screen, text_size: int, message: str, position: tuple[int, int], color='Black'):
    t = text[text_size].render(message, False, color)
    t_rect = t.get_rect(center=(position[0], position[1]))
    screen.blit(t, (t_rect.x, t_rect.y))
