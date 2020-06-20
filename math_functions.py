from operator import itemgetter
import math


class Const:
    def e():
        return math.e

    def pi():
        return math.pi

    def g():
        return 9.80665


class Stats:
    def amean(num_list):
        total = 0
        for num in num_list:
            total += num
        total /= len(num_list)
        return total

    def gmean(num_list):
        total = 1
        for num in num_list:
            total *= num
        total **= (1 / len(num_list))
        return total

    def mode(num_list):
        numbers = list()
        for num in num_list:
            numbers.append((num, num_list.count(num)))
        sorted_nums = sorted(numbers, key=itemgetter(1), reverse=True)
        mode = sorted_nums[0][0]
        return mode

    def median(num_list):
        length = len(num_list)
        sorted_nums = sorted(num_list)
        if length % 2 == 0:
            median = (sorted_nums[length / 2] + sorted_nums[length / 2 + 1]) / 2
        else:
            median = sorted_nums[(length + 1) / 2]
        return median

    def arange(num_list):
        sorted_nums = sorted(num_list)
        arange = sorted_nums[len(num_list) - 1] - sorted_nums[0]
        return arange

    def grange(num_list):
        sorted_nums = sorted(num_list)
        grange = sorted_nums[len(num_list) - 1] / sorted_nums[0]
        return grange


class Sets:
    def sum(num_list):
        total = 0
        for num in num_list:
            total += num
        return total

    def product(num_list):
        total = 1
        for num in num_list:
            total *= num
        return total


class Comps:
    def equal_to(a, b):
        return a == b

    def not_equal_to(a, b):
        return a != b

    def less_than_e(a, b):
        return a <= b

    def more_than_e(a, b):
        return a >= b

    def less_than(a, b):
        return a < b

    def more_than(a, b):
        return a > b


class Logic:
    def _not(b):
        return not b

    def _or(a, b):
        return a or b

    def nor(a, b):
        return not (a or b)

    def _and(a, b):
        return a and b

    def nand(a, b):
        return not (a and b)

    def xor(a, b):
        return (not (a and b)) and (a or b)

    def xnor(a, b):
        return not ((not (a and b)) and (a or b))

    def implies(a, b):
        return (not a) or b

    def nimplies(a, b):
        return not ((not a) or b)

    def r_implies(a, b):
        return a or (not b)

    def r_nimplies(a, b):
        return not(a or (not b))


class Modifs:
    def round(b):
        return round(b)

    def floor(b):
        return math.floor(b)

    def ceiling(b):
        return math.ceil(b)

    def absolute(b):
        return abs(b)

    def inverse(b):
        return -b

    def reciprocal(b):
        return 1 / b


class Trig:
    def sin(b):
        return math.sin(b)

    def cos(b):
        return math.cos(b)

    def tan(b):
        return math.tan(b)

    def cot(b):
        return 1 / math.tan(b)

    def sec(b):
        return 1 / math.cos(b)

    def csc(b):
        return 1 / math.sin(b)

    def arsin(b):
        return math.asin(b)

    def arcos(b):
        return math.acos(b)

    def artan(b):
        return math.atan(b)

    def arcot(b):
        return math.atan(1 / b)

    def arsec(b):
        return math.acos(1 / b)

    def arcsc(b):
        return math.asin(1 / b)


class Hyper:
    def sinh(b):
        return math.sinh(b)

    def cosh(b):
        return math.cosh(b)

    def tanh(b):
        return math.tanh(b)

    def coth(b):
        return 1 / math.tanh(b)

    def sech(b):
        return 1 / math.cosh(b)

    def csch(b):
        return 1 / math.sinh(b)

    def arsinh(b):
        return math.asinh(b)

    def arcosh(b):
        return math.acosh(b)

    def artanh(b):
        return math.atanh(b)

    def arcoth(b):
        return math.atanh(1 / b)

    def arsech(b):
        return math.acosh(1 / b)

    def arcsch(b):
        return math.asinh(1 / b)


class Expo:
    def nat_power(b):
        return math.e ** b

    def power(a, b):
        return a ** b

    def nat_log(b):
        return math.log(b)

    def log(a, b):
        return math.log(b, a)


class Single:
    def minus(b):
        return -b

    def gamma(a):
        return math.gamma(a)

    def ncr(a, b):
        return math.gamma(a) / math.gamma(b) / math.gamma(a - b)

    def npr(a, b):
        return math.gamma(a) / math.gamma(a - b)


class Index:
    def exponent(a, b):
        return a ** b

    def root(a, b):
        return b ** (1 / a)


class Geo:
    def divide(a, b):
        return a / b

    def floordiv(a, b):
        return a // b

    def modulo(a, b):
        return a % b

    def multiply(a, b):
        return a * b


class Arith:
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b


