import importlib.util
import subprocess
import sys
from unittest import mock


def run_program(filename, inputs):
    process = subprocess.Popen(
        [sys.executable, filename],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    input_text = "\n".join(inputs)
    stdout, _ = process.communicate(input=input_text)
    return stdout


def load_module(filename, module_name):
    spec = importlib.util.spec_from_file_location(module_name, filename)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class TestDictConcept:
    def test_get_config_returns_expected_dict(self):
        mod = load_module("dict_concept.py", "dict_concept")
        assert mod.get_config() == {
            "width": 480,
            "height": 480,
            "color_mode": "dark",
            "sensitivity": 0.4,
        }


class TestDictStore:
    def test_temp_and_color_present(self):
        mod = load_module("dict_store.py", "dict_store")
        data = {"temp": 22.5, "color": "blue", "status": "ok"}
        assert mod.temp_and_color(data) == (22.5, "blue")

    def test_temp_and_color_missing_keys(self):
        mod = load_module("dict_store.py", "dict_store")
        assert mod.temp_and_color({"status": "ok"}) == (None, None)


class TestDictFunc:
    def test_employee_print_empty_dict(self, capsys):
        mod = load_module("dict_func.py", "dict_func")
        mod.employee_print({})
        output = capsys.readouterr().out
        assert "Name: N/A" in output
        assert "Salary: N/A" in output
        assert "Role: N/A" in output
        assert "No other info!" in output

    def test_employee_print_with_extra_fields(self, capsys):
        mod = load_module("dict_func.py", "dict_func")
        employee = {
            "Name": "Diego",
            "Salary": 5000000,
            "Role": "Janitor",
            "Years at company": 9001,
            "Hours per week": 2,
        }
        mod.employee_print(employee)
        output = capsys.readouterr().out
        assert "Name: Diego" in output
        assert "Salary: 5000000" in output
        assert "Role: Janitor" in output
        assert "Years at company: 9001" in output
        assert "Hours per week: 2" in output
        assert "No other info!" not in output


class TestDebugging:
    def test_view_inventory_and_exit(self):
        output = run_program("debugging.py", ["1", "4"])
        assert "Welcome to the Fruit Shop!" in output
        assert "Current Inventory:" in output
        assert "apples: 10" in output
        assert "bananas: 20" in output
        assert "oranges: 15" in output
        assert "Goodbye!" in output

    def test_add_update_and_view(self):
        output = run_program("debugging.py", ["2", "grapes", "40", "3", "apples", "5", "1", "4"])
        assert "grapes added with stock 40." in output
        assert "apples stock increased by 5." in output
        assert "apples: 15" in output
        assert "grapes: 40" in output

    def test_update_missing_fruit(self):
        output = run_program("debugging.py", ["3", "mango", "4"])
        assert "mango is not in inventory. Use option 2 to add it." in output


class TestOverall:
    def setup_method(self):
        self.mod = load_module("overall.py", "overall")

    def test_student_averages(self):
        students = {
            "s1": {"hw1": 80, "hw2": 90, "hw3": 100},
            "s2": {"hw1": 70, "hw2": 75, "hw3": 85},
            "s3": {"hw1": 95, "hw2": 85, "hw3": 90},
        }
        assert self.mod.student_averages(students) == {"s1": 90, "s2": 77, "s3": 90}

    def test_assignment_averages(self):
        students = {
            "s1": {"hw1": 80, "hw2": 90, "hw3": 100},
            "s2": {"hw1": 70, "hw2": 75, "hw3": 85},
            "s3": {"hw1": 95, "hw2": 85, "hw3": 90},
        }
        assert self.mod.assignment_averages(students) == {"hw1": 82, "hw2": 83, "hw3": 92}

    def test_empty_input(self):
        assert self.mod.student_averages({}) == {}
        assert self.mod.assignment_averages({}) == {}


class TestGradesManager:
    def setup_method(self):
        self.mod = load_module("grades_manager.py", "grades_manager")

    def test_initialize_dict(self):
        result = self.mod.initialize_dict("Alice", {"Math": 90.5, "English": 85.0})
        assert result == {"Alice": {"Math": 90.5, "English": 85.0}}

    def test_add_student(self, capsys):
        with mock.patch("builtins.input", side_effect=["john doe", "Math,95", "Science,88.5", "exit"]):
            result = self.mod.add_student({})
        output = capsys.readouterr().out
        assert "Student John Doe successfully added to the grades management system." in output
        assert result == {"John Doe": {"Math": 95.0, "Science": 88.5}}

    def test_get_students_case_insensitive_and_missing(self, capsys):
        data = {
            "Alice": {"Math": 90.5, "English": 85.0},
            "Bob": {"Science": 88.0, "History": 92.0},
        }
        result = self.mod.get_students(data, ["alice", "CHARLIE", "BOB"])
        output = capsys.readouterr().out
        assert "Charlie not found!" in output
        assert result == {
            "Alice": {"Math": 90.5, "English": 85.0},
            "Bob": {"Science": 88.0, "History": 92.0},
        }

    def test_avg_by_student_all(self, capsys):
        data = {
            "Alice": {"Math": 70.0, "English": 60.0},
            "Ben": {"Science": 55.0, "History": 66.0},
        }
        self.mod.avg_by_student(data)
        output = capsys.readouterr().out
        assert "Alice: 65.0" in output
        assert "Ben: 60.5" in output

    def test_avg_by_student_selected(self, capsys):
        data = {
            "Alice": {"Math": 70.0, "English": 60.0},
            "Charlie": {"Math": 90.0, "Science": 85.0},
        }
        self.mod.avg_by_student(data, ["alice", "DAVID"])
        output = capsys.readouterr().out
        assert "David not found!" in output
        assert "Alice: 65.0" in output


class TestMainProgram:
    def test_main_add_and_show_all(self):
        output = run_program(
            "main.py",
            ["1", "john doe", "Math,95", "Science,88.5", "exit", "2", "a", "3"],
        )
        assert "Welcome to the Student Grades Manager!" in output
        assert "Student John Doe successfully added to the grades management system." in output
        assert "John Doe: 91.8" in output
        assert "Goodbye!" in output

    def test_main_selected_students(self):
        output = run_program(
            "main.py",
            ["1", "john doe", "Math,95", "Science,88.5", "exit", "2", "b", "Jane Doe,JOHN DOE", "3"],
        )
        assert "Jane Doe not found!" in output
        assert "John Doe: 91.8" in output

    def test_main_invalid_options(self):
        output = run_program("main.py", ["9", "2", "c", "3"])
        assert output.count("Invalid option selected!") >= 2


class TestDebugTopScorer:
    def test_top_scorer_with_accumulation(self):
        output = run_program("debug_top_scorer.py", ["Alice 10", "Bob 12", "Alice 8", "stop"])
        assert "Top scorer: Alice with 18 points." in output

    def test_empty_scores(self):
        output = run_program("debug_top_scorer.py", ["STOP"])
        assert "No scores recorded." in output


class TestIndustrialTemperature:
    def setup_method(self):
        self.mod = load_module("industrial_temperature.py", "industrial_temperature")

    def test_trigger_alarm_with_custom_threshold(self):
        temperatures = {
            "sensor_1": 85.5,
            "sensor_2": 90.2,
            "sensor_3": 78.8,
            "sensor_4": 92.3,
        }
        assert self.mod.trigger_alarm(temperatures, 88) == ["sensor_2", "sensor_4"]

    def test_trigger_alarm_with_default_threshold(self):
        temperatures = {
            "sensor_A": 79.0,
            "sensor_B": 81.2,
            "sensor_C": 75.4,
            "sensor_D": 85.7,
        }
        assert self.mod.trigger_alarm(temperatures) == ["sensor_B", "sensor_D"]

    def test_trigger_alarm_empty(self):
        assert self.mod.trigger_alarm({}) == []


class TestAcknowledgments:
    def test_acknowledgments_filled(self):
        with open("acknowledgments.txt", "r", encoding="utf-8") as f:
            content = f.read()

        assert "[escribe" not in content.lower()
        assert "github.com" in content.lower()
        assert "/s/" in content


if __name__ == "__main__":
    import pytest

    pytest.main([__file__, "-v"])
