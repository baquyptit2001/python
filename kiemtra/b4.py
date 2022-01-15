def isPalindrome(n):
    if len(n) == 1:
        return False
    for i in range(0, len(n) // 2):
        if n[i] != n[len(n) - 1 - i]:
            return False
    return True


inp = input()
print(isPalindrome(inp))
