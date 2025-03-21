import numpy as np
import random

class Q1:
    def __init__(self):
        self.f = lambda x: 0.5 * np.pow(np.pow(np.cos(x), 3) + np.pow(np.sin(x), 3), 2)
        self.circleArea = 0.125 * np.pi
        self.TOL = 0.5 * (10 ** -4)
     
    def part1(self):
        n = 1
        while 1 / np.pow(n,2) >= self.TOL:
            stepSize = (2 * np.pi) / n
            kidneyArea = sum(self.f((a + b) / 2) * (b - a) for a,b in [[stepSize * i, stepSize * (i + 1)] for i in range(n)])
            n += 1
        print(f'Area Computed By Rectangle Method: {kidneyArea - self.circleArea}')
                
    def part2(self):
        n = 1
        kidneyArea = 0
        while 1 / np.pow(n,3) >= self.TOL:
            stepSize = (2 * np.pi) / n
            intervals = [[stepSize * i, stepSize * (i + 1)] for i in range(n)]
            points = set()
            for a,b in intervals:
                points.add(a)
                points.add(b)
            points = sorted(list(points))
            kidneyArea = (stepSize / 2) * (sum(2 * self.f(points[i]) for i in range(1, len(points) - 1)) + self.f(points[0]) + self.f(points[-1]))
            n += 1
        print(f'Area Computed By Trapezoidal Method: {kidneyArea - self.circleArea}')

class Q2:
    def __init__(self, n):
        self.A = np.array([[random.uniform(-1,1) for _ in range(n)] for _ in range(n)])
        self.b = np.array([1 for _ in range(n)])
        self.n = n
        
    def solve(self):
        for i in range(self.n):
            val = self.A[i][i]
            for j in range(self.n):
                self.A[i][j] /= val
            self.b[i] /= val 
            for k in range(i + 1, self.n):
                for m in range(self.n):
                    self.A[k][m] -= (self.A[k][i] * self.A[i][m])
                self.b[k] -= (self.A[k][i] * self.b[i])
        for i in range(self.n - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                self.b[j] -=  (self.A[j][i] * self.b[i])
                self.A[j][i] -= (self.A[j][i] * self.A[i][i])
        print(self.b)
                        
if __name__ == "__main__":
    Q1 = Q1()
    Q1.part1()
    Q1.part2()
    Q2(66).solve()