content = File.read!("input")

# GPT code
defmodule Combinations do
  def combinations(_, 0), do: [[]]
  def combinations([], _), do: []

  def combinations([head | tail], size) do
    for(comb <- combinations(tail, size - 1), do: [head | comb]) ++
      combinations(tail, size)
  end

  def all_but_one(list) do
    size = length(list) - 1
    combinations(list, size)
  end
end

defmodule Stuff do
  def is_bad({i1, i2}) do
    diff = i1 - i2
    diff == 0 or abs(diff) > 3
  end

  def _is_good(line) do
    contains_invalid_things =
      line
      |> Enum.zip(tl(line))
      |> Enum.map(&Stuff.is_bad/1)
      |> Enum.any?()

    if contains_invalid_things do
      false
    else
      Enum.sort(line) == line or Enum.sort(line, :desc) == line
    end
  end

  def is_good(line) when length(line) == 0 do
    false
  end

  def is_good(line) do
    line
    |> Combinations.all_but_one()
    |> Enum.map(&_is_good/1)
    |> Enum.any?()
  end
end

lines =
  content
  |> String.split("\n")
  |> Enum.map(fn line ->
    line
    |> String.split()
    |> Enum.map(&String.to_integer/1)
  end)

lines
|> Enum.filter(&Stuff.is_good/1)
|> Enum.count()
|> IO.inspect()
