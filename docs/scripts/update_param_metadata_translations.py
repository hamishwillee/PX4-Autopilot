#!/usr/bin/env python3
import subprocess
from pathlib import Path
from bs4 import BeautifulSoup

REPO_URL = "https://github.com/PX4/PX4-Metadata-Translations.git"
REPO_NAME = "PX4-Metadata-Translations"

# Set the language code you want to process
LANGUAGE = "uk"  # change to 'zh', 'ko', etc.

def main():
    # Get directory where the script is located
    script_dir = Path(__file__).resolve().parent

    # Create translation_metadata directory if needed
    target_dir = script_dir / "translation_metadata"
    target_dir.mkdir(exist_ok=True)

    repo_path = target_dir / REPO_NAME

    if not repo_path.exists():
        print(f"Cloning repository into {repo_path}...")
        subprocess.run(["git", "clone", REPO_URL, str(repo_path)], check=True)
    else:
        print(f"Repository already exists in {repo_path}, updating to latest...")
        subprocess.run(["git", "-C", str(repo_path), "fetch", "--all"], check=True)
        subprocess.run(["git", "-C", str(repo_path), "reset", "--hard", "origin/HEAD"], check=True)

    print("Repository is up to date.")

    # Path to the 'translated' folder
    translated_dir = repo_path / "translated"

    # Match files like: parameters_*_uk_*.ts
    pattern = f"parameters_{LANGUAGE}_*.ts"
    print(f"getting: {pattern}")

    for ts_file in translated_dir.glob(pattern):
        if ts_file.is_file():
            print(f"Processing {ts_file.name}...")
            with ts_file.open("r", encoding="utf-8") as f:
                content = f.read()

            # Parse with BeautifulSoup as XML (Qt TS files are XML)
            soup = BeautifulSoup(content, "xml")

            #Selects all the <context> nodes that don't have an element that has the attribute type="unfinished"
            #PX4-Autopilot\src\lib\parameters\px4params
            selector = 'context:not(:has([type="unfinished"]))'
            matching_contexts = soup.select(selector)

            # Print the results
            for context in matching_contexts:
                print(context)


if __name__ == "__main__":
    main()
