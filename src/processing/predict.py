import numpy as np
from exceptions import InvalidAgeError, InvalidPlayerType


class Player:

    def __init__(self, age):

        self.age = age

    def _get_random_factor(self):

        if 40 <= self.age < 50:
            random_factor = -0.2

        elif 32 < self.age < 40:
            random_factor = -0.1

        elif 24 < self.age < 28:
            random_factor = 0.1

        elif 18 <= self.age <= 24:
            random_factor = 0.2

        else:
            raise InvalidAgeError

        return random_factor


class Hitter(Player):

    def __init__(self,
                 age,
                 average,
                 obp,
                 ops):

        super().__init__(age)
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

        predictions = {"predicted_average": predicted_average,
                       "predicted_obp": predicted_obp,
                       "predicted_ops": predicted_ops}

        return predictions


class Pitcher(Player):

    def __init__(self,
                 age,
                 era,
                 k_per_nine,
                 oba,
                 ):

        super().__init__(age)
        self.era = era
        self.k_per_nine = k_per_nine
        self.opa = oba

    def predict(self):

        random_factor = self._get_random_factor()

        era_mean = self.era - self.era*random_factor
        k_per_nine_mean = self.k_per_nine + self.era*random_factor
        opa_mean = self.opa - self.opa*random_factor

        era_stdev = 0.5
        k_per_nine_stdev = 0.5
        opa_stdev = 0.02

        predicted_era = np.random.normal(era_mean, era_stdev)
        predcted_k_per_nine = np.random.normal(k_per_nine_mean, k_per_nine_stdev)
        predicted_opa = np.random.normal(opa_mean, opa_stdev)

        predictions = {"predicted_era": predicted_era,
                       "predicted_k_per_nine": predcted_k_per_nine,
                       "predicted_opa": predicted_opa}

        return predictions


def predict(stats):
    player_type = stats["type"]
    age = stats["age"]

    if player_type.upper() == "PITCHER":
        era = stats.get("era")
        oba = stats.get("oba")
        k_per_nine = stats.get("k_per_nine")
        player = Pitcher(age, era, oba, k_per_nine)

    elif player_type.upper() == "HITTER":
        avg = stats.get("average")
        obp = stats.get("obp")
        ops = stats.get("ops")
        player = Hitter(age, avg, obp, ops)

    else:
        raise InvalidPlayerType("Must enter either a hitter or a pitcher")

    return player.predict()
