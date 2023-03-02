class NonBinTree:

    currentDir = 0

    def __init__(self, val):
        self.val = val
        self.nodes = []

    @classmethod
    def downDir(self):
        self.currentDir += 1

    @classmethod
    def upDir(self):
        self.currentDir -= 1

    def add_node(self, val):
        self.nodes.append(NonBinTree(val))

    def __repr__(self):
        # EDIT LATER TO DISPLAY TEXT BETTER
        return f"({self.val}): {self.nodes}"
    


a = NonBinTree(['/', 'dir'])
a.add_node(['a', 'dir'])
a.add_node(['b.text', 'file', '14848514'])
a.add_node(['c.dat', 'file', '8504156'])
a.add_node(['d', 'dir'])

a.downDir()


a.nodes[1].add_node(['e', 'dir'])
a.nodes[1].add_node(['f', 'file', '29116'])
a.nodes[1].add_node(['g', 'file', '2557'])
a.nodes[1].add_node(['h.lst', 'file', '62596'])

a.nodes[1].nodes[0].add_node(['i', 'file', '584'])

a.upDir()

print(a)