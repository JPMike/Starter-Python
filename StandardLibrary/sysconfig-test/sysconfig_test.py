if __name__ == '__main__':
    import sysconfig

    print(sysconfig.get_config_var('Py_ENABLE_SHARED'))
    print(sysconfig.get_config_var('LIBDIR'))
    print(sysconfig.get_config_vars('AR,', 'CXX'))
