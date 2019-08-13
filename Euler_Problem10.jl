# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

module ProjectEuler

export genMultiples, eliminateMultiples, sumPrimes

function genMultiples(n::Int, lower::Int, upper::Int)
    multiples = n.*[x for x in lower+1:(ceil(upper/n))]
    return multiples
end

function eliminateMultiples(n::Int)
    factors = [x for x in 2.0:n-1]
    for i in 2:Int(ceil(sqrt(n)))
        multiples = genMultiples(i, 1, n)
        factors = setdiff(factors, multiples)
    end
    return factors
end

function sumPrimes(n::Int)
    primeFactors = eliminateMultiples(n)
    result = Int(reduce(+, primeFactors))
    println("The sum of primes below $n is: $result")
    return result 
end

@assert sumPrimes(10) == 17
@time sumPrimes(2000000)

end
