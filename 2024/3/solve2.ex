#!/usr/bin/env elixir

content = File.read!("input")

pattern = ~r/(do|don't|mul)\((?:(\d{1,3}),(\d{1,3}))?\)/

defmodule Stuff do
  def do_thing(["do"], %{"acc" => acc}) do
    %{"enabled" => true, "acc" => acc}
  end
  def do_thing(["don't"], %{"acc" => acc}) do
    %{"enabled" => false, "acc" => acc}
  end
  def do_thing(["mul", n1, n2], %{"enabled" => enabled, "acc" => acc}) when enabled do
    %{"enabled" => true, "acc" => acc + String.to_integer(n1) * String.to_integer(n2)}
  end
  def do_thing(["mul", _n1, _n2], state) do
    state
  end
end
 
state = %{"enabled" => true, "acc" => 0}

pattern
  |> Regex.scan(content)
  |> Enum.map(&tl/1)
  |> Enum.reduce(state, fn match, acc -> Stuff.do_thing(match, acc) end)
  |> IO.inspect()