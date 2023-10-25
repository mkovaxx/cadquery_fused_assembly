#!/bin/env python
import cadquery as cq
import os


def main():
    large = make_circle(0.0, 0.0, 0.0, 30.0)
    small = make_circle(0.0, 0.0, 0.0, 15.0)

    difference = large.cut(small)

    assembly = (cq.Assembly()
        .add(small, color=cq.Color("red"))
        .add(difference, color=cq.Color("blue"))
    )

    os.makedirs("output", exist_ok=True)

    assembly.save(
        "output/circles.step",
        exportType=cq.exporters.ExportTypes.STEP,
        mode=cq.exporters.assembly.ExportModes.FUSED,
    )


def make_circle(x: float, y: float, z: float, diameter: float) -> cq.Face:
    wp = cq.Workplane("XY", origin=(x, y, z))
    wire = wp.circle(0.5 * diameter).val()
    face = cq.Face.makeFromWires(wire)
    return face


if __name__ == "__main__":
    main()
