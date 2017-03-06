class Hamming
  class << self
    def compute(str1, str2)
      raise ArgumentError if str1.length != str2.length

      str1.chars.each_index.reduce(0) do |sum, i| 
        str1[i] == str2[i] ? sum : sum + 1
      end 
    end
  end
end

module BookKeeping
  VERSION = 3
end

