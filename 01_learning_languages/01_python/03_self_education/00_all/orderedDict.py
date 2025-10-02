from collections import OrderedDict


def example(nums):
    odict = OrderedDict()

    for num in nums:
        odict[num] = "test"

    print(odict)
    odict.move_to_end(1)
    print(odict)
    odict.popitem(last=True)
    print(odict)
    odict.popitem(last=False)
    print(odict)


if __name__ == "__main__":
    example([1, 2, 3])
