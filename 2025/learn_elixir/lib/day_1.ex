defmodule LearnElixir.Day1 do

  def run_part_1(input) do
    result =
      input
      |> parse_input()
      |> calculate_zero_count()

    {:ok, result}
  end

  def run_part_2(_input) do
    IO.puts("TODO")
    {:ok, "TODO"}
  end

  defp parse_input(input) do
    input
    |> String.split("\n")
    |> Enum.map(&String.split_at(&1, 1))
  end

  defp calculate_zero_count(input) do
    IO.inspect(input)
    position = 0

    input
    |> Enum.reduce(0, fn {_direction, steps}, acc ->
      new_position = rotate_dial(position, steps)
      if new_position == 0 do
        _ = acc + 1
      end
      ^position = new_position
    end)
  end

  defp rotate_dial(position, steps) do
    rem(position + String.to_integer(steps), 99)
  end
end
