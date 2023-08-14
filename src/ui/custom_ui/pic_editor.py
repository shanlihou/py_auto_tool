import editor
import global_data


class PicEditor(editor.Editor):
    def on_return_press(self, text):
        print(text)
        global_data.DEBUG_TARGET = text


