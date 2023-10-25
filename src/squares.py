#!/bin/env python
import cadquery as cq
import os


def main():
    large = make_square(0.0, 0.0, 0.0, 30.0)
    small = make_square(0.0, 0.0, 0.0, 15.0)

    difference = large.cut(small)

    assembly = (cq.Assembly()
        .add(small, color=cq.Color("red"))
        .add(difference, color=cq.Color("blue"))
    )

    os.makedirs("output", exist_ok=True)

    assembly.save(
        "output/squares.step",
        exportType=cq.exporters.ExportTypes.STEP,
        mode=cq.exporters.assembly.ExportModes.FUSED,
    )


def make_square(x: float, y: float, z: float, side: float) -> cq.Face:
    wp = cq.Workplane("XY", origin=(x, y, z))
    wire = wp.rect(side, side).val()
    face = cq.Face.makeFromWires(wire)
    return face


if __name__ == "__main__":
    main()
