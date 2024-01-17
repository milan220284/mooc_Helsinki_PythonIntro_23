# WRITE YOUR SOLUTION HERE:
<<<<<<< HEAD
=======
class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
        frequences = {}
        for el in my_list:
            if el not in frequences.keys():
                frequences[el] = 1
            else:
                frequences[el] += 1
        
        max = 0
        max_entery = None
        for max_el, el in frequences.items():
            if el > max:
                max = el
                max_entery = max_el

        return max_entery

    @classmethod
    def doubles(cls, my_list: list):
        frequences = {}
        for el in my_list:
            if el not in frequences.keys():
                frequences[el] = 1
            else:
                frequences[el] += 1
        
        count = 0
        for el in frequences.values():
            if el > 1:
                count += 1

        return count
>>>>>>> a9d893b (finished part 9)
