#MenuTitle: New Tab with Nested Components
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals
__doc__="""
Opens a new Edit tab with glyphs that contain components made of components.
"""

thisFont = Glyphs.font
txt = ""

for thisGlyph in thisFont.glyphs:
	firstLayer = thisGlyph.layers[0]
	for thisComponent in firstLayer.components:
		otherGlyph = thisFont.glyphs[thisComponent.name]
		if otherGlyph.layers[0].components:
			txt += thisGlyph.string
			break

if txt:
	Glyphs.font.newTab(txt)
else:
	Message(
		title="New Tab with Nested Components",
		message="There are no components of components in this font.",
		OKButton="OK",
	)