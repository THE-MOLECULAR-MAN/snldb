# An alternative form of the Saturday Night Live database

To use this database/dataset with a database teaching class I worked to align the tables with a more normalized form.

A `season` is a sequence of `episodes` which were broadcast. An `episode` is a sequence of `segments` in which `actors` participate. A single `actor` participating in a single `segment` is recorded as a row in `appearances`. 

`appearances` can be of a few different kinds. They can be an `actor` playing a `role`,

**Some of the data I excluded because I didn't quite understand it.  I think that some `appearances` might be an `impression`. I think that some (but not all) `segments` are of a particular kind, recorded as their `segments.catetory` (e.g., "Weekend Update") and some are `sketches` (e.g., ). I don't understand the relationship between `segments.category` and `sketches`.**

## Changes undertaken

I did four things:

1. Most of the work was removing denormalized foreign keys (e.g., titles included keys for the season of the episode from which they came).  Not everyone will like this, but it was appropriate for the class.

2. I also renamed some of the column headers to align with the conventions that I taught in the class. Specifically foreign keys are indicated by <table_name>_id (thus `episode_id` rather than `eid`. I made some column headers longer and more descriptive.

3. Since I found the label `titles` confusing (although I now realize it comes from snl itself), I renamed that to `segment`, referring to the parts of the episodes in which the appearances occurred.

4.  I removed what I think is "derived" data. This includes the `type` column in the actors.csv (which has values like `cast`). I think (and throw in an Issue or PR if this is wrong) that this is derived from the `capacity` column in the appearances.

The transformations are in [transform_to_normalized.ipynb](transform_to_normalized.ipynb).
