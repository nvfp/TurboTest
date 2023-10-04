import unittest
from . import ErrorTT


class Test__ErrorTT(unittest.TestCase):

    def test_I(self):
        def f(): raise ErrorTT
        with self.assertRaises(ErrorTT) as ctx: f()

    def test_II(self):
        def f(): raise ErrorTT('foo')
        with self.assertRaises(ErrorTT) as ctx: f()
        self.assertEqual(str(ctx.exception), "foo")

    def test_III(self):
        def f(): raise ErrorTT('foo bar')
        try: f()
        except ErrorTT as e: self.assertEqual(str(e), "foo bar")

    def test_IV(self):
        def f(): raise ErrorTT('foo bar baz')
        try: f()
        except Exception as e: self.assertEqual(str(e), 'foo bar baz')

    def test_V(self):
        try:
            try:
                raise ErrorTT('hi 123')
            except ValueError:
                raise AssertionError("this exception should never rise")
        except ErrorTT as e:
            self.assertEqual(str(e), 'hi 123')


if __name__ == '__main__':
    unittest.main()
