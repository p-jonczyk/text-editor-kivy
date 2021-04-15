from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import os


class LoadDialog(FloatLayout):
    # creats objects for loda dialog
    load = ObjectProperty()
    cancel = ObjectProperty()


class SaveDialog(FloatLayout):
    # creats objects for save dialog
    save = ObjectProperty()
    text_input = ObjectProperty()
    cancel = ObjectProperty()


class Root(FloatLayout):
    # creats objects for root
    loadfile = ObjectProperty()
    savefile = ObjectProperty()
    text_input = ObjectProperty()

    def dismiss_popup(self):
        # dismiss dialogs / popups
        self._popup.dismiss()

    def show_load(self):
        # shows load dialog after clicking "Load" button of root
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        # handeling/setting popup of load dialog
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_save(self):
        # shows load dialog after clicking "Save" button of root
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        # handeling/setting popup of load dialog
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        # loading .txt file into text_input.text - "text input field"
        with open(os.path.join(path, filename[0])) as stream:
            self.text_input.text = stream.read()

        self.dismiss_popup()

    def save(self, path, filename):
        # saving value of text_intput.txt - "text input field" to file
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.text_input.text)

        self.dismiss_popup()


class SimpleEditor(App):
    # class of kivy (.kv) file which contains settings of GUI
    pass


if __name__ == '__main__':
    SimpleEditor().run()
