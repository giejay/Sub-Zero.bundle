# coding=utf-8

import logging
import sys
import codecs

from babelfish import Language

logger = logging.getLogger(__name__)

from subzero.modification import SubMod

fn = sys.argv[1]
debug = "--debug" in sys.argv

if debug:
    logging.basicConfig(level=logging.DEBUG)

submod = SubMod(debug=debug)
submod.load(fn, language=Language.fromietf("spa"), encoding="latin-1")
submod.modify("remove_HI", "OCR_fixes", "common", "shift_offset(s=20)")
#srt = submod.to_string("srt", "utf-8")
#f = codecs.open("testout.srt", "w+", encoding="utf-8")
#f.write(srt)
#f.close()
#print submod.f.to_string("srt")
#submod.modify("OCR_fixes")
#submod.modify("change_FPS(from=24,to=25)")
#submod.modify("common")

#print submod.f.to_string("srt")
