"""Portable entry point. Default redraws saved amplitude results; --recompute rebuilds them."""
from pathlib import Path
import argparse, os, subprocess, sys
ROOT=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--recompute',action='store_true');a=p.parse_args()
env=os.environ.copy()
for name in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:env[name]='1'
steps=(['recompute_amplitude.py'] if a.recompute else [])+[f'plot_ed{i}.py' for i in range(7,11)]
for script in steps:subprocess.run([sys.executable,str(ROOT/script)],check=True,env=env)
