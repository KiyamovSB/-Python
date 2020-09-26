from functools import reduce

print(
    reduce(lambda x, y: x*y,
            list(
                map(
                    lambda x: int(x)**5,
                    input().split()
                )
            )
    )
)