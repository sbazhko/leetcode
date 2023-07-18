# https://leetcode.com/problems/unique-email-addresses/

import re
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = set()
        for email in emails:
            # assuming emails are valid
            emailParts = email.split("@")
            emailParts[0] = emailParts[0].replace(".", "")
            emailProcessed = re.findall(
                "(.[^+]*)(\+.*)?", emailParts[0])[0][0]
            emailProcessed += "@"
            emailProcessed += emailParts[1]
            if emailProcessed not in uniqueEmails:
                uniqueEmails.add(emailProcessed)
        return len(uniqueEmails)


s = Solution()

print(s.numUniqueEmails(["test.email+alex@leetcode.com",
      "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]))
print(s.numUniqueEmails(
    ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]))
