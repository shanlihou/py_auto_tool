import similar_ratio
import debug_panel
import editor
import ui_text
import choicer
import global_data


from custom_ui import cap_choicer, custom_ana, ui_find_img, console_editor, pic_editor


class UIMgr(object):
    def __init__(self) -> None:
        self.components = {}
        self.tag_to_component = {}

        # sim_ratio
        _rect = (0.85, 0.1, 0.05, 0.8)
        self.add_component(similar_ratio.SimilarRatio(0, _rect), 'sim')

        # debug_panel
        self.add_component(debug_panel.DebugPanel(), 'dbg')

        # editor for debug
        _rect = (0.03, 0.04, 0.94, 0.1)
        self.add_component(console_editor.ConsoleEditor(1, _rect), 'dbg_editor')

        # text for debug
        _rect = (0.03, 0.16, 0.94, 0.7)
        _text = ui_text.Text(1, _rect)
        self.add_component(_text, 'dbg_text')
        global_data.DBG_TEXT_ID = _text.id

        # captrue pages
        _widget = custom_ana.CustomAna()
        self.add_component(_widget, 'custom_ana')

        # cap_choicer
        _cap_choices = ['run', 'stop']
        _cap_choice = cap_choicer.CapChoicer(1, (0.03, 0.03, 0.47, 0.1), _cap_choices, True)
        self.add_component(_cap_choice, 'cap_choice')

        # find_img
        _widget = ui_find_img.FindImg()
        self.add_component(_widget, 'ui_find_img')

        # pic editor
        _rect = (0.03, 0.04, 0.47, 0.1)
        _widget = pic_editor.PicEditor(1, _rect)
        self.add_component(_widget, 'pic_editor')

        # init pages
        self.pages = {
            'console': ['dbg_editor', 'dbg_text'],
            'color_picker': ['cap_choice', 'custom_ana'],
            'find_img': ['ui_find_img', 'pic_editor', 'sim'],
            'none': [],
        }

        # choice
        _choices = list(self.pages.keys())
        _choice = choicer.Choicer(1, (0.03, 0.87, 0.94, 0.1), _choices, True)
        self.add_component(_choice, 'choice')
        _choice.on_choice_changed = self.on_choice_changed

        self.on_choice_changed('console')

    def on_choice_changed(self, choice):
        for page_name, page_tags in self.pages.items():
            if page_name == choice:
                for tag in page_tags:
                    self.tag_to_component[tag].set_visible(True)
            else:
                for tag in page_tags:
                    self.tag_to_component[tag].set_visible(False)

    def generate_id(self):
        for i in range(100000):
            if i not in self.components:
                return i

    def add_component(self, component, tag):
        _id = self.generate_id()
        component.set_id(_id)
        self.components[_id] = component
        self.tag_to_component[tag] = component

    def draw(self, draw_ctx):
        for component in self.components.values():
            if not component.is_visible:
                continue

            component.draw(draw_ctx)

    def get_ui(self, id):
        return self.components[id]

    

