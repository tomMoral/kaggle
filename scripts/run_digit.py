#*------------------------------------------------
#   tomMoral


if __name__ == '__main__':
    import numpy as np

    from sklearn.multiclass import OneVsRestClassifier
    from sklearn.svm import LinearSVC

    import digit.load_digit as dg

    dataset = dg.load(1000)
    print dataset[0]
    lab = OneVsRestClassifier(LinearSVC(random_state=0)).fit(dataset[1], dataset[0]).predict(dataset[1])
    print lab
    count = np.zeros((10, 10))
    for i, l in enumerate(lab):
        count[l][int(dataset[0][i])] += 1
    print count.nonzero()
    raw_input("Press Enter to quit...")
