class Solution:
    # count num of words, num of total ' ' spaces
    # divide equally into num of words-1 (2 words, 1 space, 1 word, 0 space)
    # calculate remaining extra spaces as total spaces % (words-1)
    # add extra to end
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        num_words = len(words)
        total_spaces = text.count(' ')
        gap_bw_words = 0 if num_words == 1 else (total_spaces // (num_words -1))

        extra_spaces = total_spaces if gap_bw_words == 0 else (total_spaces % (num_words -1))
        # or
        # extra_spaces = total_spaces - gap_bw_words * (num_words -1)
        return (' '*gap_bw_words).join(words) + ' '*extra_spaces


# SIMILAR QUESTIONS
# UNIQUE EMAIL ADDRESSES
class Solution:
    # "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
    # If you add a plus '+' in the local name, everything after the first plus sign 
    # will be ignored. This allows certain emails to be filtered. Note that this rule
    # does not apply to domain names.
    # For example, "m.y+name@email.com" will be forwarded to "my@email.com".
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            name, domain = email.split('@') 
            local = name.split('+')[0].replace('.', '')
            seen.add(local + '@' + domain)
        return len(seen)