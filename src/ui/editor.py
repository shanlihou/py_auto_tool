import pygame
import utils
import ui_base
import global_data
import pygame
import const

class Editor(ui_base.UIBase):
    def __init__(self, win_idx, rect):
        super(Editor, self).__init__(win_idx, rect)
        self.is_active = False
        self.text = ""
        global_data.EVENT_MGR.register_cb(pygame.MOUSEBUTTONDOWN, self.on_mouse_down)
        global_data.EVENT_MGR.register_cb(pygame.KEYDOWN, self.on_key_down)

    def on_mouse_down(self, pos):
        if not self.is_visible:
            self.is_active = False
            return

        if self.is_pos_in(pos):
            self.is_active = True
        else:
            self.is_active = False

    def translate_with_shift(self, key):
        if key.isalpha():
            return key.upper()

        return {
            '=': '+',
            '-': '_',
        }.get(key, '')

    def on_key_down(self, key):
        if self.is_active:
            _key = pygame.key.name(key)
            if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                _key = self.translate_with_shift(_key)

            if key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif key == pygame.K_SPACE:
                self.text += ' '
            elif key == pygame.K_RETURN:
                self.on_return_press(self.text)
                self.text = ""
            else:
                self.text += _key

    def draw(self, draw_ctx):
        _rect = utils.get_screen_rect(self.win_idx, self.rect)
        boder_width = 3 if self.is_active else 1
        pygame.draw.rect(draw_ctx.screen, const.COLOR_GREEN, _rect, boder_width, border_radius=10)

        x, y, w, h = _rect

        off = 5

        font_size = h - off * 2

        font = utils.get_font(font_size)
        text = font.render(self.text, True, const.COLOR_GREEN, const.COLOR_BG)
        draw_ctx.screen.blit(text, (x + off, y + off))



