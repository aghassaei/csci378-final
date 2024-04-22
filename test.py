import unittest

class TestGameEnv(unittest.TestCase):

    def test(self):
        env = GameEnv()
        self.assertEqual(env.state, None, "env was just initialized but state is " + str(env.state) + " when it should be None.")

if __name__ == '__main__':
    unittest.main()