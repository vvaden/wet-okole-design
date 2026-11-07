# Project state — November 6, 2026 (Pacific/Honolulu)

## Selected direction
User selected Gray Hibiscus seat center panels (seatback AND seat cushion), black wings/bolsters, gray piping, and solid charcoal headrest fronts visually matching the dark ground of the Gray Hibiscus print. Full-color French bulldog artwork is screenprinted onto neoprene and sewn on. Truck exterior is Toyota Tacoma Mud Bath. Preserve the existing full idea-board layout, truck image, fabric detail, piping detail, and material labels.

## Authoritative files
- assets/original-color-emblem.png: untouched supplied full-color artwork. Brindle/dark dog on left, fawn/light dog on right. This supersedes the earlier monochrome emblems.
- current/approved-charcoal-board.png: user explicitly chose this design, then requested an ear/border tweak.
- current/latest-outer-circle-board.png and current/latest-outer-circle-emblem.png: latest delivered revision, not yet explicitly approved after delivery. User authorized enlarging the circular border to contain the dark dog's protruding ear while preserving the artwork. Implementation ADDED an outer gold circle and cream margin; original gold ring remains as an inner accent. Do not say the original ring was replaced. Artwork appears smaller inside the same patch placement because of the expanded border.
- assets/blank-charcoal-board.png: covers ordered without graphics.
- assets/blank-charcoal-seats.png: clean 848x905 scene for deterministic compositing.
- assets/original-contour-patch.png: original full-color art with external cream removed and narrow cream edge, before enlarged circle.

## Preservation rules
Never regenerate/redraw the emblem merely to change color or placement. Preserve dog expressions, ears, eyes, eyebrows, coat contrast, flowers and scenery. No simulated embroidery. Earlier iterations repeatedly changed details; user strongly objects. Keep original files and compare changes. Physical printing may need maker preparation; this board is a visual concept, not a confirmed production specification.

## Manufacturer/installer context from user screenshots
Local representative: Auto Trends Maui. Factory reportedly declined headrest graphics because of adhesive durability concerns. Representative has previously had a customer screenprint neoprene before she sewed custom covers. For this user's project she described ordering unprinted Wet Okole covers, providing black neoprene to a screenprinter, then replacing the factory headrest front panel with the printed panel. Latest requested mockup instead depicts a separate emblem-shaped sewn-on piece on a gray/charcoal headrest. These are different constructions; do not imply the rep has confirmed the pictured patch construction. User accepts replaceability and does not want repeated durability warnings. Representative also said actual fourth-generation Tacoma cover layout differs from mockup. Confirm dimensions/panel construction with her when production is discussed.

## Color history
User rejected invented or unverified manufacturer color names. 'Warm taupe' was a concept, not a verified offering; a previous 'Island Mocha 57' label was unreliable. Current charcoal is visually sampled from the mockup (about RGB 37,38,44), not a verified Wet Okole solid-color SKU. Gray Hibiscus was labeled 215 in prior work. Do not introduce color SKU claims without checking official sources. No further brown/red alternatives requested.

## Migration
User wants all future work in Cloud accessible from iPhone, without Mac dependency. This package carries the working state and a summary, NOT the original chat transcript or its ID. A separate full local archive preserves earlier files/scripts, including obsolete iterations. Use this curated package for continuation.

## Tools
Python 3 with Pillow and numpy. scripts/render_board.py composes the latest emblem onto the blank charcoal board while retaining existing text/layout. No font installation or Mac paths are needed. scripts/verify_package.py verifies transferred files against SHA-256 manifest. Existing delivered PNGs are authoritative; re-rendering is a smoke test, not an invitation to redesign.
