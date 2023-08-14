import editor
import global_data


class ConsoleEditor(editor.Editor):
    def on_return_press(self, text):
        try:
            ret = exec(text)
        except Exception as e:
            ret = e

        global_data.UI_MGR.get_ui(global_data.DBG_TEXT_ID).lines.append(str(ret))
