#!/bin/env python
import cadquery as cq
import os


def main():
    diameter_outer = 30.0
    diameter_inner = 15.0
    height = 30.0

    disk_outer_1 = make_disk(0.0, 0.0, 0.0, diameter_outer)
    disk_inner_1 = make_disk(0.0, 0.0, 0.0, diameter_inner)
    ring_1 = disk_outer_1.cut(disk_inner_1)

    disk_outer_2 = make_disk(0.0, 0.0, height, diameter_outer)
    disk_inner_2 = make_disk(0.0, 0.0, height, diameter_inner)
    ring_2 = disk_outer_2.cut(disk_inner_2)

    tube_outer = make_tube(0.0, 0.0, 0.0, diameter_outer, height)
    tube_inner = make_tube(0.0, 0.0, 0.0, diameter_inner, height)

    assembly = (cq.Assembly()
        .add(ring_1, color=cq.Color("red"))
        .add(tube_outer, color=cq.Color("green"))
        .add(ring_2, color=cq.Color("blue"))
        .add(disk_inner_1, color=cq.Color("cyan"))
        .add(tube_inner, color=cq.Color("magenta"))
        .add(disk_inner_2, color=cq.Color("yellow"))
    )

    os.makedirs("output", exist_ok=True)

    assembly.save(
        "output/tubes.step",
        exportType=cq.exporters.ExportTypes.STEP,
        mode=cq.exporters.assembly.ExportModes.FUSED,
    )


def make_disk(x: float, y: float, z: float, diameter: float) -> cq.Face:
    wp = cq.Workplane("XY", origin=(x, y, z))
    wire = wp.circle(0.5 * diameter).val()
    face = cq.Face.makeFromWires(wire)
    return face


def make_tube(x: float, y: float, z: float, diameter: float, height: float) -> cq.Shell:
    path = cq.Workplane("XZ").polyline([(x, z), (x, z + height)])
    wp = cq.Workplane("XY", origin=(x, y, z))
    shell = (wp
        .circle(0.5 * diameter)
        .sweep(path, makeSolid=False)
        .val()
    )
    return shell


if __name__ == "__main__":
    main()
