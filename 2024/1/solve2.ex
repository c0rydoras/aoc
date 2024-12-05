content = File.read!("input")

nums = content
  |> String.split()
  |> Enum.map(&String.to_integer/1)

list1 = nums
  |> Enum.take_every(2)

freq_map = nums
  |> tl
  |> Enum.take_every(2)
  |> Enum.frequencies()

list1
  |> Enum.reduce(0, fn n, acc -> acc + n * Map.get(freq_map, n, 0) end)
  |> IO.inspect()