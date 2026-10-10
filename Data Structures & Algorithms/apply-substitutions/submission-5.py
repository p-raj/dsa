import re


class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:

        repl = dict(replacements)
        memo = {}

        def resolve(key):
            # Already fully expanded
            if key in memo:
                return memo[key]

            value = repl[key]

            # Replace every placeholder inside this value
            value = re.sub(r"%([^%]+)%", lambda m: resolve(m.group(1)), value)

            memo[key] = value
            return value

        # Resolve placeholders in the original text
        return re.sub(r"%([^%]+)%", lambda m: resolve(m.group(1)), text)
