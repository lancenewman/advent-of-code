defmodule LearnElixirTest do
  use ExUnit.Case
  doctest LearnElixir

  alias LearnElixir

  describe "run/1" do
    test "runs solution of the provided day" do
      assert {:ok, _} = LearnElixir.run(1)
    end

    test "returns error when solution fail or is not found" do
      assert {:error, _} = LearnElixir.run(100)
    end
  end
end
