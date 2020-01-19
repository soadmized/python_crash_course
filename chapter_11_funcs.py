def capitals(city: str, country: str, population=''):
    """
    Function returns capital of country and country like 'City, Country'
    """
    if population:
        result = "{0}, {1}. Population is {2}".format(city.title(), country.title(), str(population))
    else:
        result = "{0}, {1}".format(city.title(), country.title())
    #print(result)
    return result


class AnonymousSurvey():

    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        print("Survey results: ")
        for response in self.responses:
            print("- " + response)


class Employee():

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def raise_salary(self, new_raise=5000):
        self.salary += new_raise



if __name__ == "__main__":

    cities = {'Russia': 'moscow', 'germany': 'Berlin', 'Austria': 'Vienna'}
    for key, value in cities.items():
        print(capitals(value, key))

    question = "What language did you first learn to speak?"
    my_survey = AnonymousSurvey(question)
    my_survey.show_question()
    print("Enter 'q' at any time to quit.\n")
    while True:
        response = input("Language: ")
        if response == 'q':
            break
        my_survey.store_response(response)
    my_survey.show_results()
    jack = Employee('Jack', 'Richer', 50000)
    jack.raise_salary(1000)
    jack.raise_salary()
    print(jack.salary)

