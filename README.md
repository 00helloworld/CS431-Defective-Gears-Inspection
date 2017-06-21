# CS431-Defective-Gears-Processing

### Introduction


Binary morphology can be used to perform very specific inspection tasks in industrial machine vision. Sternberg (1985) showed how a watch gear could be inspected to check whether it had any missing or broken teeth.

This code repeat Sternberg's expirement.

### Structural elements


* **hole ring**: a ring of pixels whose diameter is slightly larger than the diameters of the
four holes in the watch gears. It its just around these holes and can be used to mark
a few pixels at their centers.
* **hole mask**: an octagon that is slightly larger than the holes in the watch gears.
* **gear body**: a disk structuring element that is as big as the gear minus its teeth.
* **sampling ring spacer**: a disk structuring element that is used to move slightly
outward from the gear body
* **sampling ring width**: a disk structuring element that is used to dilate outward to
the tips of the teeth.
* **tip spacing**: a disk structuring element whose diameter spans the tip-to-tip space
between teeth.
* **defect cue**: a disk structuring element whose purpose is to dilate defects in order to
show them to the user.


The best result for the given image was achive with next parameters:
* hole_ring = 97
* hole_mask = hole_ring. Here we use circles instead of octagon
* gear_body = 280
* sampling ring spacer = 11
* sampling ring width = 22
* tip spacing = 25
* defect cue = 35

You can find all illustrations and steps on the reference below (p. 19)

### References


[Binary Image Analysis, chapter 3](https://courses.cs.washington.edu/courses/cse576/book/ch3.pdf)
