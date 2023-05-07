from lexer import TokenKind
from parser import BinaryOperationNode, Node, NumberNode


class Interpreter:
    def visit_number(self, node: NumberNode) -> int:
        assert node.value.text is not None
        return int(node.value.text)

    def visit_binary_operation(self, node: BinaryOperationNode) -> int:
        if isinstance(node.left, BinaryOperationNode):
            left = self.visit_binary_operation(node.left)
        else:
            left = self.visit_number(node.right)
        right = self.visit_number(node.right)
        if node.operator.kind == TokenKind.PLUS:
            return left + right
        else:
            return left - right


def exec(tree: BinaryOperationNode) -> None:
    print(Interpreter().visit_binary_operation(tree))
