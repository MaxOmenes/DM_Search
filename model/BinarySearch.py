import model.BasicSearch as bs


class BinarySearch(bs.BasicSearch):
    name = "Binary"

    def __init__(self):
        super().__init__()

    def search(self, arr, a):
        l = 0
        r = len(arr)
        count = 0
        while l <= r:
            count += 1

            mid = l + (r - l) // 2

            if arr[mid] == a:
                self.setTime(count)
                return mid

            elif arr[mid] < a:
                l = mid + 1

            else:
                r = mid - 1

        return -1