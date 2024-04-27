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

evaluations_np = np.array(evaluations)
mean_evaluation = np.mean(evaluations_np)
median_evaluation = np.median(evaluations_np)
mode_evaluation = stats.mode(evaluations_np)
std_dev_evaluation = np.std(evaluations_np)
q1_evaluation = np.percentile(evaluations_np, 25)
q3_evaluation = np.percentile(evaluations_np, 75)

# Calculate statistics
confidences_np = np.array(confidences)
mean_confidence = np.mean(confidences_np)
median_confidence = np.median(confidences_np)
mode_confidence = stats.mode(confidences_np)
std_dev_confidence = np.std(confidences_np)
q1_confidence = np.percentile(confidences_np, 25)
q3_confidence = np.percentile(confidences_np, 75)



print("Decision Counts:")
for decision, count in decision_counts.items():
    print(f"  {decision.title()}: {count}")
