original_lines = File.readlines("part_2_test.txt")

def get_sum(lines)
  sum = 0
  lines.each do |line|
    nums = line.delete "^0-9"
    sum = sum + "#{nums[0]}#{nums[-1]}".to_i
  end
  sum
end

puts "Part 1: #{get_sum(original_lines)}"
