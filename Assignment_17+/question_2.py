CLASSIFICATION = 0
WEIGHT = 1


class Sample:
    def __init__(self, value: float = 3.7, classification: str = "cat") -> None:
        self.value = value
        self.classification = classification

class ClosestMeanClassifier:
    def __init__(self, sample_list) -> None:
        self.sample_dict = self.sample_list_into_dict(sample_list)
        self.sample_avg = self.calculate_avg()

    def calculate_avg(self):
        sample_avg = {}

        for sample in self.sample_dict:
            avg = self.sample_dict[sample][0] / self.sample_dict[sample][1]
            sample_avg[sample] = avg

        return sample_avg


    def sample_list_into_dict(self, sample_list):
        sample_dict = {}

        for sample in sample_list:
            if sample.classification in sample_dict:
                sample_dict[sample.classification][0] += sample.value
                sample_dict[sample.classification][1] += 1
            else:
                sample_dict[sample.classification] = [sample.value, 1]

        return sample_dict

    def classify(self, weight):
        closest = None
        for sample in self.sample_avg:
            dist = abs(weight - self.sample_avg[sample])
            if closest:
                if closest[WEIGHT] > dist:
                    closest[WEIGHT] = dist
                    closest[CLASSIFICATION] = sample
            else:
                closest = [sample, dist]

        return closest[0]

def samples():

    men_heights = [186, 182, 188, 183, 174, 192, 177, 163, 180, 166]

    women_heights = [167, 174, 174, 167, 159, 169, 166, 165, 174, 163]

    men_samples = [Sample(height, "m") for height in men_heights]

    women_samples = [Sample(height, "f") for height in women_heights]

    return men_samples + women_samples

classifier = ClosestMeanClassifier(samples())

print(classifier.classify(154))
