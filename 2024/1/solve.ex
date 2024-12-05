content = File.read!("input")

nums = content
  |> String.split()
  |> Enum.map(&String.to_integer/1)

line1 = nums
  |> Enum.take_every(2)
  |> Enum.sort()

line2 = nums
  |> tl
  |> Enum.take_every(2)
  |> Enum.sort()

Enum.zip_with(line1, line2, &(&1 - &2))
  |> Enum.map(&abs/1)
  |> Enum.sum()
  |> IO.inspect()