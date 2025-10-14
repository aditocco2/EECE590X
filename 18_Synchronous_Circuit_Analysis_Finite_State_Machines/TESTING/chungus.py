import schemdraw as d
import schemdraw.elements as elm

with d.Drawing() as d:
    # Add an element to establish a starting position
    C = d.add(elm.Capacitor())
    # Add a line that extends horizontally to close the loop
    d.add(elm.Line().tox(C.start))