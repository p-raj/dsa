class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        S = set()
        for email in emails:
            parts = email.split('@')
            prefix = parts[0]
            suffix = parts[1]
            prefix = prefix.split('+')[0]
            prefix = prefix.replace('.','')
            email = prefix + suffix
            S.add(email)
        return len(S)