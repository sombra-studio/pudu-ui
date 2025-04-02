from pudu_ui import Params, Widget

import unittest


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        params: Params = Params(x=400.0, y=200.0, width=100, height=100)
        self.widget: Widget = Widget(params)

    def test_is_inside(self):
        x = 473.0
        y = 234.0
        self.assertTrue(
            self.widget.is_inside(x=x, y=y),
            msg=f"for widget {self.widget}, x: {x}, y: {y} is not inside"
        )


if __name__ == '__main__':
    unittest.main()
