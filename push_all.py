import os
import subprocess

def run_command(cmd, cwd):
    result = subprocess.run(cmd, cwd=cwd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode().strip(), result.stderr.decode().strip(), result.returncode

base_dir = os.getcwd()

for folder in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder)

    if os.path.isdir(folder_path) and os.path.isdir(os.path.join(folder_path, '.git')):
        print(f"\n📁 Processing: {folder}")
        
        # Check for unstaged or staged changes
        stdout, stderr, _ = run_command("git status --porcelain", folder_path)
        if not stdout:
            print("✅ No changes to push.")
            continue

        # Add all changes
        run_command("git add .", folder_path)

        # Commit changes
        _, stderr, code = run_command('git commit -m "Automated update"', folder_path)
        if code != 0:
            print(f"⚠️ Commit failed: {stderr}")
            continue

        # Push changes
        _, stderr, code = run_command("git push", folder_path)
        if code == 0:
            print("🚀 Pushed successfully.")
        else:
            print(f"❌ Push failed: {stderr}")
