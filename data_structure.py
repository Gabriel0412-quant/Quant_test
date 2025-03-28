# Creating algorithm TWO PONTER

class solution:
    def reverseWords_manual(s):
        res = ''
        l, r = 0, 0

        while r < len(s):
            if s[r] != '':
                r += 1
            else:
                res += s[l: r+1] [::-1]
                r+= 1
                l = r
        
        res += ''
        res += s[l:r + 2] [:: -1]
        return res[1:]
    

# Creating algorithm BINARY SEARCH

def binary_search(nums, n):
    lo = 0
    hi = len(nums) - 1  
    steps = 0

    while lo <= hi:  
        steps += 1  
        mid = (lo + hi) // 2  

        if nums[mid] == n:  
            print("Step", steps)
            return mid
        elif nums[mid] < n:
            lo = mid + 1
        else:
            hi = mid - 1  
    return -1

a = [1, 2, 3, 4, 5, 6, 7]

b = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]


print(binary_search(a, 3))  

print(binary_search(b, 17))


# slinding window

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        # Se a string estiver vazia, retorna 0
        if not s:
            return 0

        l, r = 0, 0
        max_len = 0
        counter = {}

        # Percorre a string com um ponteiro 'r'
        while r < len(s):
            # Adiciona o caractere atual no contador
            counter[s[r]] = counter.get(s[r], 0) + 1
            
            # Se algum caractere aparece mais de duas vezes, ajusta 'l'
            while any(count > 2 for count in counter.values()):
                counter[s[l]] -= 1
                l += 1
            
            # Atualiza o tamanho máximo da janela válida
            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len

# Exemplo de uso:
sol = Solution()
s = "bcbbbcba"
print(sol.maximumLengthSubstring(s))






