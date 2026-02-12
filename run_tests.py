import jupytext
import os
import Sofa
import unittest

notebook_files = []

for root, dirs, files in os.walk('notebook'):
    abs_root = os.path.abspath(root)

    # exclude temp folder
    if '.ipynb_checkpoints' in dirs:
        dirs.remove('.ipynb_checkpoints')

    for file in files:
        if (file.endswith('.ipynb')):
            full_path = os.path.join(abs_root, file)
            notebook_files.append(full_path)


class MessageHandler(Sofa.Helper.MessageHandler):
    def __init__(self):
        super().__init__()
        self.num_errors = 0
        self.num_warnings = 0

    def process(self, msg):
        if msg["type"]=="Error":
            self.num_errors += 1
        elif msg["type"]=="Warning":
            self.num_warnings += 1


class NotebookTest(unittest.TestCase):
    def test_all_notebooks(self):
        for notebook_file in notebook_files:
            print(f"Reading notebook {notebook_file}")
            nb = jupytext.read(notebook_file)
            code = jupytext.writes(nb, fmt="py:percent")

            with self.subTest(notebook_file=os.path.basename(notebook_file)):

                with MessageHandler() as msg_handler:

                    exec(code, {})
                    self.assertEqual(msg_handler.num_errors, 0)
                    self.assertEqual(msg_handler.num_warnings, 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)