# a o b
# 1 = *, 2 = a, 3 = b, 4 = ab, 5 = list

OPERATORS = (
    ("e", Const.e, 1), ("pi", Const.pi, 1), ("π", Const.pi, 1), ("g", Const.g, 1),
    ("amean", Stats.amean, 5), ("gmean", Stats.gmean, 5), ("mode", Stats.mode, 5), ("median", Stats.median, 5), ("arange", Stats.arange, 5), ("grange", Stats.grange, 5),
    ("sum", Sets.sum, 5), ("Σ", Sets.sum, 5), ("product", Sets.product, 5), ("Π", Sets.product, 5),
    ("=", Comps.equal_to, 4), ("==", Comps.equal_to, 4), ("=/=", Comps.not_equal_to, 4), ("!=", Comps.not_equal_to, 4), ("<=", Comps.less_than_e, 4), (">=", Comps.more_than_e, 4), ("<", Comps.less_than, 4), (">", Comps.more_than, 4),
    ("not", Logic._not, 4), ("or", Logic._or, 4), ("nor", Logic.nor, 4), ("and", Logic._and, 4), ("nand", Logic.nand, 4), ("xor", Logic.xor, 4), ("xnor", Logic.xnor, 4), ("xand", Logic.xnor, 4), ("imp", Logic.implies, 4), ("nimp", Logic.nimplies, 4), ("rimp", Logic.r_implies, 4), ("rnimp", Logic.r_nimplies, 4),
    ("rnd", Modifs.round, 3), ("flr", Modifs.floor, 3), ("cil", Modifs.ceiling, 3), ("abs", Modifs.absolute, 3), ("|", Modifs.absolute, 3), ("inv", Modifs.inverse, 3), ("rcp", Modifs.reciprocal, 3),
    ("sin", Trig.sin, 3), ("cos", Trig.cos, 3), ("tan", Trig.tan, 3), ("cot", Trig.cot, 3), ("sec", Trig.sec, 3), ("csc", Trig.csc, 3),
    ("asin", Trig.arsin, 3), ("acos", Trig.arcos, 3), ("atan", Trig.artan, 3), ("acot", Trig.arcot, 3), ("asec", Trig.arsec, 3), ("acsc", Trig.arcsc, 3),
    ("arsin", Trig.arsin, 3), ("arcos", Trig.arcos, 3), ("artan", Trig.artan, 3), ("arcot", Trig.arcot, 3), ("arsec", Trig.arsec, 3), ("arcsc", Trig.arcsc, 3),
    ("arcsin", Trig.arsin, 3), ("arccos", Trig.arcos, 3), ("arctan", Trig.artan, 3), ("arccot", Trig.arcot, 3), ("arcsec", Trig.arsec, 3), ("arccsc", Trig.arcsc, 3),
    ("sinh", Hyper.sinh, 3), ("cosh", Hyper.cosh, 3), ("tanh", Hyper.tanh, 3), ("coth", Hyper.coth, 3), ("sech", Hyper.sech, 3), ("csch", Hyper.csch, 3),
    ("asinh", Hyper.arsinh, 3), ("acosh", Hyper.arcosh, 3), ("atanh", Hyper.artanh, 3), ("acoth", Hyper.arcoth, 3), ("asech", Hyper.sech, 3), ("acsch", Hyper.arcsch, 3),
    ("arsinh", Hyper.arsinh, 3), ("arcosh", Hyper.arcosh, 3), ("artanh", Hyper.artanh, 3), ("arcoth", Hyper.arcoth, 3), ("arsech", Hyper.sech, 3), ("arcsch", Hyper.arcsch, 3),
    ("arcsinh", Hyper.arsinh, 3), ("arccosh", Hyper.arcosh, 3), ("arctanh", Hyper.artanh, 3), ("arccoth", Hyper.arcoth, 3), ("arcsech", Hyper.sech, 3), ("arccsch", Hyper.arcsch, 3),
    ("exp", Expo.nat_power, 3), ("pow", Expo.power, 4), ("ln", Expo.nat_log, 3), ("log", Expo.log, 4),
    ("-", Single.minus, 3), ("!", Single.gamma, 2), ("c", Single.ncr, 4), ("p", Single.npr, 4),
    ("^", Index.exponent, 4), ("**", Index.exponent, 4), ("rt", Index.root, 4),
    ("/", Geo.divide, 4), ("//", Geo.floordiv, 4), ("%", Geo.modulo, 4), ("*", Geo.multiply, 4),
    ("+", Arith.add, 4), ("-", Arith.subtract, 4)
)

OPERATOR_STRINGS = list()
for operator_tuple in OPERATORS:
    OPERATOR_STRINGS.append(operator_tuple[0])

NUMBERS = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", ",")

BRACKETS = (("(", "[", "{"), (")", "]", "}"))
