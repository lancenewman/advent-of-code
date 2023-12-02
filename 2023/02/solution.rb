# Processing hierarchy
# Line: "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
# Game: "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
# Handfull: "3 blue, 4 red"
# Dice: { red: 4, green: 0, blue; 3 }

DICE_LIMITS = {
  red: 12,
  green: 13,
  blue: 14,
}

# Maybe don't need if games are always in order
def get_id(line)
  line.split(" ", 2).last.chomp(":").to_i
end

def get_game(line)
  line.split(":", 2)[1].split(";")
end

def get_dice(game)
  res = {
    red: 0,
    green: 0,
    blue: 0,
  }

  game.split(",").each do |dice| 
    amount, color = dice.split
    res[color.to_sym] = amount.to_i
  end

  res
end

def valid_selection?(handfulls)
  handfulls.all? do |dice|
    dice[:red] <= DICE_LIMITS[:red] && 
    dice[:green] <= DICE_LIMITS[:green] && 
    dice[:blue] <= DICE_LIMITS[:blue]
  end
end

def get_min(handfulls, color)
  # The minimum dice required for a given color is the maximum pulled in any one handfull
  max = 0
  handfulls.each do |handfull|
    if handfull[color] > max
      max = handfull[color]
    end
  end
  max
end

def get_power(handfulls)
  get_min(handfulls, :red) * get_min(handfulls, :green) * get_min(handfulls, :blue)
end

input = File.readlines("input.txt")
id_sum = 0
power_sum = 0

input.each do |line|
  game = get_game(line)
  handfulls = game.map { |handfull| get_dice(handfull) }

  # Part 1
  if valid_selection?(handfulls)
    id_sum = id_sum + get_id(line)
  end
  
  # Part 2
  power_sum = power_sum + get_power(handfulls)
end

puts "Part 1: #{id_sum}"
puts "Part 2: #{power_sum}"
