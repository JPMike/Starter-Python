if __name__ == '__main__':
    import copy

    # recursive list, experiment, should not do that
    x = [1]
    x.append(x)
    y = copy.deepcopy(x)
    print(f"x is y: {x is y}")  # should be False
    print(f"x == y: {x == y}")  # maximum recursion depth exceeded in comparison
