from .message_handler import MessageHandler
import jupytext
from io import StringIO
from contextlib import redirect_stdout
import re

def run_notebook(notebook_path: str) -> list[str]:
    # Convert notebook to Python format
    # Note that some cells from the notebook can be skipped if they are tagged 'active-ipynb'. This is useful to skip steps with a GUI
    nb = jupytext.read(notebook_path)
    code = jupytext.writes(nb, fmt="py:percent")

    error_list = []

    # Execute code with the message handler capturing errors/warnings
    with MessageHandler() as msg_handler:
        globals_dict = {
            "__name__": "__main__",
            "__file__": notebook_path,
        }

        f = StringIO()

        with redirect_stdout(f):
            # WARNING: message handlers may be cleared by the execution of the code, preventing
            # the counting the errors.
            exec(code, globals_dict)

        s = f.getvalue()

        errors_in_output = re.findall(r"\[ERROR\].*\n", s)
        warnings_in_output = re.findall(r"\[WARNING\].*\n", s)

        error_list.extend(errors_in_output)
        error_list.extend(warnings_in_output)

        error_list.extend(msg_handler.error_list)
        error_list.extend(msg_handler.warning_list)



    return error_list
