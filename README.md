# Duplicate File Synchronizer

A Python script that synchronizes duplicate files with a target file by updating them to match the target's content.

## Overview

This tool helps you keep files with the same name synchronized across different locations. You specify a target file and a directory to search, and the script will find all files with the same name in that directory (and its subdirectories) and update them to match the target file's content.

## Features

- **Target-based synchronization**: Update all matching files to match your target file
- **Recursive search**: Searches through all subdirectories of the specified location
- **Safe operation**: Never modifies the original target file
- **Error handling**: Reports any files that couldn't be updated
- **Progress feedback**: Shows which files were updated and a summary at the end

## Requirements

- Python 3.6 or higher
- No external dependencies - uses only Python's standard library

## Installation

1. Download the script to your computer
2. Make it executable (optional):
   ```bash
   chmod +x sync_file_once.py
   ```

## Usage

Run the script and follow the interactive prompts:

```bash
python3 sync_file_once.py
```

Or if you made it executable:

```bash
./sync_file_once.py
```

### Interactive Prompts

1. **Enter target file path**: Provide the full path to the file you want to use as the source (e.g., `/home/user/documents/important.txt`)
2. **Enter directory to search**: Provide the directory where you want to search for duplicate files (e.g., `/home/user/backups` or `/` for the entire system)

## How It Works

1. The script reads the target file's content into memory
2. It recursively searches through the specified directory for files with the same name as the target
3. For each matching file found (excluding the target itself), it overwrites the file with the target's content
4. It reports success/failure for each file and provides a summary

## Example

Let's say you have:
- Target file: `/home/alice/latest_report.docx`
- You want to update all copies in: `/home/alice/backups/`

When you run the script:
```
Enter target file path: /home/alice/latest_report.docx
Enter directory to search: /home/alice/backups/
```

The script will:
1. Find all files named `latest_report.docx` in `/home/alice/backups/` and its subdirectories
2. Update each found file to match the content of `/home/alice/latest_report.docx`
3. Report which files were updated

## Important Notes

⚠️ **Warning**: This script overwrites files without creating backups. Use with caution!

- **No backup**: The script does not create backups of the files it modifies
- **No undo**: Once files are updated, the original content cannot be recovered
- **Target is safe**: The target file itself is never modified
- **File permissions**: The script maintains the existing file permissions when overwriting
- **Case-sensitive**: File name matching is case-sensitive

## Use Cases

- Synchronize configuration files across multiple locations
- Update duplicate backup files with the latest version
- Ensure all copies of a document are identical
- Propagate changes made to a template file to all its copies

## Limitations

- Only matches files by name (not by content)
- Does not handle symbolic links specially (will overwrite the link target)
- Cannot synchronize in reverse (make target match duplicates)
- No dry-run mode (always performs actual updates)

## Safety Recommendations

1. **Test first**: Run the script on a test directory with non-critical files
2. **Backup important data**: Ensure you have backups before running on production data
3. **Use specific directories**: Avoid searching entire system (`/`) unless absolutely necessary
4. **Check permissions**: Ensure you have write permissions for files you intend to update

## License

This script is provided as-is for personal use. Modify as needed for your requirements.
