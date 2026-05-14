#!/usr/bin/env python3
import os
import re
import subprocess
import tempfile

# Create directories
os.makedirs('modified', exist_ok=True)
os.makedirs('images', exist_ok=True)

def process_file(filepath):
    base = os.path.basename(filepath).replace('.md', '')
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Find all mermaid blocks
    mermaid_pattern = re.compile(r'```mermaid\n(.*?)\n```', re.DOTALL)
    count = 0
    def replace_mermaid(match):
        nonlocal count
        mermaid_code = match.group(1)
        count += 1
        svg_file = f'images/{base}_{count}.svg'
        
        # Write mermaid code to temp file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.mmd', delete=False) as temp:
            temp.write(mermaid_code)
            temp_path = temp.name
        
        # Run mmdc with Puppeteer config to disable sandbox
        cmd = ['mmdc', '-i', temp_path, '-o', svg_file, '-t', 'default', '-b', 'white', '-p', '.puppeteer.json']
        subprocess.run(cmd, check=True)
        
        # Clean up temp
        os.unlink(temp_path)
        
        # Return img tag
        return f'![Mermaid Diagram]({svg_file})'
    
    # Replace all mermaid blocks
    new_content = mermaid_pattern.sub(replace_mermaid, content)
    
    # Write modified file
    modified_path = f'modified/{base}.md'
    with open(modified_path, 'w') as f:
        f.write(new_content)
    
    print(f'Processed {filepath} -> {modified_path}')

# Process all files
for file in ['case-studies/*.md', 'resume/*.md']:
    import glob
    for filepath in glob.glob(file):
        process_file(filepath)