# Sol 1
def shortestUncommonSubstrings(arr):
    n = len(arr)
    answer = [""] * n

    for i in range(n):
        current_string = arr[i]
        substrings = set()
        length = len(current_string)

        for l in range(length):
            for r in range(l+1, length+1):
                substrings.add(current_string[l:r])
        
        candidates = sorted(substrings, key=lambda x: (len(x),x))

        for c in candidates:
            is_unique = True
            for j in range(n):
                if i == j:
                    continue

                if c in arr[j]:
                    is_unique = False
                    break

            if is_unique:
                answer[i] = c
                break
            
    return answer

# O(N^2 X L^3)

# Sol 2

class TrieNode:
    def __init__(self):
        self.children = {}
        self.indices = set()

def build_generalized_suffix_trie(arr):
    root = TrieNode()
    for idx, s in enumerate(arr):
        L = len(s)
        for start in range(L):
            node = root
            for j in range(start, L):
                char = s[j]
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                node.indices.add(idx)
    return root

def dfs(node, path, candidates):
    """
    Recorre el trie en DFS. 
    'path' es el substring (camino desde la raíz hasta el nodo actual).
    'candidates' es un diccionario: clave = índice de cadena, valor = el candidato actual.
    """
    # Si este nodo aparece únicamente en una cadena:
    if len(node.indices) == 1:
        i = next(iter(node.indices))
        # Si no tenemos candidato para esta cadena o si el actual es mejor:
        if i not in candidates:
            candidates[i] = path
        else:
            # Elegimos el que tenga menor longitud, y en caso de empate, el lex menor.
            current = candidates[i]
            if len(path) < len(current) or (len(path) == len(current) and path < current):
                candidates[i] = path
    # Recorremos los hijos en orden lexicográfico para asegurar orden lex en caso de empate
    for ch in sorted(node.children.keys()):
        dfs(node.children[ch], path + ch, candidates)

def shortestUncommonSubstrings2(arr):
    n = len(arr)
    answer = [""] * n
    # Construir el Generalized Suffix Trie de todas las cadenas en arr.
    root = build_generalized_suffix_trie(arr)
    # Diccionario para almacenar, para cada cadena, el candidato encontrado.
    candidates = {}
    dfs(root, "", candidates)
    
    for i in range(n):
        # Si no se encontró ningún candidato único, se deja la cadena vacía.
        if i in candidates:
            answer[i] = candidates[i]
        else:
            answer[i] = ""
    return answer

arr1 = ["cab", "ad", "bad", "c"]
print(shortestUncommonSubstrings(arr1))
# Output esperado: ["ab", "", "ba", ""]

arr2 = ["abc", "bcd", "abcd"]
print(shortestUncommonSubstrings(arr2))
# Output esperado: ["", "", "abcd"]
