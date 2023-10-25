#!/bin/env python
import cadquery as cq
import os


def main():
    large = make_box(0.0, 0.0, 0.0, 30.0, 30.0)
    small = make_box(0.0, 0.0, 0.0, 15.0, 30.0)

    difference = large.cut(small)

    assembly = (cq.Assembly()
        .add(small, color=cq.Color("red"))
        .add(difference, color=cq.Color("blue"))
    )

    os.makedirs("output", exist_ok=True)

    assembly.save(
        "output/boxes.step",
        exportType=cq.exporters.ExportTypes.STEP,
        mode=cq.exporters.assembly.ExportModes.FUSED,
    )


def make_box(x: float, y: float, z: float, side: float, height: float) -> cq.Solid:
    wp = cq.Workplane("XY", origin=(x, y, z))
    solid = wp.rect(side, side).extrude(height).val()
    return solid


if __name__ == "__main__":
    main()
