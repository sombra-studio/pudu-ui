from pudu_ui import App, Button


def on_btn1_press(btn):
    btn.visible = False
    btn2.visible = True


def on_btn2_press(btn):
    btn.visible = False
    btn1.visible = True


if __name__ == '__main__':
    app = App()

    btn1 = Button(batch=app.batch)
    btn1.x = 200
    btn1.y = 100
    btn1.text = "Button 1"
    btn1.on_press = on_btn1_press
    btn1.invalidate()

    btn2 = Button(batch=app.batch)
    btn2.x = 500
    btn2.y = 100
    btn2.text = "Button 2"
    btn2.on_press = on_btn2_press
    btn2.visible = False
    btn2.invalidate()

    app.current_screen.widgets += [btn1, btn2]

    app.run()
