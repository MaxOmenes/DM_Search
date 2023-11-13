import model.BasicSearch as bs


class LinearSearch(bs.BasicSearch):
    name = "Linear"

    def __init__(self):
        super().__init__()

    def search(self, arr, a):
        count = 0
        for i in range(len(arr)):
            count += 1
            if arr[i] == a:
                self.setTime(count)
                return i
        return -1
