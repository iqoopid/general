class MoreMeth():

    def __init__(glad, array):
        glad.array1 = array
        

    def concat(own, array2):
        for i in array2:
            own.array1.append(i)
        return own.array1

# a = MoreMeth()
# array2 = ["eta", "theta", "iota", "kappa", "lambda", "mu"]
# b, c = a.concat(array2)
# print(b, "\n", c)
