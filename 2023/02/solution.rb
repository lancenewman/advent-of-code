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

def valid_selection?(handfull)
  handfull.all? do |dice|
    dice[:red] <= DICE_LIMITS[:red] && 
    dice[:green] <= DICE_LIMITS[:green] && 
    dice[:blue] <= DICE_LIMITS[:blue]
  end
end

def min_dice(dice)
  dice.each do |handfull|

  end
end

input = File.readlines("input.txt")
sum = 0
input.each do |line|
  game = get_game(line)
  handfulls = game.map { |handfull| get_dice(handfull) }
  puts handfulls
  if valid_selection?(handfulls)
    sum = sum + get_id(line)
  end
end
puts "Part 1: #{sum}"
