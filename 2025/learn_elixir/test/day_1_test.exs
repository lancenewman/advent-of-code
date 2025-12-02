defmodule LearnElixir.Day1Test do
  use ExUnit.Case
  alias LearnElixir.Day1

  describe "run/1" do
    test "returns the number of times the dial lands on zero" do
      input = Enum.join([
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82",
      ], "\n")

      assert {:ok, 3} = Day1.run_part_1(input)
    end
  end
end
