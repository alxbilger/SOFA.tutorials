"""
Notebook Validation System

This module scans a directory for Jupyter notebooks (.ipynb files), converts them to Python code,
and validates their execution by checking for errors and warnings.

Features:
- Recursively finds all .ipynb files in specified directories
- Excludes temporary checkpoints folders
- Converts notebooks to Python format using jupytext
- Executes converted code with error/warning tracking
- Provides comprehensive test coverage
- Skip code cells with tag 'active-ipynb'

Dependencies:
- jupytext: For converting between Jupyter notebook and Python code formats
- Sofa (Sofa.Helper.MessageHandler): For capturing execution messages
"""

import jupytext
import os
import unittest
from message_handler import MessageHandler


def _find_notebooks(directory: str) -> list[str]:
    """
    Recursively find all .ipynb files in the specified directory.

    Args:
        directory (str): Path to search for notebooks

    Returns:
        list[str]: A list containing absolute filesystem paths of all found Jupyter notebook (.ipynb)
    """
    notebook_files = []

    for root, dirs, files in os.walk(directory):
        abs_root = os.path.abspath(root)

        # exclude temp folder
        if '.ipynb_checkpoints' in dirs:
            dirs.remove('.ipynb_checkpoints')

        for file in files:
            if (file.endswith('.ipynb')):
                full_path = os.path.join(abs_root, file)
                notebook_files.append(full_path)

    return notebook_files


class NotebookTest(unittest.TestCase):
    """
    Test class that validates all Jupyter notebooks in the notebook directory.

    Executes each converted Python code and verifies there are no execution errors or warnings.
    """

    def test_all_notebooks(self):
        notebook_files = _find_notebooks('notebook')
        for notebook_file in notebook_files:
            print(f"Reading notebook {notebook_file}")

            # Convert notebook to Python format
            # Note that some cells from the notebook can be skiped if they are tagged 'active-ipynb'. This is useful to skip steps with a GUI
            nb = jupytext.read(notebook_file)
            code = jupytext.writes(nb, fmt="py:percent")

            with self.subTest(notebook_file=os.path.basename(notebook_file)):
                # Execute code with message handler capturing errors/warnings
                with MessageHandler() as msg_handler:

                    try:
                        exec(code, {})
                    except Exception as e:
                        self.fail(f"Execution failed in {notebook_file}: {str(e)}")

                    # Verify no execution errors or warnings occurred
                    self.assertEqual(msg_handler.num_errors, 0)
                    self.assertEqual(msg_handler.num_warnings, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)