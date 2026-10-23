from grade_calculator import calculate_grade
def test_grade_a():
    assert calculate_grade(95) == "A"
def test_grade_b():
    assert calculate_grade(80) == "B"
def test_grade_c():
    assert calculate_grade(65) == "C"
def test_grade_d():
    assert calculate_grade(40) == "D"
def test_fail():
    assert calculate_grade(20) == "Fail"
def test_invalid_marks():
    assert calculate_grade(101) == "Invalid marks"
    assert calculate_grade(-5) == "Invalid marks"
def test_boundary_marks():
    assert calculate_grade(90) == "A"
    assert calculate_grade(75) == "B"
    assert calculate_grade(60) == "C"
    assert calculate_grade(35) == "D"
