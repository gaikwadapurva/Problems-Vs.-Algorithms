### Analysis

This algorithm will be used to implement an HTTPRouter like you would find in a typical web server using the Trie data structure we learned previously.

Time complexity: The runtime complexity of this algorithm would be O(n) because searching and inserting from a trie depends on the length of the path being searched for, and being inserted. 

Space complexity: The worst case here would be that no paths have common folders between them and all of those are independent of each other resulting in a space complexity of O(n).