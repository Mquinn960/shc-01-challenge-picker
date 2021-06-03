class SubsetFinder():

    def find_subset(self, input_array, capacity):

        def subset_sum(array, num):
            if sum([x['modifier'] for x in array]) == num:
                return array
            if len(array) > 1:
                for subset in (array[:-1], array[1:]):
                    result = subset_sum(subset, num)
                    if result is not None:
                        return result

        return subset_sum(input_array, capacity)
