import choicer
import global_data


class CapChoicer(choicer.Choicer):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.on_choice_changed = self._on_choice_changed

    def _on_choice_changed(self, choice: str) -> None:
        if choice == 'run':
            global_data.CAPTURE = True
        else:
            global_data.CAPTURE = False

