class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def _dfs(self, node, prefix, results):
        if node.is_end:
            results.append(prefix)
        for char, child in node.children.items():
            self._dfs(child, prefix + char, results)

    def autocomplete(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        results = []
        self._dfs(node, prefix, results)
        return results

    def get_all_words(self):
        results = []
        self._dfs(self.root, "", results)
        return results

def levenshtein_distance(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s[i-1] == t[j-1] else 1
            dp[i][j] = min(dp[i-1][j] + 1,
                           dp[i][j-1] + 1,
                           dp[i-1][j-1] + cost)
    return dp[m][n]

def auto_correct(trie, word):
    words = trie.get_all_words()
    min_dist = float('inf')
    suggestions = []
    for w in words:
        dist = levenshtein_distance(word, w)
        if dist < min_dist:
            min_dist = dist
            suggestions = [w]
        elif dist == min_dist:
            suggestions.append(w)
    return suggestions

# Exemplo de uso:
if __name__ == "__main__":
    # Inserindo títulos de livros (em minúsculas para simplificar)
    titles = ["harry potter", "hamlet", "hunger games", "foundation", "dune", "1984", "pride and prejudice", "the hobbit"]
    trie = Trie()
    for title in titles:
        trie.insert(title)

    # Autocompletar: sugestões para o prefixo "ha"
    print("Autocomplete para 'ha':", trie.autocomplete("ha"))
    
    # Correção automática: sugere o título mais similar a "hary potter"
    print("Auto-correct para 'hary potter':", auto_correct(trie, "hary potter"))
