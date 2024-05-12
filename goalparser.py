class Solution:
    def interpret(self, command: str) -> str:
        stack = []

        for i in range(len(command)):
            if command[i] == 'G':
                stack.append('G')
            elif command[i] == '(':
                if command[i+1] == ')':
                    stack.append('o')
                elif command[i+1] == 'a':
                    stack.append('al')
            
        return ''.join(stack)
        
