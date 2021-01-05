class Neuron:

    def __init__(self, w, f=lambda x: x):
        self.w = w
        self.f = f
        self.pred = None

    def forward(self, x):
        self.pred = x
        return self.f(sum(x1 * y1 for x1, y1 in zip(self.w, x)))

    def backlog(self):
        return self.pred
# YOUR CODE HERE
