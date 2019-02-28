from abc import ABC, abstractmethod

class ScoreBoardBase(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calculate_score(self):
        pass

class ScoreBoard:
    def __init__(self):
        self.model = None

    # Utility method
    @staticmethod
    def show_score(taps, multiplier):
        print(self.model.calculate_score(taps, multiplier))


class Balloon(ScoreBoardBase):
    def calculate_score(self, taps, multiplier):
        return (taps * multiplier) - 20


class SquareBalloon(ScoreBoardBase):
    def calculate_score(self, taps, multiplier):
        return (taps * multiplier) + 40


class Clown(ScoreBoardBase):
    def calculate_score(self, taps, multiplier):
        return (taps * multiplier) - 10



def main():
    # Entry point if not imported...
    sb = ScoreBoard()
    sb.model = Balloon()
    print("Balloon Tap Score: %i" % sb.model.calculate_score(10,5))

    sb.model = Clown()
    print("Clown Tap Score: %i" % sb.model.calculate_score(10,5))

    sb.model = SquareBalloon()
    print("SquareBalloon Tap Score: %i" % sb.model.calculate_score(10,5))

if __name__ == '__main__':
    main()