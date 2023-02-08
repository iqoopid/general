class MoreMeth():

    def concat(own, array2):
        array0 = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta", "iota", "kappa", "lambda", "mu"]
        array1 = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta"]
        for i in array2:
            array1.append(i)
        return array1, array0

# a = MoreMeth()
# array2 = ["eta", "theta", "iota", "kappa", "lambda", "mu"]
# b, c = a.concat(array2)
# print(b, "\n", c)
