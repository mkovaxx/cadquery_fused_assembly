#!/bin/env python
import cadquery as cq
import os


def main():
    large = make_cylinder(0.0, 0.0, 0.0, 30.0, 30.0)
    small = make_cylinder(0.0, 0.0, 0.0, 15.0, 30.0)

    difference = large.cut(small)

    assembly = (cq.Assembly()
        .add(small, color=cq.Color("red"))
        .add(difference, color=cq.Color("blue"))
    )

    os.makedirs("output", exist_ok=True)

    assembly.save(
        "output/cylinders.step",
        exportType=cq.exporters.ExportTypes.STEP,
        mode=cq.exporters.assembly.ExportModes.FUSED,
    )


def make_cylinder(x: float, y: float, z: float, diameter: float, height: float) -> cq.Solid:
    wp = cq.Workplane("XY", origin=(x, y, z))
    solid = wp.circle(0.5 * diameter).extrude(height).val()
    return solid


if __name__ == "__main__":
    main()
