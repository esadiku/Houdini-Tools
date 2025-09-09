import os
import shutil
import platform

def get_houdini_versions():
    home = os.path.expanduser("~")
    system = platform.system()

    if system == "Windows":
        base = os.path.join(home, "Documents")
    elif system == "Darwin":
        base = os.path.join(home, "Library", "Preferences", "houdini")
    else:
        base = home

    versions = []
    if os.path.exists(base):
        for folder in os.listdir(base):
            if folder.startswith("houdini") and folder[7:].replace(".", "").isdigit():
                versions.append(os.path.join(base, folder))
    return versions

def install_shelf():
    repo_root = os.path.dirname(os.path.abspath(__file__))
    source_toolbar = os.path.join(repo_root, "toolbar")

    if not os.path.exists(source_toolbar):
        print("❌ 'toolbar' folder not found in the repository.")
        return

    versions = get_houdini_versions()
    if not versions:
        print("⚠️ No Houdini versions found on this computer.")
        return

    for houdini_dir in versions:
        dest_toolbar = os.path.join(houdini_dir, "toolbar")
        os.makedirs(dest_toolbar, exist_ok=True)

        for file in os.listdir(source_toolbar):
            if file.endswith(".shelf"):
                src = os.path.join(source_toolbar, file)
                dst = os.path.join(dest_toolbar, file)
                shutil.copy2(src, dst)
                print(f"✅ {file} → {dest_toolbar}")

    print("\n🎉 Installation completed for all Houdini versions!")
    print("Restart Houdini and your shelves will appear automatically.")

if __name__ == "__main__":
    install_shelf()
