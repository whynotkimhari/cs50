import sys

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        w, h = draw.textsize(letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        for variable in self.domains:
            for word in self.domains[variable].copy():
                if len(word) != variable.length:
                    self.domains[variable].remove(word)


    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        # x and y are variables in puzzle
        # disclaimer: x and y just can "cut" each other at 1 point, (i, j)
        # overlaps return the "cut" point if any, or None instead
        isRevise = False
        # if x and y has "cut" each other
        if self.crossword.overlaps[x, y] is not None:
            x_cut_point, y_cut_point = self.crossword.overlaps[x, y]
            for wordx in self.domains[x].copy():
                    cnt = 0
                    for wordy in self.domains[y]:
                        if wordx[x_cut_point] != wordy[y_cut_point]:
                            cnt += 1
                    if cnt == len(self.domains[y]):
                        self.domains[x].remove(wordx)
                        isRevise = True
                        
        return isRevise

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        if arcs == None:
            arcs = []
            # queue = all arcs in csp
            for var1 in self.domains:
                for var2 in self.domains:
                    if var1 != var2:
                        arcs.append((var1, var2))
        
        # while queue is not empty
        while len(arcs) != 0:
            (x, y) = arcs.pop()
            if self.revise(x, y):
                if len(self.domains[x]) == 0:
                    return False
                new_set = self.crossword.neighbors(x) - {y}
                for z in new_set:
                    arcs.append((z, x))

        return True
    
    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        values_in_assignment = []

        for var in self.domains:
            values_in_assignment.append(assignment.get(var))

        for value in values_in_assignment:
            if value == None:
                return False
            
        return True

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        # check if exist duplicate word in crossword
        if len(list(assignment.values())) > len(set(assignment.values())):
            return False
        
        # check if exist word with incorrect length in crossword
        for var in assignment:
            if var.length != len(assignment[var]):
                return False
            
        # check if exist conflict between two neighbors
        for var in assignment:
            nei = self.crossword.neighbors(var)
            for var_nei in nei:
                if var_nei in assignment:
                    (i, j) = self.crossword.overlaps[var, var_nei]
                    if assignment[var][i] != assignment[var_nei][j]:
                        return False

        return True

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        #assignment: 1key to 1word
        ranked_domain_values = []

        for word in self.domains[var]:
            cnt = 0
            for var_nei in self.crossword.neighbors(var):
                if var_nei not in assignment and word in self.domains[var_nei]:
                    cnt += 1
            ranked_domain_values.append((cnt, word))

        return [word for (cnt, word) in ranked_domain_values]

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        unassigned_variable = []

        for var in self.domains:
            if var not in assignment:
                unassigned_variable.append((var, len(self.domains[var])))
        unassigned_variable = sorted(unassigned_variable, key=lambda x : x[1])
        
        if len(unassigned_variable) > 0:
            minn = unassigned_variable[0][1]
        
        for (var, num) in unassigned_variable.copy():
            if num > minn:
                unassigned_variable.remove((var, num))
        
        degrees = []
        for (var, num) in unassigned_variable.copy():
            degrees.append((var, len(self.crossword.neighbors(var))))
        degrees = sorted(degrees, key= lambda x : x[1])
        
        maxx = degrees[-1][1]
        for (var, lnei) in degrees.copy():
            if lnei < maxx:
                degrees.remove((var, lnei))
        
        return degrees[0][0]

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        if self.assignment_complete(assignment):
            return assignment
        choice_var = self.select_unassigned_variable(assignment)
        
        for word in self.order_domain_values(choice_var, assignment):
            assignment[choice_var] = word
            if self.consistent(assignment):
                result = self.backtrack(assignment)
                if result != None:
                    return result
            assignment.pop(choice_var)

        return None


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()
    
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
