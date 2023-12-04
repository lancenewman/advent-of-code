INPUT = File.readlines("input.txt")

def parse
  cards = {}
  INPUT.each do |line|
    card, numbers = line.split(":", 2)
    winning_numbers, my_numbers = numbers.split("|", 2)
    cards[card.split[1].to_i] = { 
      winning: winning_numbers.split.map(&:to_i), 
      mine: my_numbers.split.map(&:to_i) 
    }
  end
  cards
end

def part_1
  parse.sum do |_, numbers|
    matches = numbers[:winning] & numbers[:mine]
    matches.size > 0 ? 1 * ( 2 ** ((matches.size - 1))) : 0
  end
end

def part_2
  # Start with one copy of every card
  copy_counts = Array.new(INPUT.size, 1)
  
  parse.each_with_index do |(card, numbers), i|
    # Find out if there are any matching numbers
    matches = numbers[:winning] & numbers[:mine]

    if matches.size > 0
      last_card = i + matches.size > INPUT.size ? INPUT.size : i + matches.size
      ((i + 1)..last_card).each { |j| copy_counts[j] += (1 * copy_counts[i]) }
    end
  end
  copy_counts.sum
end

puts "Part 1: #{part_1}"
puts "Part 2: #{part_2}"