from pudu_ui import App, Toggle


app = App()


if __name__ == '__main__':
    toggle = Toggle(batch=app.batch)
    toggle.x = app.width // 2 - toggle.width // 2
    toggle.y = app.height // 2 - toggle.height // 2
    # toggle.focus()
    toggle.invalidate()

    app.current_screen.widgets.append(toggle)

    app.run()
