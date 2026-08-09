class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = s.lower()
        palindrome = re.sub(r'[^a-zA-Z0-9]', '', palindrome)
        # if palindrome == palindrome[::-1]:
        #     return True
        # return False

        l = 0
        r = len(palindrome) - 1

        while l < r:
            if palindrome[l] != palindrome[r]:
                return False
            l = l +1
            r = r -1
        return True


