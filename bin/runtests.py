#!./bin/with-memcached python

if __name__ == "__main__":
    import pytest
    pytest.main(['--doctest-modules', '--doctest-glob=*.txt', 'src', 'tests'])
