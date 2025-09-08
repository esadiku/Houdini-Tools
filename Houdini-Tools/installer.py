import os
import shutil
import hou

source_folder = os.path.join(os.path.dirname(__file__), "Houdini-Tools")
home = os.getenv("HOME") or os.getenv("USERPROFILE")
houdini_docs = os.path.join(home, "Documents", "houdini" + str(hou.applicationVersion()[0]))
dest_folder = os.path.join(houdini_docs, "Houdini-Tools")

os.makedirs(dest_folder, exist_ok=True)
shutil.copytree(source_folder, dest_folder, dirs_exist_ok=True)

print(f"Houdini Tools installed in Houdini Documents at:\n{dest_folder}")
print("\nNext step: In Houdini → Shelf → Import Shelf → select 'shelf/' folder inside Houdini-Tools")
