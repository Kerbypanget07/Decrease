# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 20:34:49 2023

@author: Kervy
"""
def cross_river(n):
    steps = []
    steps.append(("Boy1, Boy2", "S"))
    steps.append(("Boy2", "<-- Boy1, S -->"))
    steps.append(("<-- Boy2, S -->", "Boy1"))
    steps.append(("Boy1", "<-- Boy2, S -->"))

    return steps * n

def print_solution(steps):
    for i, step in enumerate(steps, start=1):
        print(f"Step {i}: {step[0]} --> {step[1]}")

n = int(input("Enter the number of soldiers: "))
solution = cross_river(n)
print_solution(solution)

