from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class ConvertMilesKM(App):
    """Run app to convert miles to km."""
    output_km = StringProperty()

    def build(self):
        """Build the app with the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def convert_miles_km(self, text):
        """Convert miles to km."""
        result = self.convert_to_number(text) * MILES_TO_KM
        self.output_km = str(result)

    def handle_increment(self, input_text, change):
        """Handle up and down buttons and update input with new value."""
        result = self.convert_to_number(input_text) + change
        self.root.ids.input_number.text = str(result)
        self.convert_miles_km(result)

    def convert_to_number(self, text):
        """Convert input text to a float number."""
        try:
            return float(text)
        except ValueError:
            return 0.0


ConvertMilesKM().run()
