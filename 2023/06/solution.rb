INPUT = File.readlines("input.txt")

class Race
  def initialize(time, target_distance)
    @time = time
    @target_distance = target_distance
  end

  def num_possible_wins
    wins = 0
    @time.times do |charge_time|
      remaining_time = @time - charge_time
      if charge_time * remaining_time  > @target_distance
        wins += 1
      end
    end
    wins
  end
end

def part_1
  times = INPUT[0].split.slice(1, INPUT[0].size).map(&:to_i)
  distances = INPUT[1].split.slice(1, INPUT[1].size).map(&:to_i)
  races = []
  times.zip(distances) { |time, distance| races << Race.new(time, distance) }
  races
end

def part_2
  time = INPUT[0].split.slice(1, INPUT[0].size).join.to_i
  distance = INPUT[1].split.slice(1, INPUT[1].size).join.to_i
  Race.new(time, distance)
end

puts "Part 1: #{ part_1.reduce(1) { |product, race| product * race.num_possible_wins} }"
puts "Part 2: #{ part_2.num_possible_wins }"