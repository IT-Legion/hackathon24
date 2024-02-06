from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Rectangle,Color


class CanvasApp(App):
    def build(self):
        layout = RelativeLayout()

    

        # Создаем кнопку на холсте
        button = Button(text='<', on_press=self.on_button_press,
                        size_hint=(0.15, 0.15),
                        size=(32, 32),
                        pos_hint={'left': 1, 'top': 1})

        layout.add_widget(button)

        button2 = Button(text='>', on_press=self.on_button_press,
                        size_hint=(0.15, 0.15),
                        size=(32, 32),
                        pos_hint={'right': 1, 'top': 1})
        layout.add_widget(button2)

        return layout

    def on_button_press(self, instance):
        print('Кнопка была нажата!')


if __name__ == '__main__':
    CanvasApp().run()

