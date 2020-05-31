### Analysis

The only unique part about this TrieNode, was the inclusion of the suffixes function.
At each recursive call, I appended each char as a child of the current suffix, to all suffixes.

Time Complexity:
Insert loops over all character in the given word - O(n).
Find loops over all characters in the given prefix - O(n).
Suffixes loops over all TrieNodes in children, and calls itself m times - O(mn).

Space Complexity:
Worst case would be when words with no common characters between them, therefore having a node for each letter - O(n).