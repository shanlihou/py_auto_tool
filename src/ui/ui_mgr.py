import similar_ratio
import debug_panel
import editor


class UIMgr(object):
    def __init__(self) -> None:
        self.components = []
        _rect = (0.85, 0.1, 0.05, 0.8)
        self.add_component(similar_ratio.SimilarRatio(0, _rect))
        self.add_component(debug_panel.DebugPanel())
        _rect = (0.03, 0.04, 0.94, 0.1)
        self.add_component(editor.Editor(1, _rect))

    def add_component(self, component):
        self.components.append(component)

    def draw(self, draw_ctx):
        for component in self.components:
            component.draw(draw_ctx)


