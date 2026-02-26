from .message_handler import MessageHandler
import jupytext

def run_notebook(notebook_path: str) -> tuple[int, int]:
    # Convert notebook to Python format
    # Note that some cells from the notebook can be skipped if they are tagged 'active-ipynb'. This is useful to skip steps with a GUI
    nb = jupytext.read(notebook_path)
    code = jupytext.writes(nb, fmt="py:percent")

    num_errors, num_warnings = 0, 0

    # Execute code with the message handler capturing errors/warnings
    with MessageHandler() as msg_handler:
        globals_dict = {
            "__name__": "__main__",
            "__file__": notebook_path,
        }

        # WARNING: message handlers may be cleared by the execution of the code, preventing
        # the counting the errors.
        exec(code, globals_dict)

        num_errors = msg_handler.num_errors
        num_warnings = msg_handler.num_warnings

    return num_errors, num_warnings
