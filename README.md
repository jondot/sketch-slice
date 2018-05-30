# Sketch Slice

An _opinionated_ design automation tool that turns Sketch files into assets for React Native apps.

## Quick Start

```
$ pip install sketch-slice
$ sketch-slice --help
Usage: sketch-slice [OPTIONS] SKETCHFILE

  Process SKETCHFILE into the destination folder. Set SKETCHTOOL_BIN env
  variable to sketchtool if not found.

Options:
  --prefix TEXT     Prefix for layers to filter.
  --output TEXT     Directory to output to. Defaults to same name as sketch
                    file.
  --dryrun BOOLEAN  If set, will simulate running.
  --help            Show this message and exit.
```

### Prepare your Sketch File Layout

Turn this:

```
artboard
  group1
    layer-1
    layer-2
  group2
    layer-3
  layer-4
```

With some simple naming rules (note the use of `ex-`), into this:

```
artboard
  group1
    ex-2-layer-1   (1)
    layer-2
  ex-1-group2      (2)
    layer-3
  group2
    ex-3-slice-1        (3)
    layer-3
  ex-0-layer-4
```

Use Sketch to assign your export formats and sizes before saving your sketch file.

Let's go over the highlighted artifacts above:

* (1) You can export a layer by adding a prefix `ex-2-` in this case. The number `2` is added to force ordering in the output file. Export names are lexicographically sorted.
* (2) You can export groups as well.
* (3) If there's a slice in a group, that slice will be taken representing the entire group (works for when Sketch glitches out and doesn't measure the real bounds of the group)

You can now run the tool like this:

```
$ sketch-slice garden.sketch --prefix ex- --output garden
```

This will use the `ex-` prefix, which is what we used above, and output a bundle to a folder named `garden`.

A bundle looks like this:

```
garden/
  [a bunch of images]
  layout.json
  index.js
```

And now you can import from React Native having the sliced image assets _and_ their layout information:

```javascript
import garden from './garden'
```

And `garden` will contain an array of 'parts' (a name that abstracts a Sketch layer, group, or slice) like this:

```javascript
{
    parts:[
        {
            key: 'ex-0-layer1',
            image: [React Native Image Asset],
            layout: {
                left: 14,
                top: 50,
                height: 200,
                width: 120
            }
        }
        ...
    ]
}
```

# Contributing

Fork, implement, add tests, pull request, get my everlasting thanks and a respectable place here :).

### Thanks:

To all [Contributors](https://github.com/jondot/sketch-slice/graphs/contributors) - you make this happen, thanks!

# Copyright

Copyright (c) 2018 [Dotan Nahum](http://gplus.to/dotan) [@jondot](http://twitter.com/jondot). See [LICENSE](LICENSE.txt) for further details.

```

```
