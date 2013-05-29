

def load(n_digit=-1):
    import os

    data = []
    digit = []
    train = os.path.join(os.path.dirname(__file__), "train.csv")
    with open(train) as f:
        for line in f.readlines()[1:n_digit]:
            pix = line.split(',')
            digit.append(pix[0])
            data.append(pix[1:])
    return (digit, data)
