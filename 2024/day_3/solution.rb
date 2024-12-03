memory = File.read(ARGV[0])

def part_1(memory)
  # String#scan does the heavy lifting by using regular expression capturing.
  memory.scan(/mul\((\d{1,3}),(\d{1,3})\)/).map { |operands| operands[0].to_i * operands[1].to_i }.sum
end

p "Part 1: #{part_1 memory}"

def part_2(memory)
  fragments = memory.split("don't()")

  # Operation enabled at start, so we automatically include the first fragment
  operable_memory = fragments[0]
  fragments[1..-1].each do |fragment|
    # The first element of this array is always disabled because it immediately
    # follows a don't() instruction. If there's only one element, then the
    # entire fragment is disabled.
    fragment_parts = fragment.split("do()", 2)
    next if fragment_parts.size <= 1

    # We split on don't() originally, so everything after the first do() is operable
    operable_memory += fragment_parts[1]
  end

  # Now that we've reconstructed memory to only include operable statements, 
  # it can be processed just like part 1.
  part_1 operable_memory
end

p "Part 2: #{part_2 memory}"