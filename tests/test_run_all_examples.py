import os
import importlib.util
from pathlib import Path
import socket
import time
import tkinter as tk


def wait_for_port_to_be_free(port=9876, timeout=60):
    """Wait for the rerun port to become available"""
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex(("localhost", port))
                if result != 0:  # Port is free
                    return True
        except:
            return True
        time.sleep(1)
    return False


def test_run_all_examples():
    examples_dir = Path(__file__).parent.parent / "examples"

    # Loop over all files in subfolders
    for root, dirs, files in os.walk(examples_dir):
        for file in files:
            if file.endswith(".py"):

                # If you are running the files to check visually that you did not break anything, uncomment the
                # following line. It will wait for the rerun window to be closed before running the next example.
                # wait_for_port_to_be_free()

                file_path = Path(root) / file

                spec = importlib.util.spec_from_file_location("example_module", file_path)
                if spec and spec.loader:

                    # Import the example
                    module = importlib.util.module_from_spec(spec)

                    # Run the example
                    spec.loader.exec_module(module)

                    # Check if the module has a main function and call it
                    print(f"Running {file_path}")
                    if hasattr(module, "main"):
                        module.main()
                    else:
                        raise RuntimeError("All example files must have a main() function")
