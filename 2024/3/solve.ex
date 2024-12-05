content = File.read!("input")

pattern = ~r/mul\((\d{1,3}),(\d{1,3})\)/

pattern
  |> Regex.scan(content)
  |> Enum.map(&tl/1)
  |> Enum.map(fn [a, b] -> String.to_integer(a) * String.to_integer(b) end)
  |> Enum.sum()
  |> IO.inspect()
  