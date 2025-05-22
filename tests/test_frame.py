from pudu_ui import Frame
import unittest


class FrameTestCase(unittest.TestCase):
    def setUp(self):
        self.frame = Frame()

    def test_recompute(self):
        # Quad should change position
        new_x = 200
        new_y = 100
        self.frame.x = new_x
        self.frame.y = new_y
        self.frame.width += new_x // 2
        self.frame.height += new_y // 2
        self.frame.invalidate()
        self.frame.update(1.0)

        self.assertEqual(self.frame.quad.get_position(), (new_x, new_y))
        self.assertEqual(self.frame.quad.width, self.frame.width)
        self.assertEqual(self.frame.quad.height, self.frame.height)


if __name__ == '__main__':
    unittest.main()
