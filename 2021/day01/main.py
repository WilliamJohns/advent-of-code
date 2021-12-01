def part_1(nums: list[int]) -> None:
    """1553"""
    count = 0
    prev = nums[0]
    for n in nums[1:]:
        if n > prev:
            count += 1
        prev = n
    print(f"Part 1: {count=}")

def part_2(nums: list[int]) -> None:
    """1597"""
    count = 0
    prev = sum(nums[:3])
    for idx, _ in enumerate(nums[1:-1]):
        n = prev - nums[idx-1] + nums[idx+2]
        if n > prev:
            count += 1
    print(f"Part 2: {count=}")

def main():
    with open("input.txt", "r") as f:
        nums = list(map(int, f.readlines()))

    part_1(nums)
    part_2(nums)


if __name__ == "__main__":
    main()

