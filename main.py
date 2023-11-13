import model.LinearSearch as LS
import model.BinarySearch as BS
import model.InterpolationSearch as IS


searches = {LS.LinearSearch(),
            BS.BinarySearch(),
            IS.InterpolationSearch()}

file_arr = open('input.txt', "r").read().split(",")
arr = [int(i) for i in file_arr]

output = open('output.txt', 'a')

for search in searches:
    for i in range(len(arr)):
        search.search(arr, arr[i])
    output.write(search.getName() + " " +
                 str(search.getMinTime()) + " " +
                 str(search.getAvgTime()) + " " +
                 str(search.getMaxTime()) + "\n")

output.close()
