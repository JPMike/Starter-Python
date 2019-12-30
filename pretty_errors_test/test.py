def foo():
    return 1 / 0


if __name__ == '__main__':
    import pretty_errors

    foo()
    pass
