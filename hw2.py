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
            kidneyArea = sum(self.f((a + b) / 2) * (b - a) for a,b in [[((2 * np.pi) / n) * i, ((2 * np.pi) / n) * (i + 1)] for i in range(n)])
            n += 1
        return f'Area Computed By Rectangle Method: {kidneyArea - self.circleArea}'
                
    def part2(self):
        kidneyArea = 0
        return f'Area Computed By Trapezoidal Method: {kidneyArea - self.circleArea}'

class Q2:
    def __init__(self, n):
        self.A = np.array([[random.uniform(-1,1) for _ in range(n)] for _ in range(n)])
        self.b = np.array([1 for _ in range(n)])
        
    def solve(self):
        return np.linalg.matmul(np.linalg.inv(self.A), self.b)
        

if __name__ == "__main__":
    print(Q1().part1())
    print(Q2(66).solve())