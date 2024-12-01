LINES = File.readlines(ARGV[0])

group_1 = []
group_2 = []
LINES.each do |line|
  id_1, id_2 = line.split.map(&:to_i)
  group_1 << id_1
  group_2 << id_2
end

p "part 1: #{ group_1.sort.zip(group_2.sort).map { |id_1, id_2| (id_1 - id_2).abs }.sum }"

similarity_score = 0
group_2_tally = group_2.tally
group_1.each do |id_1|
  similarity_score += group_2_tally[id_1].nil? ? 0 : id_1 * group_2_tally[id_1]
end

p "part 2: #{similarity_score}"