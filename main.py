import json
import numpy as np
from scipy import stats

file_path = 'dataset/reviews.json'

decision_counts = {
    'accept': 0,
    'probably reject': 0,
    'reject': 0,
    'no decision': 0
}

# Lists to store the data for each feature
evaluations = []
confidences = []
orientations = []
nullValuesCount= 0

# Open the JSON file with UTF-8 encoding and load its data
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

#Collecting the data in the .json file
for paper in data['paper']:
    print("Paper ID:", paper['id'])
    decision = paper['preliminary_decision'].lower()
    print("Preliminary Decision:", decision)


    if decision in decision_counts:
        decision_counts[decision] += 1
    else:
        decision_counts[decision] = 1

    print("Reviews:")
    for review in paper['review']:
        print("  Review ID:", review['id'])
        print("  Evaluation:", review['evaluation'])
        print("  Confidence:", review['confidence'])
        print("  Date:", review['timespan'])
        print("")
    print()

for paper in data['paper']:
    print(r"Paper ID:", paper['id'])
    for review in paper['review']:
        print(r"Review nr:", review['id'])
        if 'evaluation' in review:
            if review['evaluation'] is not None:
                evaluations.append(int(review['evaluation']))
            else:
                nullValuesCount = nullValuesCount + 1

                
                
        if 'confidence' in review:
            if review['confidence'] is not None:
                confidences.append(int(review['confidence']))
            else:
                nullValuesCount = nullValuesCount + 1



        if 'orientation' in review:
            if review['orientation'] is not None:
                orientations.append(int(review['orientation']))
            else:
                nullValuesCount = nullValuesCount + 1

print(f"There are combined {nullValuesCount} null values for orientation, confidence and evaluation.")


# Calculate the statistics we want

evalu = np.array(evaluations)
meanEvalu = np.mean(evalu)
medianEvalu = np.median(evalu)
modeEvalu = stats.mode(evalu)
stddDevEvalu = np.std(evalu)
q1Evalu = np.percentile(evalu, 25)
q3Evalu = np.percentile(evalu, 75)

# Calculate statistics
conf = np.array(confidences)
meanConf = np.mean(conf)
medianConf = np.median(conf)
modeConf = stats.mode(conf)
stddDevConfi = np.std(conf)
q1Conf = np.percentile(conf, 25)
q3Conf = np.percentile(conf, 75)



print("Decision Counts:")
for decision, count in decision_counts.items():
    print(f"  {decision.title()}: {count}")
