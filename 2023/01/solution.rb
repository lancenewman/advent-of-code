LINES = File.readlines("input.txt")

def part_1
  sum = 0
  LINES.each do |line|
    nums = line.delete "^0-9"
    sum = sum + "#{nums[0]}#{nums[-1]}".to_i
  end
  sum
end

puts "Part 1: #{part_1}"

NUMBER_HASH = {
  "zero" => 0,
  "one" => 1,
  "two" => 2,
  "three" => 3,
  "four" => 4,
  "five" => 5,
  "six" => 6,
  "seven" => 7,
  "eight" => 8,
  "nine" => 9,
}.freeze

def part_2
  regex = /(?=(\d|#{NUMBER_HASH.keys.join('|')}))/

  nums = LINES.map do |line|
    line.scan(regex).values_at(0, -1).flatten.map { |num| NUMBER_HASH[num] || num }.join.to_i
  end
  nums.sum
end

puts "Part 2: #{part_2}"