def simplify_path(path: str) -> str:
    """
    Simplify a Unix-style absolute path.

    Handles:
    - Multiple consecutive slashes
    - '.' for current directory
    - '..' for parent directory, including attempts beyond root
    - Trailing slashes
    - Empty path

    Args:
        path (str): The input path (absolute, starting with '/')
    
    Returns:
        str: The normalized canonical path.
    """
    if not path:
        return "/"

    stack = []
    parts = path.split("/")

    for part in parts:
        if part == "" or part == ".":  # skip empty parts or current dir
            continue
        elif part == "..":
            if stack:  # go up one directory
                stack.pop()
        else:
            stack.append(part)  # add valid directory

    return "/" + "/".join(stack)
