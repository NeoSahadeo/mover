import sys
import unittest
from unittest.mock import patch
import move


class TestMoves(unittest.TestCase):
    @patch('sys.argv', ['move.py'])
    def test_no_argv(self):
        with self.assertRaises(SystemExit) as context:
            self.movefiles = move.MoveFiles(sys.argv)
        self.assertEqual(move.help, str(context.exception))

    @patch('sys.argv', ['move.py', '--help -h --kill'])
    def test_argv_validation(self):
        with self.assertRaises(SystemExit) as context:
            self.movefiles = move.MoveFiles(sys.argv)
        self.assertEqual(move.help, str(context.exception))

    @patch('sys.argv', ['move.py', '--kill'])
    def test_command_does_not_exist(self):
        with self.assertRaises(SystemExit) as context:
            self.movefiles = move.MoveFiles(sys.argv)
        self.assertEqual(str(context.exception), str(context.exception))

    @patch('sys.argv', ['move.py', '-s --rename'])
    def test_stay_rename_error(self):
        with self.assertRaises(SystemExit) as context:
            self.movefiles = move.MoveFiles(sys.argv)
        self.assertEqual(str(context.exception), str(context.exception))

    @patch('sys.argv', ['move.py', 'file1'])
    def test_source_and_destination_no_enough_args(self):
        with self.assertRaises(SystemExit) as context:
            self.movefiles = move.MoveFiles(sys.argv)
        self.assertEqual(move.help, str(context.exception))

    @patch('sys.argv', ['move.py', '{"file1", "file_2"}', 'dest'])
    def test_source_and_destination_incorrect_format(self):
        with self.assertRaises(SystemExit) as context:
            self.movefiles = move.MoveFiles(sys.argv)
        self.assertEqual(move.incorrect_format, str(context.exception))

    @patch('sys.argv', ['move.py', 'file1', 'file_2', 'dest'])
    def test_source_and_destination_correct_format(self):
        self.movefiles = move.MoveFiles(sys.argv)

    @patch('sys.argv', ['move.py', 'file1', 'file_2', 'file_3', '-r'])
    def test_rename_error(self):
        with self.assertRaises(SystemExit) as context:
            self.movefiles = move.MoveFiles(sys.argv)
            self.movefiles.mv()
        self.assertEqual(str(context.exception), str(context.exception))


if __name__ == '__main__':
    unittest.main()
