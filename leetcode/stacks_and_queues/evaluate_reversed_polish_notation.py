from typing import List

class Solution:
    """
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            "/": lambda a, b: int(a / b), 
            "+": lambda a, b: a + b, 
            "-": lambda a, b: a - b, 
            "*": lambda a, b: a * b
            }
        for char in tokens:
            if char in operators:
                n1, n2 = stack.pop(), stack.pop()
                stack.append(operators[char](n2, n1))
            else:
                stack.append(int(char))
        return stack.pop()
    """

    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for c in tokens:
            if c == "+":
                st.append(st.pop() + st.pop())
            elif c == "-":
                second, first = st.pop(), st.pop()
                st.append(first - second)
            elif c == "*":
                st.append(st.pop() * st.pop())
            elif c == "/":
                second, first = st.pop(), st.pop()
                st.append(int(first / second))                
            else:
                st.append(int(c))
        
        return st[0]            


if __name__ == "__main__":
    print(Solution().evalRPN(["2","1","+","3","*"])) # 9
    print(Solution().evalRPN(["4","13","5","/","+"])) # 6
    print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])) # 22

        