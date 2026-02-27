import os

def find_notebooks(directory: str, exclude: list[str] = None) -> list[str]:
    """
    Recursively find all .ipynb files in the specified directory.

    Args:
        directory (str): Path to search for notebooks
        exclude (list[str]): List of notebook filenames to exclude

    Returns:
        list[str]: A list containing absolute filesystem paths of all found Jupyter notebook (.ipynb)
    """
    if exclude is None:
        exclude = []

    notebook_files = []

    for root, dirs, files in os.walk(directory):
        abs_root = os.path.abspath(root)

        # exclude temp folder
        if '.ipynb_checkpoints' in dirs:
            dirs.remove('.ipynb_checkpoints')

        for file in files:
            if file.endswith('.ipynb'):
                if file in exclude:
                    continue
                full_path = os.path.join(abs_root, file)
                notebook_files.append(full_path)

    return notebook_files