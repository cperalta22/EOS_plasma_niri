#!/usr/bin/env python3
import sys
import os
import re
import subprocess

def parse_markdown(filepath):
    """
    Parses the '## Software complementario' section in the markdown file.
    Extracts categories and yay packages, checking whether they are commented out.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the section "## Software complementario"
    section_match = re.search(r'## Software complementario(.*?)(##\s+|$)', content, re.DOTALL)
    if not section_match:
        print("Error: Section '## Software complementario' not found in markdown file.")
        sys.exit(1)

    section_text = section_match.group(1)

    # Extract contents of the bash block
    bash_match = re.search(r'```bash\s*(.*?)\s*```', section_text, re.DOTALL)
    if not bash_match:
        print("Error: Bash block not found inside '## Software complementario'.")
        sys.exit(1)

    bash_lines = bash_match.group(1).splitlines()

    categories = []
    current_category = "General"
    current_mode = None  # can be 'yay', 'flatpak', or None
    is_current_mode_commented = False

    for line in bash_lines:
        line_strip = line.strip()
        if not line_strip:
            continue

        # Check for category comment
        if line_strip.startswith('#'):
            comment_content = line_strip[1:].strip()
            # If it's a command like #yay or #flatpak, it's not a category header
            if re.match(r'^(yay|flatpak)', comment_content):
                cmd_name = re.match(r'^(yay|flatpak)', comment_content).group(1)
                current_mode = cmd_name
                is_current_mode_commented = True
                continue
            elif comment_content.endswith('\\'):
                if 'yay' in comment_content or 'flatpak' in comment_content:
                    current_mode = 'yay' if 'yay' in comment_content else 'flatpak'
                    is_current_mode_commented = True
                    continue
            
            # Check if this comment is a package comment or a category comment
            indent = len(line) - len(line.lstrip())
            after_hash = line_strip[1:]
            is_package_comment = False
            if indent > 0 or after_hash.startswith('  ') or (not after_hash) or (after_hash.strip().islower() and ' ' not in after_hash.strip()):
                is_package_comment = True

            if not is_package_comment:
                current_category = comment_content
                continue

        # Check for command starts
        if 'yay -S' in line_strip or 'yay- S' in line_strip:
            current_mode = 'yay'
            is_current_mode_commented = line_strip.startswith('#')
            continue
        elif 'flatpak install' in line_strip:
            current_mode = 'flatpak'
            is_current_mode_commented = line_strip.startswith('#')
            continue

        # If we are in yay mode, process package
        if current_mode == 'yay':
            pkg_line = line_strip
            is_pkg_commented = is_current_mode_commented or pkg_line.startswith('#')
            clean_pkg = pkg_line.replace('#', '').replace('\\', '').strip()
            if not clean_pkg or ' ' in clean_pkg:
                continue
                
            cat_dict = next((c for c in categories if c['name'] == current_category), None)
            if not cat_dict:
                cat_dict = {'name': current_category, 'packages': []}
                categories.append(cat_dict)
            
            cat_dict['packages'].append({
                'name': clean_pkg,
                'selected': not is_pkg_commented
            })
            
        elif current_mode == 'flatpak':
            # Skip flatpak packages
            continue

    return categories

def main():
    # Path to markdown file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    md_path = os.path.join(script_dir, 'install_eos_niri.md')
    if not os.path.exists(md_path):
        print(f"Error: Could not find '{md_path}'")
        sys.exit(1)

    categories = parse_markdown(md_path)
    if not categories:
        print("No packages parsed.")
        sys.exit(1)

    # Check if gum is installed
    try:
        subprocess.run(['which', 'gum'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    except subprocess.CalledProcessError:
        print("Error: 'gum' is not installed. Please install it first using: yay -S gum")
        sys.exit(1)

    # Prepare items for gum choose
    all_choices = []
    pre_selected = []

    for cat in categories:
        for pkg in cat['packages']:
            display_name = f"[{cat['name']}] {pkg['name']}"
            all_choices.append(display_name)
            if pkg['selected']:
                pre_selected.append(display_name)

    # Run gum choose
    gum_args = [
        'gum', 'choose',
        '--no-limit',
        '--header=Select software to install (Space to select/deselect, Enter to confirm, Esc/Ctrl+C to cancel)',
        '--selected=' + ','.join(pre_selected)
    ]
    gum_args.extend(all_choices)

    try:
        proc = subprocess.run(gum_args, stdout=subprocess.PIPE, text=True)
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
        sys.exit(0)

    if proc.returncode != 0:
        print("Operation cancelled or failed.")
        sys.exit(proc.returncode)

    selected_lines = proc.stdout.splitlines()
    if not selected_lines:
        print("No packages selected. Exiting.")
        sys.exit(0)

    # Extract package names from selected items
    selected_packages = []
    for line in selected_lines:
        match = re.match(r'^\[.+?\]\s*(.+)$', line)
        if match:
            selected_packages.append(match.group(1).strip())
        else:
            selected_packages.append(line.strip())

    print("\nSelected packages to install:")
    for pkg in selected_packages:
        print(f" - {pkg}")
    print()

    # Confirm installation using gum confirm
    confirm_args = ['gum', 'confirm', f"Do you want to run: yay -S {' '.join(selected_packages)}?"]
    confirm_proc = subprocess.run(confirm_args)
    if confirm_proc.returncode != 0:
        print("Installation cancelled.")
        sys.exit(0)

    # Execute yay -S
    print(f"\nExecuting: yay -S {' '.join(selected_packages)}")
    try:
        # Using os.execvp to replace current process with yay -S
        # This gives yay direct control of the terminal input/output
        os.execvp('yay', ['yay', '-S'] + selected_packages)
    except FileNotFoundError:
        print("Error: 'yay' is not installed or not in PATH.")
        sys.exit(1)

if __name__ == '__main__':
    main()
