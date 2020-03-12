class TextHandler:

    """
    Handle perf counters
    Need to create instance for each core
    """

    def __init__(self):
        self.text = text
        self.counters = {'set_entity_sum': 0, 'set_entity_total_avg': 0,
                         'process_batch_sum': 0, 'process_batch_total_avg': 0,
                         'process_event_sum': 0, 'process_event_total_avg': 0,
                         'set_rule_sum': 0, 'set_rule_total_avg': 0}

    def parser(self):
        with open('{PerfInfo}') as file:
            pass


class Plotter:

    """
    Used to give 2 sets of values - for newer and older cores
    """
    pass


if __name__ == '__main__':
    """text = input('input prompt: ')
    print(text)"""
    pass
