from difflib import ndiff

def detect_changes(text1, text2):
    old_lines = text1.splitlines()
    new_lines = text2.splitlines()
    
    added = []
    deleted = []
    modified = []

    diff = list(ndiff(old_lines, new_lines))

    for line in diff:
        if line.startswith('+ '):
            added.append(line[2:])
        elif line.startswith('- '):
            deleted.append(line[2:])
        elif line.startswith('? '):  # Skip markers
            continue

    # Simple modified logic – if a line was deleted and a similar line added
    for d in deleted:
        for a in added:
            if d[:30] in a or a[:30] in d:
                modified.append((d, a))
                added.remove(a)
                deleted.remove(d)
                break

    return {
        'added': added,
        'deleted': deleted,
        'modified': modified
    }