import subprocess
import os

print(subprocess.run(["sh 1_session-setup-chromadb/setup-chroma.sh"], shell=True))