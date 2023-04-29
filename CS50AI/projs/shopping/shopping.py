import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    evidence = []
    labels = []
    with open(filename) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            e = []
            for j in range(len(row)):
                if j in [1, 3, 5, 6, 7, 8, 9]:
                    e.append(float(row[j]))
                elif j == 10:
                    if row[j] == "Jan":
                        e.append(int(0))
                    elif row[j] == "Feb":
                        e.append(int(1))
                    elif row[j] == "Mar":
                        e.append(int(2))
                    elif row[j] == "Apr":
                        e.append(int(3))
                    elif row[j] == "May":
                        e.append(int(4))
                    elif row[j] == "June":
                        e.append(int(5))
                    elif row[j] == "Jul":
                        e.append(int(6))
                    elif row[j] == "Aug":
                        e.append(int(7))
                    elif row[j] == "Sep":
                        e.append(int(8))
                    elif row[j] == "Oct":
                        e.append(int(9))
                    elif row[j] == "Nov":
                        e.append(int(10))
                    else:
                        e.append(int(11))
                elif j == 15:
                    if row[j] == "Returning_Visitor":
                        e.append(int(1))
                    else:
                        e.append(int(0))  
                elif j == 16:
                    if row[j] == "FALSE":
                        e.append(int(0))
                    else:
                        e.append(int(1))
                elif j == 17:
                    if row[j] == "FALSE":
                        labels.append(int(0))
                    else:
                        labels.append(int(1))
                else:
                    e.append(int(row[j]))
            evidence.append(e)
    return (evidence, labels)

def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = KNeighborsClassifier(n_neighbors = 1)
    model.fit(evidence, labels)
    return model


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    total1 = 0
    total2 = 0
    sensitivity = 0
    specificity = 0
    for actual, predicted in zip(labels, predictions):
        if actual == 0:
            total1 += 1
            if actual == predicted:
                specificity += 1
        else:
            total2 += 1
            if actual == predicted:
                sensitivity += 1
            
    sensitivity = sensitivity / total2
    specificity = specificity / total1
    return (sensitivity, specificity)


if __name__ == "__main__":
    main()
