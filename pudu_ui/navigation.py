from pudu_ui.controller import Controller


FORWARD = "forward"
BACKWARD = "backward"


class Navigator:
    def __init__(self):
        self.controllers = {}
        self.current_controller = None

    def add_controller(self, controller: Controller):
        if not controller.name:
            raise Exception("add_controller: Controller must have a name")

        self.controllers[controller.name] = controller

    def change(self, name: str, *args, **kwargs):
        if self.current_controller:
            self.current_controller.close()

        if not name in self.controllers:
            raise Exception(
                f"change: Couldn't find a controller with name: {name}"
            )
        self.current_controller = self.controllers[name]
        self.current_controller.load(*args, **kwargs)
