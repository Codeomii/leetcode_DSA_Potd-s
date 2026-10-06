class Solution:

  def minAddToMakeValid(self, s: str) -> int:
    open_needed = close_needed = 0
    for c in s:
      if c == "(":
        open_needed += 1
      elif open_needed:
        open_needed -= 1
      else:
        close_needed += 1
    return open_needed + close_needed