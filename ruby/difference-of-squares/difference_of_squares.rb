class Squares
  attr_reader :numbers

  def initialize(n)
    @numbers = [*1..n]
  end

  def square_of_sum
    sum = numbers.reduce(&:+)
    sum * sum if sum
  end

  def sum_of_squares
    squares = numbers.map{ |n| n * n }
    squares.reduce(&:+)
  end

  def difference
    return 0 unless square_of_sum
    square_of_sum - sum_of_squares
  end
end

module BookKeeping
  VERSION = 3
end