#!/usr/bin/python3

from os import scandir, unlink
import argparse

def scantree(path):
    """Recursively yield DirEntry objects for files in a given directory."""
    for entry in scandir(path):
        if entry.is_dir(follow_symlinks=False):
            yield from scantree(entry.path)
        elif entry.is_file(follow_symlinks=False):
            yield entry
        else:
            continue # ignore if non-file

def delete(files, delete=False):
    """Delete all files in array of DirEntry objects if delete=True, else just print paths"""
    print("files to delete: ", len(files))
    for f in files:
        print(f.path)
        if delete:
            unlink(f.path)

def main():
    parser = argparse.ArgumentParser(description='Recursively delete files until dir size is less than threshold size. Files with oldest modification time are deleted first.')
    parser.add_argument('directory', metavar='dir', action="store", help="root directory")
    parser.add_argument('threshold', metavar='bytes', action="store", type=int, help="threshold size in bytes")
    parser.add_argument('--delete', action="store_true", default=False, help="perform delete (default: print files to be deleted)")
    
    args = parser.parse_args()

    tree_files = scantree(args.directory)
    threshold = args.threshold

    # sort files by mtime. oldest first.
    tree_files = sorted(tree_files, key=lambda f: f.stat().st_mtime)

    tree_size = sum(f.stat().st_size for f in tree_files)

    delete_files = []

    print("tree size: %d bytes" % tree_size)
    print("threshold: %d bytes" % threshold)
    
    for f in tree_files:
        if tree_size < threshold:
            break
        else:
            delete_files.append(f)
            tree_size -= f.stat().st_size

    delete(delete_files, args.delete)

if __name__ == "__main__":
    main()
