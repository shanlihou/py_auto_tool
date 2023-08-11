import similar_ratio
import debug_panel


class UIMgr(object):
    def __init__(self) -> None:
        self.components = []

        self.add_component(similar_ratio.SimilarRatio())
        self.add_component(debug_panel.DebugPanel())

    def add_component(self, component):
        self.components.append(component)

    def draw(self, draw_ctx):
        for component in self.components:
            component.draw(draw_ctx)


