from SortAlgorithm import SortAlgorithm


class CircleSort(SortAlgorithm):
    """
    Implements circle sort.
    http://www.geeksforgeeks.org/circle-sort/
    """

    def sort(self):
        yield
        swaps = 0
        s = 1
        while s:
            s = self.circle_sort(0, len(self.items.items))
            swaps += s
            yield

    def circle_sort(self, left_pos, right_pos):
        number_of_elements = right_pos - left_pos
        if number_of_elements < 2:
            return 0
        swaps = 0
        middle = number_of_elements // 2

        for i in range(middle):
            if self.cmp.gtI(left_pos + i, right_pos - (i + 1)):
                self.items.swap(left_pos + i, right_pos - (i + 1))
                swaps += 1

        if (number_of_elements & 1) and self.cmp.ltI(left_pos + middle, left_pos + middle - 1):
            self.items.swap(left_pos + middle - 1, left_pos + middle)
            swaps += 1

        return swaps + self.circle_sort(left_pos, left_pos + middle) + self.circle_sort(left_pos + middle, right_pos)
