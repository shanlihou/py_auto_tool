import pygame
import utils
import ui_base
import global_data

class Editor(ui_base.UIBase):
    def __init__(self, win_idx, rect):
        self.rect = rect
        self.win_idx = win_idx
        self.is_active = False
        self.text = ""
        global_data.EVENT_MGR.register_cb(pygame.MOUSEBUTTONDOWN, self.on_mouse_down)
        global_data.EVENT_MGR.register_cb(pygame.KEYDOWN, self.on_key_down)

    def on_mouse_down(self, pos):
        if self.is_pos_in(pos):
            self.is_active = True
        else:
            self.is_active = False

    def on_key_down(self, key):
        if self.is_active:
            if key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif key == pygame.K_RETURN:
                self.is_active = False
            else:
                self.text += chr(key)

        print(self.text)

    def draw(self, draw_ctx):
        _rect = utils.get_screen_rect(self.win_idx, self.rect)
        boder_width = 3 if self.is_active else 1
        pygame.draw.rect(draw_ctx.screen, (0, 255, 0), _rect, boder_width)


        x, y, w, h = _rect

        font = utils.get_font(h)
        text = font.render(self.text, True, (0, 0, 255), (0, 255, 0))
        draw_ctx.screen.blit(text, (x + 5, y + 5))



