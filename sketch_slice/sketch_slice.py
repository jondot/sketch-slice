from toolz.curried import pipe, map, mapcat, filter, first, sorted
from jsonpath_ng.ext import parse
import json
import re
from glom import glom
from os import path


class IO:

    def write_file(self, to, content):
        pass

    def export_images(self, file, to):
        return ""

    def mkdir(self, to):
        pass

    def report(self, str):
        print(str)

    def headline(self, str):
        print(str)

    def get_data(self, file):
        pass


null_io = IO()


def fetch(content, prefix):
    return {
        "parts": pipe(
            parse("$..layers").find(content),
            mapcat(lambda m: m.value),
            filter(lambda v: v["exportOptions"]["exportFormats"]),
            filter(lambda v: re.match(prefix, v["name"])),
            map(
                lambda v: glom(
                    v,
                    {
                        "key": "name",
                        "layout": (
                            "frame",
                            {
                                "left": ("x", round),
                                "top": ("y", round),
                                "width": ("width", round),
                                "height": ("height", round),
                            },
                        ),
                    },
                )
            ),
            sorted(key=lambda p: p["key"]),
            list,
        )
    }


def index(layout_data):
    tmpl_all = """
import layout from './layout.json'

const parts = [
{parts}
].map((part, i) => ({{
  ...part,
  ...layout.parts[i]
}}))

export default {{ parts }}
"""
    parts = "\n".join(
        pipe(
            layout_data["parts"],
            map(
                lambda p: "  {{ image: require('./{key}.png') }},".format(key=p["key"])
            ),
            list,
        )
    )
    return tmpl_all.format(parts=parts)


def bundle(file, to, prefix, io=null_io):
    content = io.get_data(file)
    if not content:
        return

    layout_data = fetch(content, prefix)
    if not layout_data:
        return

    io.report("Writing: layout.json + index.js")
    io.write_file(path.join(to, "layout.json"), json.dumps(layout_data))
    io.write_file(path.join(to, "index.js"), index(layout_data))


def export(file, to, io=null_io):
    res = io.export_images(file, to)
    io.report(res)
