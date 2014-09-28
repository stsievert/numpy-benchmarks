from __future__ import division
from pylab import *
import sys
import timeit

MULTIPLIER = 1.0

def SVDTest():
    N = 1e3 * MULTIPLIER
    u, s, v = svd(randn(N,N))
def QRTest():
    N = 2e3 * MULTIPLIER
    q, r = qr(randn(N,N))
def InverseTest():
    N = 2e3 * MULTIPLIER
    A = randn(N,N)
    x = randn(N)
    sol = inv(A).dot(x)
def DeterminantTest():
    N = 3.0e3 * MULTIPLIER
    A = randn(N,N)
    d = det(A)
def NormTest():
    N = 5e3 * MULTIPLIER
    A = randn(N,N)
    n = norm(A)
def EigTest():
    N = 8e2 * MULTIPLIER
    e = eig(randn(N,N))
def DotTest():
    N = 2e3 * MULTIPLIER
    A = randn(N,N)
    B = randn(N,N)
    C = A.dot(B)
    

def RunBenchmarks():
    functions = ["SVDTest", "QRTest", "InverseTest", "DeterminantTest",
            "NormTest", "EigTest", "DotTest"]
    N = 3
    print "Running various test functions. Best of "+str(N)+" loops."
    for f in functions:
    #for f in ["DotTest"]:
        print "Running "+f+" . . . ",
        sys.stdout.flush()

        times = timeit.repeat(f+"()", "from __main__ import "+f, number=N)
        time = min(times)

        print "{0:.3f}s".format(time / N)

RunBenchmarks()
