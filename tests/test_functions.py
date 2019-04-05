# Referencing the modules
#
# import pytest
# import src.flaskbasic.functions as Functions
#
#
# # instant
# fun = Functions
# # test student name
#
# def test_student_name():
#     assert fun.readName('Lwando',1) == 'Lwando'
#     assert fun.readName('Zukisa',2) == 'Zukisa'
#     assert fun.readName('ludwe',3) == 'ludwe'
#
# # test delete student function
#
# def delete(student_id):
#             student_results = Student.query.get_or_404(student_id)
#             db.session.delete(student_results)
#             db.session.commit()
#
# # test all the results
#
# def test_all_results():
#     assert fun.readResults(1,'Lwando',10, 60, 10 ) == (1, 'Lwando', 10, 60, 10)
#     assert fun.readResults(2,'Zukisa',10, 60, 5) == (2,'Zukisa',10, 60, 5)
#     assert fun.readResults(3,'ludwe',32, 12, 22) == (3,'ludwe',32, 12, 22)

# ng the modules

import pytest
from unittest import mock
from mock import Mock
from src.flaskbasic.models import Student
from src.flaskbasic.functions import Functions
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/src/flaskbasic')

# instant
# fun = Functions
# test student name
@pytest.fixture
def mock_data():
    return Mock(spec=Student)


# test student name and id
def test_student_name(mock_data):

    data = Mock(return_value = mock_data)

    assert data.readName('Lwando',1)
    assert data.readName('Zukisa',2)
    assert data.readName('ludwe',3)
