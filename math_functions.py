from operator import itemgetter
import math


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


OPERATORS = (
    ("amean", Stats.amean), ("gmean", Stats.gmean), ("mode", Stats.mode), ("median", Stats.median), ("arange", Stats.arange), ("grange", Stats.grange),
    ("sum", Sets.sum), ("Σ", Sets.sum), ("product", Sets.product), ("Π", Sets.product),
    ("=", Comps.equal_to), ("==", Comps.equal_to), ("=/=", Comps.not_equal_to), ("!=", Comps.not_equal_to), ("<=", Comps.less_than_e), (">=", Comps.more_than_e), ("<", Comps.less_than), (">", Comps.more_than),
    ("not", Logic._not), ("or", Logic._or), ("nor", Logic.nor), ("and", Logic._and), ("nand", Logic.nand), ("xor", Logic.xor), ("xnor", Logic.xnor), ("xand", Logic.xnor), ("imp", Logic.implies), ("nimp", Logic.nimplies), ("rimp", Logic.r_implies), ("rnimp", Logic.r_nimplies),
    ("rnd", Modifs.round), ("flr", Modifs.floor), ("cil", Modifs.ceiling), ("abs", Modifs.absolute), ("|", Modifs.absolute), ("inv", Modifs.inverse), ("rcp", Modifs.reciprocal),
    ("sin", Trig.sin), ("cos", Trig.cos), ("tan", Trig.tan), ("cot", Trig.cot), ("sec", Trig.sec), ("csc", Trig.csc),
    ("asin", Trig.arsin), ("acos", Trig.arcos), ("atan", Trig.artan), ("acot", Trig.arcot), ("asec", Trig.arsec), ("acsc", Trig.arcsc),
    ("arsin", Trig.arsin), ("arcos", Trig.arcos), ("artan", Trig.artan), ("arcot", Trig.arcot), ("arsec", Trig.arsec), ("arcsc", Trig.arcsc),
    ("arcsin", Trig.arsin), ("arccos", Trig.arcos), ("arctan", Trig.artan), ("arccot", Trig.arcot), ("arcsec", Trig.arsec), ("arccsc", Trig.arcsc),
    ("sinh", Hyper.sinh), ("cosh", Hyper.cosh), ("tanh", Hyper.tanh), ("coth", Hyper.coth), ("sech", Hyper.sech), ("csch", Hyper.csch),
    ("asinh", Hyper.arsinh), ("acosh", Hyper.arcosh), ("atanh", Hyper.artanh), ("acoth", Hyper.arcoth), ("asech", Hyper.sech), ("acsch", Hyper.arcsch),
    ("arsinh", Hyper.arsinh), ("arcosh", Hyper.arcosh), ("artanh", Hyper.artanh), ("arcoth", Hyper.arcoth), ("arsech", Hyper.sech), ("arcsch", Hyper.arcsch),
    ("arcsinh", Hyper.arsinh), ("arccosh", Hyper.arcosh), ("arctanh", Hyper.artanh), ("arccoth", Hyper.arcoth), ("arcsech", Hyper.sech), ("arccsch", Hyper.arcsch),
    ("exp", Expo.nat_power), ("pow", Expo.power), ("ln", Expo.nat_log), ("log", Expo.log),
    ("-", Single.minus), ("!", Single.gamma), ("c", Single.ncr), ("p", Single.npr),
    ("^", Index.exponent), ("**", Index.exponent), ("rt", Index.root),
    ("/", Geo.divide), ("//", Geo.floordiv), ("%", Geo.modulo), ("*", Geo.multiply),
    ("+", Arith.add), ("-", Arith.subtract)
)

NUMBERS = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", ",")

BRACKETS = (("(", "[", "{"), (")", "]", "}"))
