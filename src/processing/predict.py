import numpy as np
from exceptions import InvalidAgeError


class Player:

    def __init__(self, name, age, years_experience):

        self.name = name
        self.age = age
        self.years_experience = years_experience

    def _get_random_factor(self):

        if 40 <= self.age < 50:
            random_factor = -0.2

        elif 32 < self.age < 40:
            random_factor = -0.1

        elif 24 < self.age < 28:
            random_factor = 0.1

        elif 18 < self.age <= 24:
            random_factor = 0.2

        else:
            raise InvalidAgeError

        return random_factor


class Hitter(Player):

    def __init__(self,
                 name,
                 age,
                 years_experience,
                 average,
                 obp,
                 ops):

        super().__init__(name, age, years_experience)
        self.average = average
        self.obp = obp
        self.ops = ops

    def predict(self):

        random_factor = self._get_random_factor()
        average_mean = self.average + self.average*random_factor
        obp_mean = self.obp + self.average*random_factor
        ops_mean = self.ops + self.ops*random_factor

        predicted_average = np.random.normal(average_mean, 0.02)
        predicted_obp = np.random.normal(obp_mean, 0.03)
        predicted_ops = np.random.normal(ops_mean, 0.1)

        return predicted_average, predicted_obp, predicted_ops





class Pitcher(Player):

    def __init__(self,
                 name,
                 age,
                 years_experience,
                 era,
                 k_per_nine,
                 oba,
                 ):

        super().__init__(name, age, years_experience)
        self.era = era
        self.k_per_nine = k_per_nine
        self.opa = oba

    def predict(self):

        random_factor = self._get_random_factor()

        random_factor += (self.years_experience / (self.years_experience + 10))

        era_mean = self.era - self.era*random_factor
        k_per_nine_mean = self.k_per_nine + self.era*random_factor
        opa_mean = self.opa - self.opa*random_factor

        era_stdev = 0.5
        k_per_nine_stdev = 0.5
        opa_stdev = 0.02

        predicted_era = np.random.normal(era_mean, era_stdev)
        predcted_k_per_nine = np.random.normal(k_per_nine_mean, k_per_nine_stdev)
        predicted_opa = np.random.normal(opa_mean, opa_stdev)

        return predicted_era, predcted_k_per_nine, predicted_opa
