import wavedrom
svg = wavedrom.render("""
{ head:{text:'Topic 13 Question 1'},
signal:
[
{name: "a", wave: "1.0...1..01..0......"},{name: "b", wave: "1.01.0............1."},{name: "c", wave: "1......01.......0..."},{name: "ab", wave: ''},{name: "f", wave: ''},],
  foot:{"tock":1}
}""")
svg.saveas("demo1.svg")