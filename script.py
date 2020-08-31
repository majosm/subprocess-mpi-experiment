import os
import sys
import subprocess

script = "\'" + """from mpi4py import MPI
from pathlib import Path
rank = MPI.COMM_WORLD.Get_rank()
print(f"rank {rank}")
Path(f"out{rank}.txt").touch()""".replace("\n", "; ") + "\'"

print_script = ['echo', script]
run_script = [sys.executable, '-m', 'mpi4py', '-c', script]

command = ['lrun', '-n', '4'] + run_script

# Version 1
# exit_code = os.system(" ".join(command))

# Version 2
# exit_code = subprocess.call(command)

# Version 3
# exit_code = subprocess.call(command, shell=True)

assert not exit_code
