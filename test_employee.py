from employee import employee_info

def test_employee_details():
    result = employee_info("Amulya", "101", "BCA", "50000")

    expected = (
        "Employee Name : Amulya\n"
        "Employee ID : 101\n"
        "Department : BCA\n"
        "Salary : 50000"
    )

    assert result == expected