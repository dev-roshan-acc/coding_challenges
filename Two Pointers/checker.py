
class OutputChecker:
    def __init__(self, solution_func):
        
        self.solution_func = solution_func

    def run_test(self, input_args, expected_output, case_name="Test Case"):
        
        result = self.solution_func(input_args)
        passed = result == expected_output
        print(f"{case_name}: {'✅ Passed' if passed else '❌ Failed'}")
        print(f"Expected: {expected_output}")
        print(f"Got     : {result}")
        print("-" * 40)
