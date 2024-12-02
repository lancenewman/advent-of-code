LINES = File.readlines(ARGV[0])
reports = LINES.map { |report| report.split.map(&:to_i) }

# Part 1
def safe?(report)
  report.each_cons(3).all? { |a, b, c| ((a < b && b < c) || (a > b && b > c)) && ((a - b).abs <= 3 && (b - c).abs <= 3) }
end

p "Part 1: #{reports.map { |report| safe? report }.tally[true]}"

# Part 2
def safe_with_tolerance?(report)
  return true if safe? report
  
  report.size.times do |i|
    report_cpy = report.dup
    report_cpy.delete_at i
    return true if safe? report_cpy
  end
  false
end

p "Part 2: #{reports.map { |report| safe_with_tolerance? report }.tally[true]}"