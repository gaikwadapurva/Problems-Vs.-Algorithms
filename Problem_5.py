class TrieNode:
    def __init__(self):
        """Initialize this node in the Trie"""
        self.children = {}  # Dictionary of children
        self.is_word = False  # True if path taken up to this TrieNode is a word

    def insert(self, char):
        """Add a child node in this Trie"""
        self.children[char] = TrieNode()

    def suffixes(self, suffix=''):
        """Recursive function that collects the suffix for all complete words below this point"""

        suffixes = []

        # Iterate over children
        for char, node in self.children.items():

            # If node represents a word
            if node.is_word:
                # Append the suffix (up to this point) with the current char in question
                suffixes.append(suffix + char)

            # If node has more children
            if node.children:
                # Recursively add the children to the current suffixes
                suffixes.extend(node.suffixes(suffix + char))

        return suffixes


class Trie:
    """The Trie itself containing the root node and insert/find functions"""

    def __init__(self):
        """Initializes this Trie (add a root node)"""
        self.root = TrieNode()  # Root of tree

    def insert(self, word):
        """Adds a word to the Trie"""

        node = self.root  # Node used to traverse the Trie

        # Iterate over all character in word
        for char in word:

            # If character isn't a child of current node
            if char not in node.children:
                # Add character as a child
                node.insert(char)

            # Move traversal node forward
            node = node.children[char]

        # New word has been added to Trie
        node.is_word = True

    def find(self, prefix):
        """Finds the Trie node that represents this prefix"""

        node = self.root  # Node used to traverse the Trie

        # Iterate over all character in prefix
        for char in prefix:

            # If character isn't a child of current node
            if char not in node.children:
                # Prefix doesn't exist in Trie
                return False

            # Move traversal node forward
            node = node.children[char]

        # Return node that represents prefix
        return node


def test(prefix):
    # if prefix != '':
    prefix_node = MyTrie.find(prefix)
    print(prefix + ".suffixes():")
    if prefix_node:
        print(prefix_node.suffixes())
    else:
        print(prefix + " not found")
    print('')


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]

for word in wordList:
    MyTrie.insert(word)

print("Word List:", wordList, '\n')

test('')
# expected output: ['ant', 'anthology', 'antagonist', 'antonym', 'fun', 'function', 'factory',
# 'trie', 'trigger', 'trigonometry', 'tripod']

test('f')
# expected output: ['un', 'unction', 'actory']
test('an')
# expected output: ['t', 'thology', 'tagonist', 'tonym']

test('ant')
# expected output: ['hology', 'agonist', 'onym']

test('tripod')
# expected output: []