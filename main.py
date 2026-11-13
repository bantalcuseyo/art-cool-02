import os
import shutil
from pathlib import Path

SRC = Path(__file__).resolve().parent / "entry.png"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SRC, OUT_DIR / "entry.png")
print("wrote", OUT_DIR / "entry.png")
