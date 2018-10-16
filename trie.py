from typing import Tuple


class TrieNode(object):
    """
    Our trie node implementation. Very basic. but does the job
    """

    def __init__(self, word: str):
        self.word = word
        self.children = {}
        # Is it the last character of the word.`
        self.sentence_finished = False
        # How many times this character appeared in the addition process
        self.counter = 1


def add(root, wordlist):
    """
    Adding a word in the trie structure
    """
    node = root
    for word in wordlist:
        # We did not find it so add a new chlid
        if not node.children.get(word):
            new_node = TrieNode(word)
            node.children[word] = new_node
            # And then point node to the new child
            node = new_node
    # Everything finished. Mark it as the end of a word.
    node.word_finished = True


def find_prefix(root, words) -> Tuple[bool, int]:
    """
    Check and return
      1. If the prefix exsists in any of the words we added so far
      2. If yes then how may words actually have the prefix
    """
    node = root
    # If the root node has no children, then return False.
    # Because it means we are trying to search in an empty trie
    if not root.children:
        return False, 0
    for word in words:
        if node.children.get(word):
            node = node.children[word]
        else:
            return False, 0

    # Well, we are here means we have found the prefix. Return true to indicate that
    # And also the counter of the last node. This indicates how many words have this
    # prefix
    return True, node.counter


if __name__ == "__main__":
    root = TrieNode('*')
    add(root, ["hello", "world"])
    add(root, ['hello'])

    print(find_prefix(root, ['hello']))
    print(find_prefix(root, ['hello', 'world']))
    print(find_prefix(root, ['hackathon']))
    print(find_prefix(root, ['ha']))
    print(find_prefix(root, ['hammer']))
