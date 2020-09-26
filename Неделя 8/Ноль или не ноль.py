print(
    any(
        map(
            lambda x: x == '0',
            open('input.txt').read().split()
        )
    )
)