import copy
import random


class MarkovChain:
    def __init__(self):
        self.values = {}

    def fit(self, sequence) -> None:
        for i in range(len(sequence) - 1):
            if sequence[i] in self.values.keys():
                self.values[sequence[i]][sequence[i + 1]] = self.values[sequence[i]].get(sequence[i + 1], 0) + 1
            else:
                self.values[sequence[i]] = {sequence[i + 1]: 1}

    def forward(self, kernel, length):
        ret_list = copy.copy(kernel)
        for i in range(length):
            cur = ret_list[len(ret_list) - 1]
            value = self.values.get(cur, self.values[random.choice(list(self.values.keys()))])
            keys = [key for key in value.keys()]
            ret_list.append((random.choices(keys, weights=[value[key] for key in keys]))[0])
        return ret_list