# check for each letter of alphabet. Use regex?

class Pangram
  class << self
    def pangram?(phrase)
      return if phrase == ''

      phrase = phrase.downcase.gsub(/[^a-z]/, '')
      phrase.chars.map(&:ord).sort.uniq.map(&:chr) == [*'a'..'z']
    end
  end
end

module BookKeeping
  VERSION = 4
end