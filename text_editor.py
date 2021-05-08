from kivy.properties import ObjectProperty, ColorProperty, StringProperty
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.config import Config
from kivy.lang import Builder
from kivy.base import EventLoop
from kivy.uix.bubble import Bubble
from kivy.uix.scatter import Scatter
from kivy.graphics.transformation import Matrix
from kivy.uix.dropdown import DropDown
import os
import tempfile

# disables multitouch functionality of kivy (usfule for mobiles)
Config.set('input', 'mouse', 'mouse,disable_multitouch')


class LoadDialog(FloatLayout):
    # creats objects for loda dialog
    load = ObjectProperty()
    cancel = ObjectProperty()


class SaveDialog(FloatLayout):
    # creats objects for save dialog
    save = ObjectProperty()
    text_input = ObjectProperty()
    cancel = ObjectProperty()


class Root(FloatLayout, Scatter):
    # creats objects for root
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

    def on_touch_up(self, touch):
        # handeling different mouse actions

        # menu showne when mouse right-click
        if touch.button == 'right':
            # built-in function for text input field
            self.text_input._show_cut_copy_paste(
                (touch.x, touch.y), EventLoop.window, mode='paste')

        if super(Root, self).on_touch_up(touch) and touch.is_mouse_scrolling:
            # zooming in/out acording to coursor possition
            if touch.button == 'scrollup':
                mat = Matrix().scale(0.9, 0.9, 0.9)
                self.apply_transform(mat, anchor=touch.pos)
            elif touch.button == 'scrolldown':
                mat = Matrix().scale(1.1, 1.1, 1.1)
                self.apply_transform(mat, anchor=touch.pos)

    def redo(self):
        # redo functionality
        self.text_input.do_redo()

    def undo(self):
        # undo functionality
        self.text_input.do_undo()

    def print_file(self):
        # print functionality
        printit = tempfile.mktemp(".txt")
        open(printit, 'w').write(self.text_input.text)
        os.startfile(printit, "print")

    def clear_text_input(self):
        # clear all text functionality
        self.text_input.text = ""

    def cut_btn(self):
        # cut text functionality
        self.text_input.cut()

    def copy_btn(self):
        # copy text functionality
        self.text_input.copy()

    def paste_btn(self):
        # paste text functionality
        self.text_input.paste()

    def select_all_btn(self):
        # select all text functionality
        self.text_input.select_all()


class SimpleEditor(App):
    # class of kivy (.kv) file which contains settings of GUI
    pass


if __name__ == '__main__':
    SimpleEditor().run()
