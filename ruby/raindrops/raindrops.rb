class Raindrops
  def self.convert(num)
    factors = [*1..num].select { |f| (num.to_i % f) == 0 }
    raindrops = ''

    raindrops += 'Pling' if factors.include? 3
    raindrops += 'Plang' if factors.include? 5
    raindrops += 'Plong' if factors.include? 7
    raindrops = num.to_s if raindrops.empty?

    raindrops
  end
end

module BookKeeping
  VERSION = 3
end