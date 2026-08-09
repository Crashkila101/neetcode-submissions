class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = s.lower()
        palindrome = re.sub(r'[^a-zA-Z0-9]', '', palindrome)
        if palindrome == palindrome[::-1]:
            return True
        return False

