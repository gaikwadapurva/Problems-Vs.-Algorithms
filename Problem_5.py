## Represents a single node in the Trie
class TrieNode:

    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.is_word = False

    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode()
        else:
            pass

    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for all complete words below this point
        suffix_list = []
        for char, node in self.children.items():
            if node.is_word:
                suffix_list.append(suffix + char)    
            if node.children:
                suffix_list.extend(node.suffixes(suffix + char))
        return suffix_list


## The Trie itself containing the root node and insert/find functions
class Trie:

    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        node = self.root
        for char in word:
            node.insert(char)
            node = node.children[char]
        node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return node


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", "fuel",
    "trie", "trigger", "trigonometry", "tripod","trauma"
]
for word in wordList:
    MyTrie.insert(word)


def find(prefix):
    print()
    print(prefix + ".suffixes():")
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')


find('')
find('a')
find('fu')
find('tri')
find('abcd')