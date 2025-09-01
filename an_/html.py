import os

# HTML content to be written to .md files
html_content = """<div style="float: left; width: 64%; padding: 1%;">


</div>
<div style="float: right; width: 26%; padding: 1%;">

</div>
<div style="clear: both;"></div>
"""

# Function to find and update all .md files
def update_md_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(html_content)
                    print(f"Updated: {file_path}")
                except Exception as e:
                    print(f"Error updating {file_path}: {e}")

# Run the function in the current directory
if __name__ == "__main__":
    current_directory = os.getcwd()
    update_md_files(current_directory)
    print("Finished updating .md files.")