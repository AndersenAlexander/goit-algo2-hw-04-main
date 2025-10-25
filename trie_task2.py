from trie import Trie
from colorama import Fore, init
init(autoreset=True)

class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        # Validate input
        if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
            print(Fore.RED + "Invalid input: expected a list of strings.")
            return ""
        if not strings:
            print(Fore.YELLOW + "Empty list: no common prefix.")
            return ""

        # Insert words and mark terminal nodes (value != None)
        for w in strings:
            self.put(w, True)  # IMPORTANT: mark terminals

        # Walk down while: exactly one child AND current node is not terminal
        node = self.root
        prefix_chars = []
        while node and len(node.children) == 1 and node.value is None:
            (ch, next_node), = node.children.items()
            prefix_chars.append(ch)
            node = next_node

        prefix = "".join(prefix_chars)
        if prefix:
            print(Fore.GREEN + f"Longest common prefix: {prefix}")
        else:
            print(Fore.YELLOW + "There is no common prefix.")
        return prefix

if __name__ == "__main__":
    trie = LongestCommonWord()
    assert trie.find_longest_common_word(["flower", "flow", "flight"]) == "fl"
    trie = LongestCommonWord()
    assert trie.find_longest_common_word(["interspecies", "interstellar", "interstate"]) == "inters"
    trie = LongestCommonWord()
    assert trie.find_longest_common_word(["dog", "racecar", "car"]) == ""
    # Extra edge case:
    trie = LongestCommonWord()
    assert trie.find_longest_common_word(["ab", "abc"]) == "ab"
