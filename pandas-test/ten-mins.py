import pandas as pd
import numpy as np


def object_creation():
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    print(s)


def test():
    object_creation()
    pass


if __name__ == '__main__':
    test()
    pass
