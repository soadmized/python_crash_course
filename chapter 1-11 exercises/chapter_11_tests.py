from unittest import TestCase
from chapter_11_funcs import capitals, AnonymousSurvey, Employee


class TestCapitals(TestCase):

    def test_common_check(self):
        result = capitals('moscow', 'russia')
        self.assertEqual(result, 'Moscow, Russia')

    def test_with_population(self):
        result = capitals('moscow', 'russia', 10000000)
        self.assertEqual(result, 'Moscow, Russia. Population is 10000000')


class TestAnonimousSurvey(TestCase):

    def setUp(self):
        question = 'Are you high?'
        self.survey = AnonymousSurvey(question)
        self.responses = ['ya', 'yes', 'yeah']


    def test_question_store(self):
        for response in self.responses:
            self.survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.survey.responses)


class TestEmployee(TestCase):

    def setUp(self):
        self.salary = 50000
        self.worker = Employee('Jack', 'Richer', self.salary)
        self.new_raise = 2555
        self.new_default_salary = self.worker.salary + 5000
        self.new_custom_salary = self.worker.salary + self.new_raise

    def test_raise_default(self):
        self.worker.raise_salary()
        self.assertEqual(self.worker.salary, self.new_default_salary)

    def test_raise_custom(self):
        self.worker.raise_salary(self.new_raise)
        self.assertEqual(self.worker.salary, self.new_custom_salary)