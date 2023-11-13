import model.BasicSearch as bs


class InterpolationSearch(bs.BasicSearch):
    name = "Interpolation"

    def __init__(self):
        super().__init__()

    def search(self, arr, a):
        highEnd = len(arr) - 1
        lowEnd = 0
        count = 0

        while arr[lowEnd] <= a <= arr[highEnd] and lowEnd <= highEnd:
            count += 1
            probe = int(lowEnd + (highEnd - lowEnd) * (a - arr[lowEnd]) / (arr[highEnd] - arr[lowEnd]))
            if highEnd == lowEnd:
                if arr[lowEnd] == a:
                    self.setTime(count)
                    return lowEnd
                else:
                    self.setTime(count)
                    return -1

            if arr[probe] == a:
                self.setTime(count)
                return probe

            if arr[probe] < a:
                lowEnd = probe + 1
            else:
                highEnd = probe - 1

        self.setTime(count)
        return -1
