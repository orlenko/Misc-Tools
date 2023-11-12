import re
from collections import defaultdict
import sys

UUID_REGEX = r'\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b'
LARGE_NUM_REGEX = r'\b[0-9.+\-eE]{5,}\b'

NOISE = (
    (UUID_REGEX, '[some uuid]'),
    (LARGE_NUM_REGEX, '[some number]')
  )

PREFIX_LENGTH = len('Sep 11 00:00:20 DFXM-EDGE-AWESOME07 stationSoftware[942]: ')


def load_text(filename: str) -> str:
    """Loads the text from the given file."""
    with open(filename, 'r') as file:
        return file.read()


def clean_noise(text: str) -> str:
    """Removes noise from the given text."""
    for regex, replacement in NOISE:
        text = re.sub(regex, replacement, text)
    return text

def strip_prefix(text: str) -> str:
    """Removes the prefix from the given text."""
    return '\n'.join(line[PREFIX_LENGTH:] for line in text.split('\n'))

def sort_lines(text: str, *args, **kwargs) -> str:
    """Sorts the lines in the given text."""
    return '\n'.join(sorted(text.split('\n'), *args, **kwargs))

def collapse_with_count(text: str, min_count=0) -> str:
    """Collapses the lines in the given text with a count."""
    counts = defaultdict(int)
    for line in text.split('\n'):
        counts[line] += 1

    max_width = len(str(max(counts.values(), key=abs)))
    return '\n'.join(f'{count:0{max_width}} {line}' for line, count in counts.items() if count >= min_count)


if __name__ == '__main__':
    filename = sys.argv[1]
    # Adjust this value based on the length of the prefix in your logs
    prefix_length = len('Sep 11 00:00:20 DFXM-EDGE-AWESOME07 stationSoftware[942]: ')
    result = sort_lines(collapse_with_count(sort_lines(clean_noise(strip_prefix(load_text(filename)))), 1000), reverse=True)
    print(result)
