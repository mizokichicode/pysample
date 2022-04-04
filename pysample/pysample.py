if __package__ is None:
    import calc
    import module
else:
    from . import calc
    from . import module


def main():
    module.hello()
    print()
    print('add           : ', calc.add(10, 8))
    print('subtraction   : ', calc.subtraction(10, 8))
    print('multiplication: ', calc.multiplication(10, 8))
    print('division      : ', calc.division(10, 8))


if __name__ == '__main__':
    main()
