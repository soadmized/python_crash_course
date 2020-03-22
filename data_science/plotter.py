# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import re

'''
ФАЙЛ СО СЧЕТЧИКАМИ ДОЛЖЕН НАЗЫВАТЬСЯ perf_info.txt!!!
'''


class TextHandler:
    """
    Handle perf counters
    """
    def __init__(self):
        self.counters_1 = {'method': {},
                           'scenario': {},
                           'ndb': {}}

        self.counters_2 = {'method': {},
                           'scenario': {},
                           'ndb': {}}

    def _text_parser(self):
        """
        parsing counters from perf_info.txt
        :returns 2 lists contains metrics for each core
        """
        with open('perf_info.txt') as file:
            counters = file.readlines()
        handled_list = []
        for line in counters:
            line = line.split('|')
            line = [i.strip() for i in line]           # remove spaces
            if ('SetEntity' in line) or ('ProcessBatchOfEvent' in line) or ('ProcessEvent' in line) or ('SetRule' in line):   # REFACTOR THIS
                line = line[2:-5]                      # slice for scenario statistics
            else:
                line = line[-9:-5]                     # slice for methods/ndb statistics

            if (len(line) == 0) or ('Total Count' in line):
                del line
            else:
                for i in range(len(line)):
                    try:
                        line[i] = int(line[i])         # to integers
                    except:
                        pass
                handled_list.append(line)
        core_1 = handled_list[0:131]                   # split statistics for each core
        core_2 = handled_list[131:]
        return core_1, core_2

    def parse(self):
        """
        Structure:

        """
        core_1, core_2 = self._text_parser()           # returns tuple - (core_1, core_2)
        methods_1 = core_1[:11]                        # split methods, scenarios and ndb for core_1
        scenarios_1 = core_1[11:15]
        ndb_1 = core_1[15:]
        methods_2 = core_2[:11]                        # split methods, scenarios and ndb for core_2
        scenarios_2 = core_2[11:15]
        ndb_2 = core_2[15:]

        for i in range(11):
            self.counters_1['method'][methods_1[i][0]] = methods_1[i][1:]
            self.counters_2['method'][methods_2[i][0]] = methods_2[i][1:]

        for i in range(4):
            self.counters_1['scenario'][scenarios_1[i][0]] = scenarios_1[i][1:]
            self.counters_2['scenario'][scenarios_2[i][0]] = scenarios_2[i][1:]

        for i in range(116):
            self.counters_1['ndb'][ndb_1[i][0]] = ndb_1[i][1:]
            self.counters_2['ndb'][ndb_2[i][0]] = ndb_2[i][1:]

        return self.counters_1, self.counters_2


class Plotter:

    @staticmethod
    def bar(counters_tuple):
        """
        Make bar diagram for every metric except ndb counters
        """
        core_1, core_2 = counters_tuple

        core_name_1 = input('Input core_1 name: ')
        core_name_2 = input('Input core_2 name: ')

        y_axis_scenario = [i for i in core_1['scenario'].keys()]
        y_axis_method = [i for i in core_1['method'].keys()]
        y_scenario = np.arange(len(y_axis_scenario))
        y_method = np.arange(len(y_axis_method))
        width = 0.3

        fig, ((scenario_sum_time, scenario_total_avg_time),
              (method_sum_time, method_total_avg_time)) = plt.subplots(nrows=2, ncols=2)

        # SUM TIME SCENARIO PLOT
        scenario_sum_time_1 = [i[3] for i in core_1['scenario'].values()]
        scenario_sum_time_2 = [i[3] for i in core_2['scenario'].values()]
        rects1_sum_sc = scenario_sum_time.barh(y_scenario - width / 2, scenario_sum_time_1, width, label=core_name_1)
        rects2_sum_sc = scenario_sum_time.barh(y_scenario + width / 2, scenario_sum_time_2, width, label=core_name_2)
        scenario_sum_time.set_title('scenario_sum_time')
        scenario_sum_time.set_yticks(y_scenario)
        scenario_sum_time.set_yticklabels(y_axis_scenario, size=8)
        scenario_sum_time.legend()

        # TOTAL AVG TIME SCENARIO PLOT
        scenario_total_avg_time_1 = [i[4] for i in core_1['scenario'].values()]
        scenario_total_avg_time_2 = [i[4] for i in core_2['scenario'].values()]
        rects1_total_avg_sc = scenario_total_avg_time.barh(y_scenario - width / 2, scenario_total_avg_time_1, width, label=core_name_1)
        rects2_total_avg_sc = scenario_total_avg_time.barh(y_scenario + width / 2, scenario_total_avg_time_2, width, label=core_name_2)
        scenario_total_avg_time.set_title('scenario_total_avg_time')
        scenario_total_avg_time.set_yticks(y_scenario)
        scenario_total_avg_time.set_yticklabels(y_axis_scenario, size=8)
        scenario_total_avg_time.legend()

        # SUM TIME METHOD PLOT
        method_sum_time_1 = [i[1] for i in core_1['method'].values()]
        method_sum_time_2 = [i[1] for i in core_2['method'].values()]
        rects1_sum_mth = method_sum_time.barh(y_method - width / 2, method_sum_time_1, width, label=core_name_1)
        rects2_sum_mth = method_sum_time.barh(y_method + width / 2, method_sum_time_2, width, label=core_name_2)
        method_sum_time.set_title('method_sum_time')
        method_sum_time.set_yticks(y_method)
        method_sum_time.set_yticklabels(y_axis_method, size=8)
        method_sum_time.legend()

        # TOTAL AVG TIME SCENARIO PLOT
        method_total_avg_time_1 = [i[2] for i in core_1['method'].values()]
        method_total_avg_time_2 = [i[2] for i in core_2['method'].values()]
        rects1_total_avg_mth = method_total_avg_time.barh(y_method - width / 2, method_total_avg_time_1, width,
                                                        label=core_name_1)
        rects2_total_avg_mth = method_total_avg_time.barh(y_method + width / 2, method_total_avg_time_2, width,
                                                        label=core_name_2)
        method_total_avg_time.set_title('method_total_avg_time')
        method_total_avg_time.set_yticks(y_method)
        method_total_avg_time.set_yticklabels(y_axis_method, size=8)
        method_total_avg_time.legend()

        plt.show()


if __name__ == '__main__':
    handler = TextHandler()
    handled_tuple = handler.parse()
    core_1, core_2 = handled_tuple

    Plotter.bar(handled_tuple)  # using static method without class instance
