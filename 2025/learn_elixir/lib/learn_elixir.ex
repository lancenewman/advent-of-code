defmodule LearnElixir do
  @moduledoc """
  Documentation for `LearnElixir`.
  """

  @spec run(non_neg_integer()) :: {:ok, any()} | {:error, any()}
  def run(day) do
    solution_module = String.to_existing_atom("Elixir.LearnElixir.Day#{day}")

    input =
      day
      |> input_file()
      |> File.read!()

    IO.puts("Running day #{day} part 1")
    solution_module.run_part_1(input)
    IO.puts("Running day #{day} part 2")
    solution_module.run_part_2(input)
  rescue
    error -> {:error, error}
  end

  defp input_file(day), do: "#{File.cwd!()}/lib/inputs/day_#{day}"
end
