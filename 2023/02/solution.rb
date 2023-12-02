DICE_LIMITS = {
  red: 12,
  green: 13,
  blue: 14,
}

# Maybe don't need if games are always in order
def get_id(line)
  line.split(" ", 2).last.chomp(":").to_i
end

def get_handfulls(line)
  line.split(":", 2)[1].split(";")
end

def get_dice(handfull)
  res = {
    red: 0,
    green: 0,
    blue: 0,
  }

  handfull.split(",").each do |dice| 
    amount, color = dice.split
    res[color.to_sym] = amount.to_i
  end

  res
end

def valid_game?(dice)
  dice.all? do |handfull|
    handfull[:red] <= DICE_LIMITS[:red] && 
    handfull[:green] <= DICE_LIMITS[:green] && 
    handfull[:blue] <= DICE_LIMITS[:blue]
  end
end

input = File.readlines("input.txt")
sum = 0
input.each do |line|
  handfulls = get_handfulls(line)
  dice = handfulls.map { |handfull| get_dice(handfull) }
  puts dice
  if valid_game?(dice)
    sum = sum + get_id(line)
  end
end
puts "Part 1: #{sum}"
