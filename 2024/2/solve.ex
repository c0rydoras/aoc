content = File.read!("input")

defmodule Stuff do
  def is_bad({i1, i2}) do
    diff = i1 - i2
    diff == 0 or abs(diff) > 3
  end

  def is_good(line) when length(line) == 0 do false end

  def is_good(line) do
    contains_invalid_things = line
        |> Enum.zip(tl(line))
        |> Enum.map(&Stuff.is_bad()/1)
        |> Enum.any?()

    if contains_invalid_things do
      false
    else
      (Enum.sort(line) == line or Enum.sort(line, :desc) == line)
    end
  end
end

lines = content
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
