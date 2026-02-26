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
"""

import os
import unittest
from notebook_validation import find_notebooks, notebook_runner

class NotebookTest(unittest.TestCase):
    """
    Test class that validates all Jupyter notebooks in the notebook directory.

    Executes each converted Python code and verifies there are no execution errors or warnings.
    """

    def test_all_notebooks(self):
        notebook_files = find_notebooks.find_notebooks('notebooks')
        print(f"Found {len(notebook_files)} notebooks in 'notebooks' directory")
        self.assertTrue(len(notebook_files) > 0, "No notebooks found in 'notebooks' directory")
        for notebook_file in notebook_files:
            print(f"Reading notebook {notebook_file}")

            with self.subTest(notebook_file=os.path.basename(notebook_file)):
                try:
                    num_errors, num_warnings = notebook_runner.run_notebook(notebook_file)
                except Exception as e:
                    self.fail(f"Execution failed in {notebook_file}: {str(e)}")

                self.assertEqual(num_errors, 0, f"Found {num_errors} SOFA errors in {notebook_file}")
                self.assertEqual(num_warnings, 0, f"Found {num_warnings} SOFA warnings in {notebook_file}")


if __name__ == "__main__":
    unittest.main(verbosity=2)