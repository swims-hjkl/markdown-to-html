import re


def markdown_to_blocks(text):
    result = []
    for split in text.split("\n\n"):
        split_stripped = '\n'.join(i.strip()
                                   for i in split.strip().split("\n"))
        result.append(split_stripped)
    return result


def _block_is_ordered_list(block):
    for index, line in enumerate(block.split("\n")):
        if not line.startswith(f"{index+1}. "):
            return False
    return True


def _block_is_heading(block):
    if re.match(r"^#{1,6}\s", block):
        return True
    return False


def block_to_block_type(block: str):
    if _block_is_heading(block):
        return "heading"
    if block.startswith("```") and block.endswith("```"):
        return "code"
    if all([k[0] == ">" for k in block.split("\n")]) == len(block.split("\n")):
        return "quote"
    if all([(k.startswith("* ") or k.startswith("- ")) for k in block.split("\n")]):
        return "unordered_list"
    if _block_is_ordered_list(block):
        return "ordered_list"
    else:
        return "paragraph"
