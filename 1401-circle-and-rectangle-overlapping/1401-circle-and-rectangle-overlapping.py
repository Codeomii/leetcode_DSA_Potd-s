class Solution:

  def checkOverlap(
      self,
      radius: int,
      xCenter: int,
      yCenter: int,
      x1: int,
      y1: int,
      x2: int,
      y2: int,
  ) -> bool:
    return (
        max(x1, min(xCenter, x2)) - xCenter
    ) ** 2 + (max(y1, min(yCenter, y2)) - yCenter) ** 2 <= radius**2