from pudu_ui import Params, Widget

import unittest


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        params: Params = Params(x=400, y=200, width=100.0, height=100.0)
        self.widget: Widget = Widget(params)

    def test_is_inside(self):
        x: float = 473
        y: float = 234
        self.assertTrue(
            self.widget.is_inside(x=x, y=y),
            msg=f"for widget {self.widget}, x: {x}, y: {y} is not inside"
        )


if __name__ == '__main__':
    unittest.main()
