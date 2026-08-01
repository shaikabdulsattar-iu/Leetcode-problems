class Solution:

  def calculate(self, s: str) -> int:
    stack = []
    curr_number = 0
    last_op = '+'
    operators = {'+', '-', '*', '/'}

    for i, ch in enumerate(s):
      if ch.isdigit():
        curr_number = curr_number * 10 + int(ch)
      if ch in operators or i == len(s) - 1:
        if ch == ' ':
          if i == len(s) - 1 and last_op not in operators:
            continue

        if last_op == '+':
          stack.append(curr_number)
        elif last_op == '-':
          stack.append(-curr_number)
        elif last_op == '*':
          stack.append(stack.pop() * curr_number)
        elif last_op == '/':
          stack.append(int(stack.pop() / curr_number))
        if ch in operators:
          last_op = ch
        curr_number = 0

    return sum(stack)