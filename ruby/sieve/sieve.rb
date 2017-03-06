class Sieve
  def initialize(number)
    @number = number
  end

  def primes
    primes = [*2..@number]
    composites = []

    [*2..@number].each do |n|
      next if composites.include? n

      [*(n + 1)..@number].each do |num|
        if num % n == 0 && primes.include?(num)
          primes.delete(num)
          composites.push(num)
        end
      end
    end

    primes.sort()
  end
end

module BookKeeping
  VERSION = 1 
end