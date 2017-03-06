class Complement
  def self.of_dna(dna_strand)
    dna_to_rna = {
      'G' => 'C',
      'C' => 'G',
      'T' => 'A',
      'A' => 'U'
    }

    rna = dna_strand.chars.map do |nuc|
      dna_to_rna[nuc] ? dna_to_rna[nuc] : break
    end

    rna ? rna.join('') : ''
  end
end

module BookKeeping
  VERSION = 4
end
