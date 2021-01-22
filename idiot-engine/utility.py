class State:
    def __init__(self, end = False):
        self.is_end = end
        self.epsilon_transition = []
        self.normal_transition = {}
    
    def add_epsilon_transtion(self, f):
        self.epsilon_transition.append(f)
        self.is_end = False
    
    def add_normal_transition(self, by, f):
        self.normal_transition[by] = f
        self.is_end = False
    
class NFA:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def concat(self, other):
        self.end.add_epsilon_transtion(other.start)
        self.end.is_end = False
        return NFA(self.start, other.end)
    
    def union(self, other):
        start = State()
        start.add_epsilon_transtion(self.start)
        start.add_epsilon_transtion(other.start)
        end = State(True)
        self.end.add_epsilon_transition(end)
        other.end.add_epsilon_transition(end)
        other.end.is_end = False
        self.end.is_end = False

        return NFA(start, end)
    
    def star(self):
        start = State()
        start.add_epsilon_transtion(self.start)
        self.end.add_epsilon_transition(self.start)
        end = State(True)
        self.end.add_epsilon_transition(end)
        start.add_epsilon_transtion(end)
        self.end.is_end = False
        return NFA(start, end)
    
    def plus(self):
        start = State()
        start.add_epsilon_transtion(self.start)
        self.end.add_epsilon_transition(self.start)
        end = State(True)
        self.end.add_epsilon_transition(end)
        self.end.is_end = False
        return NFA(start, end)

    def question(self):
        start = State()
        start.add_epsilon_transtion(self.start)
        end = State(True)
        self.end.add_epsilon_transition(end)
        start.add_epsilon_transtion(end)
        self.end.is_end = False
        return NFA(start, end)



def get_epsilon():
    start = State()
    end = State(True)
    start.add_epsilon_transtion(end)
    return NFA(start, end)

def get_normal(by):
    start = State()
    end = State(True)
    start.add_normal_transition(by, end)
    return NFA(start, end)


def eat(postfix):
    if not postfix:
        return get_epsilon()

    stack = []
    for stuff in postfix:
        if stuff == '*':
            stack.append(stack.pop().star())
        elif stuff == '|':
            a, b = stack.pop(), stack.pop()
            stack.append(b.union(a))
        elif stuff == '.':
            a, b = stack.pop(), stack.pop()
            stack.append(b.concat(a))
        else:
            stack.append(get_normal(stuff))
    return stack.pop()
