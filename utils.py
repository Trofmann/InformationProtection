from typing import List


def split_to_blocks(iterable: str, block_len: int) -> List[str]:
    return [iterable[i:i + block_len] for i in range(0, len(iterable), block_len)]
