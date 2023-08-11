import click_effect
import pygame


class EffectMgr(object):
    def __init__(self) -> None:
        self.effects = {}

    def generate_id(self):
        for i in range(100000):
            if i not in self.effects:
                return i

    def add_effect(self, effect):
        self.effects[effect.effect_id] = effect

    def draw(self, draw_ctx):
        for effect in list(self.effects.values()):
            effect.draw(draw_ctx)

    def add_click_effect(self, pos):
        effect_id = self.generate_id()
        effect = click_effect.ClickEffect(effect_id, pos, pygame.time.get_ticks())
        self.add_effect(effect)
    
    def remove_effect(self, effect_id):
        del self.effects[effect_id]

