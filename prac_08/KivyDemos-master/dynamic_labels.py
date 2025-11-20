
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabels(App):
    """Create a main program."""

    def __init__(self, **kwargs):
        """Initialise the Dynamic Labels App."""
        super().__init__(**kwargs)
        self.names = ["Bob", "Alice", "Bib", "Andrew", "Bin"]

    def build(self):
        """Build the Dynamic Labels App."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels for each name in list of names."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabels().run()
