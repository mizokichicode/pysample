if __package__ is None:
    import calc
    import module
    import module2
else:
    from . import calc
    from . import module
    from . import module2


def main():
    module.hello()
    module2.hello2()
    print()
    print('add           : ', calc.add(10, 8))
    print('subtraction   : ', calc.subtraction(10, 8))
    print('multiplication: ', calc.multiplication(10, 8))
    print('division      : ', calc.division(10, 8))


if __name__ == '__main__':
    main()
