import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass

class TreeNode(Node):
    def evaluate(self):
        if self.val.isdigit():
            return int(self.val)
        elif self.val == '*':
            return self.left.evaluate() * self.right.evaluate()
        elif self.val == '+':
            return self.left.evaluate() + self.right.evaluate()
        elif self.val == '-':
            return self.left.evaluate() - self.right.evaluate()
        else:    
            return self.left.evaluate() // self.right.evaluate()
            
    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        cur, stack = None, []
        for c in postfix:
            cur = TreeNode(c)
            if not c.isdigit():
                cur.right = stack.pop()
                cur.left = stack.pop()
            stack.append(cur)
        return cur           
		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""

## APPROACH 2

import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass
class Number(Node):
    def __init__(self, value):
        self.value = value
    def evaluate(self)->int:
        return self.value

class BinaryNode(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def evaluate(self) -> int:
        pass

class Plus(BinaryNode):
    def evaluate(self) -> int:
        return self.left.evaluate() + self.right.evaluate()

class Minus(BinaryNode):
    def evaluate(self) -> int:
        return self.left.evaluate() - self.right.evaluate()

class Div(BinaryNode):
    def evaluate(self) -> int:
        return self.left.evaluate() // self.right.evaluate()
class Mul(BinaryNode):
    def evaluate(self) -> int:
        return self.left.evaluate() * self.right.evaluate()
"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        operators = {'+':Plus, '-':Minus, '/': Div, '*': Mul}
        stack = []
        for token in postfix:
            if token in operators:
                right = stack.pop()
                left = stack.pop()
                stack.append(operators[token](left, right))
            else:
                stack.append(Number(int(token)))
        return stack[0]
        
		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""