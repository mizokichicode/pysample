if __package__ is None:
    import calc
else:
    from . import calc


def main():
    print('add           : ', calc.add(10, 8))
    print('subtraction   : ', calc.subtraction(10, 8))
    print('multiplication: ', calc.multiplication(10, 8))
    print('division      : ', calc.division(10, 8))


if __name__ == '__main__':
    main()
