from kikit.units import *
from pcbnew import FootprintLoad

def kikitPostprocess(panel, args):
    tl, tr, bl, br = panel.panelCorners(2.5 * mm, 2.5 * mm)
    for pos in [tl, tr, bl]:
        footprint = FootprintLoad('FUSB301.pretty', 'JLC_Tooling_Hole')
        footprint.SetPosition(pos)
        panel.board.Add(footprint)
