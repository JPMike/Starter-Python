import pandas as pd
import numpy as np


def my_print(*args):
    print(*args, sep="\n")


def object_creation_test():
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    my_print("Series s:", s)

    dates = pd.date_range('20191104', periods=5)
    my_print("dates:", dates)

    df = pd.DataFrame(np.random.randn(5, 4), index=dates, columns=list('ABCD'))
    my_print("df:", df)
    my_print("df head:", df.head(3))
    my_print("df tail:", df.tail(3))
    my_print("df index:", df.index)
    my_print("df columns:", df.columns)
    my_print("df to numpy:", df.to_numpy())
    my_print("df describe:", df.describe())
    my_print("df transposing:", df.T)
    my_print("df sort by index:", df.sort_index(axis=1, ascending=False))
    my_print("df sort by value:", df.sort_values(by='B'))
    my_print("df get:", df['A'])
    my_print("df slice:", df[0:3])
    my_print("df slice:", df['20191104':'20191106'])
    my_print("df get by label:", df.loc[dates[0]])
    my_print("df get multi axis:", df.loc[:, ['A', 'B']])
    my_print("df get multi axis:", df.loc['20191104':'20191106', ['A', 'B']])
    my_print("df get multi axis:", df.loc['20191104', ['A', 'B']])
    my_print("df get scalar value:", df.loc[dates[0], 'A'])
    my_print("df get scalar value:", df.at[dates[0], 'A'])
    my_print("df get by position:", df.iloc[3])
    my_print("df get by position:", df.iloc[3:5, 0:2])
    my_print("df get by position:", df.iloc[[1, 2, 4], [0, 2]])
    my_print("df get by position:", df.iloc[1:3, :])
    my_print("df get by position:", df.iloc[1, 1])
    my_print("df get by position:", df.iat[1, 1])
    my_print("df boolean indexing:", df[df.A > 0])
    my_print("df boolean indexing:", df[df > 0])
    my_print("df mean:", df.mean())
    my_print("df mean on other index:", df.mean(1))

    ss = pd.Series([1, 3, 5, np.nan, 6], index=dates).shift(2)
    my_print("ss shift:", ss)
    my_print("df sub:", df.sub(ss, axis='index'))

    my_print("df:", df)
    my_print("df apply cumsum:", df.apply(np.cumsum))
    my_print("df apply lambda:", df.apply(lambda x: x.max() - x.min()))

    df_c1 = df.copy()
    df_c1['E'] = ['one', 'one', 'two', 'three', 'four']
    my_print("df_c1:", df_c1)
    my_print("df_c1 boolean indexing:", df_c1[df_c1['E'].isin(['two', 'four'])])

    s1 = pd.Series([1, 2, 3, 4, 5], index=pd.date_range('20191104', periods=5))
    my_print("s1:", s1)
    df_c2 = df.copy()
    df_c2['F'] = s1
    my_print("df_c2:", df_c2)
    df_c2.at[dates[0], 'A'] = 0
    df_c2.iat[0, 1] = 0
    df_c2.loc[:, 'D'] = np.array([5] * len(df_c2))
    df_c2[df_c2 > 0] = -df_c2
    my_print("df_c2 setting:", df_c2)

    df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
    df1.loc[dates[0]:dates[1], 'E'] = 1
    my_print("df1:", df1)
    my_print("df1 drop NA:", df1.dropna(how='any'))
    my_print("df1 fill NA:", df1.fillna(value=5))
    my_print("df1 is NA:", pd.isna(df1))

    df2 = pd.DataFrame({
        'A': 1.,
        'B': pd.Timestamp('20191104'),
        'C': pd.Series(1, index=list(range(4)), dtype='float32'),
        'D': np.array([3] * 4, dtype='int32'),
        'E': pd.Categorical(["test", "train", "test", "train"]),
        'F': 'foo'
    })
    my_print("df2:", df2)
    my_print("df2 dtypes:", df2.dtypes)
    my_print("df2 A:", df2.A)
    my_print("df2 to numpy:", df2.to_numpy())

    s2 = pd.Series(np.random.randint(1, 7, size=10))
    my_print("s2:", s2)
    my_print("s2 value counts:", s2.value_counts())

    s3 = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
    my_print("s3:", s3)
    my_print("s3 str lower:", s3.str.lower())


def merge_test():
    df = pd.DataFrame(np.random.randn(10, 4))
    my_print(df)


def test():
    # object_creation_test()
    merge_test()
    pass


if __name__ == '__main__':
    test()
    pass
