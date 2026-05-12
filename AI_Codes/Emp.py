from collections import OrderedDict


class EmployeeEvaluation:

    def __init__(self):
        self.name = input("Enter name of employee: ")

        # [rating, weightage, weighted_score]
        self.competencies = OrderedDict({
            "Communication": [0, 0, 0],
            "Productivity": [0, 0, 0],
            "Creativity": [0, 0, 0],
            "Integrity": [0, 0, 0],
            "Punctuality": [0, 0, 0],
        })

        self.performance = OrderedDict({
            "Goal 1": [0, 0, 0],
            "Goal 2": [0, 0, 0],
            "Goal 3": [0, 0, 0],
            "Goal 4": [0, 0, 0],
            "Goal 5": [0, 0, 0],
        })

    def print_table(self, data: dict, title: str, label: str):
        print(f"\n{title}")
        print(f"{label:<20} {'Rating':<10} {'Weightage':<15} {'Weighted Score'}")

        for key, value in data.items():
            print(f"{key:<20} {int(value[0]):<10} {int(value[1]):<15} {value[2]:.2f}")
        print()

    def input_data(self):
        print("Enter rating from 1-3")
        print("Weightage should be equal to 100 for each section\n")

        # Competencies input
        weight_total = 0
        for key in self.competencies:
            self.competencies[key][0] = int(input(f"Enter rating for {key}: "))
            remaining = 100 - weight_total
            self.competencies[key][1] = int(input(f"Enter weightage (remaining {remaining}): "))
            weight_total += self.competencies[key][1]

        # Performance input
        weight_total = 0
        for key in self.performance:
            self.performance[key][0] = int(input(f"Enter rating for {key}: "))
            remaining = 100 - weight_total
            self.performance[key][1] = int(input(f"Enter weightage (remaining {remaining}): "))
            weight_total += self.performance[key][1]

    def calc_score(self):
        for key in self.competencies:
            v = self.competencies[key]
            v[2] = v[0] * v[1] / 100

        for key in self.performance:
            v = self.performance[key]
            v[2] = v[0] * v[1] / 100

    def calculate(self):
        self.input_data()
        print()

        self.calc_score()

        # Competency results
        self.print_table(self.competencies, "Competency Goals", "Competency")
        sum_competency = sum(v[2] for v in self.competencies.values())
        print(f"Sum of weighted scores - Competency = {sum_competency:.2f}\n")

        # Performance results
        self.print_table(self.performance, "Performance Goals", "Goals")
        sum_performance = sum(v[2] for v in self.performance.values())
        print(f"Sum of weighted scores - Performance = {sum_performance:.2f}\n")

        # Final result
        total = sum_competency + sum_performance
        print(f"Overall Rating of {self.name} (out of 3): {total:.2f}")

        if total >= 2.7:
            print("Employee Exceeds expectations")
        elif total >= 1.7:
            print("Employee meets expectations")
        else:
            print("Employee fails expectations")


# ✅ Correct main block
if __name__ == "__main__":
    obj = EmployeeEvaluation()
    obj.calculate()