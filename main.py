from sympy import symbols, latex
from sympy.solvers import nonlinsolve


def main():
    x, x1, x2, x3 = symbols("x x1 x2 x3") 
    y, y1, y2, y3 = symbols("y y1 y2 y3")
    a, b = symbols("a b")

    eqs = [x1 * a + x2 *b + x3 * a * b - x, 
           y1 * a + y2 *b + y3 * a * b - y] 

    for i, solution in enumerate(nonlinsolve(eqs, [a, b]), start=1):
        print(f"b[{i}]={latex(solution[1])}")


if __name__ == "__main__":
    main()
