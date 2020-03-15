import re


class TextHandler:

    """
    Handle perf counters
    Need to create instance for each core
    """

    def __init__(self):
        """
        Dict structure: success error total_count sum_time total_avg_time
        """
        self.old_set_entity = {}
        self.old_process_batch = {}
        self.old_process_event = {}
        self.old_set_rule = {}
        self.new_set_entity_ = {}
        self.new_process_batch = {}
        self.new_process_event = {}
        self.new_set_rule = {}

    def text_parser(self):
        """
        parsing counters from perf_info.txt
        """
        with open('perf_info.txt') as file:
            counters = file.readlines()
        flag = False
        handled_counters = []
        for line in counters:
            line = line.split('|')
            line = [i.strip() for i in line]  # remove spaces
            line = line[2:-5]
            if (len(line) == 0) or ('Scenario' in line):
                del line
            else:
                handled_counters.append(line)
        return handled_counters

    def counters_parser(self, handled_counters):
        """
        parsing counters for each scenario
        :param handled_counters:
        :return:
        """
        pass




class Plotter:

    """
    Used to give 2 sets of values - for newer and older cores
    """
    pass


if __name__ == '__main__':
    handler = TextHandler()
    handler.text_parser()