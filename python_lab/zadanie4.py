class AhoCorasick:
    def __init__(self):
        self.trie = {}
        self.output = {}
        self.fail = {}

    def add_pattern(self, pattern):

        node = self.trie
        for char in pattern:
            if char not in node:
                node[char] = {}
            node = node[char]
        node["$"] = pattern

    def build(self):

        from collections import deque

        queue = deque()


        for char, next_node in self.trie.items():
            self.fail[next_node] = self.trie
            queue.append(next_node)


        while queue:
            current_node = queue.popleft()
            for char, next_node in current_node.items():
                if char == "$":
                    continue


                fail_state = self.fail[current_node]
                while fail_state and char not in fail_state:
                    fail_state = self.fail.get(fail_state, self.trie)
                self.fail[next_node] = fail_state[char] if fail_state else self.trie


                if "$" in self.fail[next_node]:
                    if "$" not in next_node:
                        next_node["$"] = []
                    next_node["$"].extend(self.fail[next_node]["$"])

                queue.append(next_node)

    def search(self, text):

        node = self.trie
        results = []

        for i, char in enumerate(text):
            while node and char not in node:
                node = self.fail.get(node, self.trie)

            if not node:
                node = self.trie
                continue

            node = node[char]
            if "$" in node:
                results.extend((i - len(pattern) + 1, pattern) for pattern in node["$"])

        return results

# Example
if __name__ == "__main__":
    ac = AhoCorasick()

    # Add patterns to search
    patterns = ["he", "she", "his", "hers"]
    for pattern in patterns:
        ac.add_pattern(pattern)

    # Build the automaton
    ac.build()

    # Search text
    text = "ahishers"
    matches = ac.search(text)

    print("Matches found:")
    for start_idx, pattern in matches:
        print(f"Pattern '{pattern}' found at index {start_idx}")
