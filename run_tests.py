import jupytext
import subprocess
import os
import Sofa

notebook_files = []

for root, dirs, files in os.walk('notebook'):
    abs_root = os.path.abspath(root)

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
        self.num_infos = 0

    def process(self, msg):
        if msg["type"]=="Error":
            self.num_errors += 1
        elif msg["type"]=="Warning":
            self.num_warnings += 1
        elif msg["type"]=="Info":
            self.num_infos += 1


i = 0
for notebook_file in notebook_files:
    print(f"Reading notebook {notebook_file}")
    nb = jupytext.read(notebook_file)
    code = jupytext.writes(nb, fmt="py:percent")

    code = "\n".join(["    " + line for line in code.splitlines()])
    code = "with MessageHandler() as msg_handler:\n" + code + "\n    print(f\"Number of warnings: {msg_handler.num_warnings}\")\n    print(f\"Number of infos: {msg_handler.num_infos}\")"
    # print(code)

    exec(code)