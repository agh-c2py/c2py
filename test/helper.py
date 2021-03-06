from ..__main__ import translate
import subprocess
import sys


def run_example(example_name: str) -> str:
    code = translate(f"examples/{example_name}.c")
    output = subprocess.run([sys.executable, "-c", code],
                            capture_output=True, text=True)
    return output.stdout


def generate_list(to: int, separator: str, ending=None) -> str:
    if ending is None:
        ending = separator
    return separator.join([str(i) for i in range(to)]) + ending
