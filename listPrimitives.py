from program import *

import math

def _multiplication(x): return lambda y: x*y
def _addition(x): return lambda y: x + y
def _subtraction(x): return lambda y: x - y
def _reverse(x): return list(reversed(x))
def _append(x): return lambda y: x + y
def _single(x): return [x]
def _slice(x): return lambda y: lambda l: l[x:y]
def _map(f): return lambda l: map(f,l)
def _reduce(f): return lambda x0: lambda l: reduce(lambda a,b: f(a)(b),l,x0)
def _filter(f): return lambda l: filter(f,l)
def _eq(x): return lambda y: x == y
def _mod(x): return lambda y: x%y
def _not(x): return not x
def _gt(x): return lambda y: x > y
def _index(j): return lambda l: l[j]
def _isPrime(n):
    return n in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
def _isSquare(n):
    r = int(math.sqrt(n))
    return r*r == n
primitives = [
    Primitive("index",arrow(tint,tlist(tint),tint),_index),
    Primitive("+",arrow(tint,tint),_addition),
    Primitive("*",arrow(tint,tint),_multiplication),
    Primitive("-",arrow(tint,tint),_subtraction),
    Primitive("sort",arrow(tlist(tint),tlist(tint)),sorted),
    Primitive("reverse",arrow(tlist(tint),tlist(tint)),_reverse),
    Primitive("++",arrow(tlist(tint),tlist(tint),tlist(tint)),_append),
    Primitive("singleton",arrow(tint,tlist(tint)),_single),
    Primitive("slice",arrow(tint,tint,tlist(tint),tlist(tint)),_slice),
    Primitive("len",arrow(tlist(tint),tint),len),
    Primitive("map",arrow(arrow(tint,tint),tlist(tint),tlist(tint)),_map),
    Primitive("reduce",arrow(arrow(tint,tint), tint, tlist(tint), tint),_reduce),
    Primitive("filter",arrow(arrow(tint,tbool), tlist(tint), tlist(tint)),_filter),
    Primitive("eq?",arrow(tint,tint,tbool), _eq),
    Primitive("mod",arrow(tint,tint,tint), _mod),
    Primitive("not",arrow(tbool,tbool), _not),
    Primitive("gt?",arrow(tint,tint,tbool), _gt)    ,
    Primitive("is-prime",arrow(tint,tbool),_isPrime),
    Primitive("is-square",arrow(tint,tbool),_isSquare),
] + [ Primitive(str(j),tint,j) for j in range(10) ]