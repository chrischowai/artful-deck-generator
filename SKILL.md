---
name: artful-deck-generator
description: Create artful, visually balanced presentation html decks from PDFs, notes, outlines, or existing HTML slides. Use when the user asks to generate or improve a PPT/keynote-style deck with strong narrative structure, bilingual or polished copy, mandatory GenImage/art-directed imagery, web-native slides, PDF export, or visual QA for overlap, blank space, weak composition, and print/export correctness.
---

# Artful Deck Generator

## Outcome

Produce a html presentation deck that feels designed, not pasted together: clear argument, human copy, content-first image direction, stable 16:9 layout, browser QA, and a correct PDF/export path.

## Bundled Resources

- `scripts/quick_validate.py`: run after editing this skill. It validates frontmatter, required deck guardrails, and the reference image without requiring PyYAML.
- `references/image-art-reference.md`: read before image-heavy deck work when the expected generated-art quality or crop behavior is ambiguous.
- `references/layout-variety-reference.md`: read before building decks over 20 slides, or whenever the screenshot/contact-sheet pass suggests repeated slide silhouettes.
- `references/style and layout/`: visual examples for layout families and pacing. Inspect this folder together with `references/layout-variety-reference.md`; borrow structure, not content.
- `references/final-deck-audit.md`: read before final delivery. Use its subagent prompt and pass/fail checklist for final deck audit, mandatory for decks over 20 slides.
- `references/complete-slide-art-reference.jpg`: local visual reference for complete, non-cropped, one-slide 16:9 generated art.
- `references/formal-business-reference.png`: selected reference for the Formal Business deck-image style.
- `references/professional-hr-reference.png`: selected reference for the Professional HR deck-image style.
- `references/ai-technology-reference.png`: selected reference for the AI and Technology deck-image style.
- `references/mature-cartoon-reference.png`: selected reference for the Mature Cartoon deck-image style.

## Workflow

1. Read the source before outlining.
   - For PDFs, extract text and identify the real argument, not the chapter order.
   - For existing decks, inspect the actual HTML/CSS/screenshots before editing.
   - Before outlining, drafting copy, or building a deck, confirm the language. If the user already explicitly chose a language, treat it as confirmed; otherwise, present exactly these choices and wait for the answer:
     1. English
     2. Traditional Chinese
     3. Bilingual (English + Traditional Chinese)
     4. Other: please specify
   - Never infer bilingual output or a default language. For "Other," confirm the exact language or language combination before continuing.
   - State assumptions when the desired density or output format is ambiguous.

2. Review and condense the teaching flow before building.
   - Write a one-screen flow summary first: audience, time box, learning outcome, narrative arc, and slide count.
   - Prefer a tight teaching sequence: why verification matters -> failure modes -> verification routine -> risk/governance -> practice -> close.
   - Merge repeated ideas, delete decorative slides, and make every slide answer "what should the learner do differently?"

3. Compress the structure.
   - Build a narrative arc: pain point -> core concepts -> practical method -> human/philosophical close.
   - Must respective user request number of deck first. If user said generate 50 slides, please respect and generate 50 slides. 
   - If user don't mentioned the number of slides to be generated. Keep most decks to 15-20 slides unless the content truly needs more.
   - For decks over 20 slides, read `references/layout-variety-reference.md` and inspect every screenshot in `references/style and layout/` before coding. Take the full reference set as the layout palette, but borrow structure rather than copying content.
   - For decks over 20 slides, create a visible slide-format plan before implementation with: slide number, slide purpose, layout family, density, image placement, interaction type, and reference inspiration. Use it to rotate layout families, density, image placement, and interaction type across the deck.
   - Assign each slide a layout type before writing code: title, statement, two-column image, comparison, framework grid, pipeline, quote, closing.
   - Do not let more than two adjacent slides use the same layout family in a large deck unless it is an intentional repeated motif.
   - Do not deliver fewer than 15 slides for a teaching deck unless the user explicitly asks for a shorter micro-deck or the source is too small.

4. Humanize the copy.
   - Use short, speakable lines.
   - Remove lecture tone, filler transitions, generic AI phrasing, and long explanatory paragraphs.
   - Use only the confirmed language selection in visible slide copy. Do not add a second language for decoration or presumed audience fit.
   - For bilingual decks, make English primary and Traditional Chinese supporting unless the user specifies the reverse; do not let both compete at equal weight.
   - Put the confirmed language(s) on every slide: title or subtitle, key points, and any closing takeaway. Speaker notes may be primary-language only unless the user asks otherwise.

5. Art-direct images.
   - If unsure what "complete generated slide art" should look like, read `references/image-art-reference.md` and inspect `references/complete-slide-art-reference.jpg`.
   - GenImage is mandatory for new deck imagery. Always generate or select one purposeful image per slide for every new deck, whether or not the user explicitly asks for image-rich slides.
   - Lock three independent decisions for every image: **message** (what the slide teaches), **subject** (the concrete scene, object, system, or metaphor that communicates it), and **treatment** (the chosen style's medium, palette, light, texture, framing, and mood). Decide them in that order.
   - **Style reference controls treatment, never the subject.** Do not inherit its people, room, meeting, workshop, desk, lab, dashboard, or story unless the slide itself needs that exact subject.
   - Before calling GenImage, write a slide-by-slide image brief with this shape: `Slide claim -> semantic role -> natural subject/metaphor -> style treatment -> must avoid`. Use semantic roles such as human action, decision, contrast, process, system, evidence, consequence, or reflection to choose the image; do not start from the reference image's scene.
   - Put the slide-specific subject first in every prompt and the style treatment after it. Include a negative constraint that rejects the reference scene whenever it is not relevant, for example: `not a workshop, meeting, conference room, presentation, or group gathered around a screen`.
   - Run a content relevance gate before generation: for each image, state in one sentence how a viewer can infer the slide's key idea from the image alone. If that sentence only says it "matches the HR/technology/business style," replace the subject or metaphor.
   - Run a scene-diversity pass across the full brief. Meeting, workshop, presentation, office-review, or dashboard scenes need a slide-specific reason; they are never the default for a selected style. Reject repeated scene families that differ only by people, camera angle, or props.
   - Use prompts that describe the slide-specific subject, mood, medium, composition, and constraints.
   - Before generating slide images, ask the user to choose one image style unless they already specified it. Do not build the deck before the style is chosen or clearly inferred from the user's request.
   - Style menu:
     - Formal Business: premium executive treatment: polished editorial photography, charcoal/navy/walnut/off-white palette, subtle gold, precise lighting, formal composition, high-trust materials, and measured seriousness. Use `references/formal-business-reference.png` for treatment only.
     - Professional HR: warm, human-centered treatment: natural light, wood and soft-gray materials, muted teal/coral/sage/navy/off-white palette, inclusive and credible emotional tone. Use `references/professional-hr-reference.png` for treatment only.
     - AI and Technology: credible technical treatment: graphite/black-blue palette, secure and legible technical cues, subtle cyan light, restrained red-orange risk accents, serious non-fantasy finish. Use `references/ai-technology-reference.png` for treatment only.
     - Mature Cartoon: sophisticated editorial treatment: adult graphic-novel linework, subtle paper texture, muted teal/warm gray/graphite/cream palette, restrained coral accents, expressive but not childish. Use `references/mature-cartoon-reference.png` for treatment only.
     - Painterly Human-AI Cooperation: warm editorial watercolor or paper-collage treatment, artistic and not too sci-fi. Do not default to a literal human-AI conversation; use `references/complete-slide-art-reference.jpg` for treatment only.
   - Do not overfit to the style reference's depicted subject. A deck may need a prompt blueprint, verification gate, decision fork, policy object, coaching moment, process loop, abstract system map, evidence object, or decision metaphor; keep the selected treatment while changing the subject to match the slide.
   - Treat images as layout drivers, not decoration added after text.
   - For generated deck art, prefer one individually generated 16:9 image per slide. Do not use a multi-panel contact sheet and then evenly crop it into slide art; it often cuts subjects at the wrong edges.
   - If reusing a larger generated image, crop manually by visual inspection for each slide and save the selected crop as its own asset. Never assume equal grid slicing is correct.
   - Prompt every image with full-composition constraints: "complete scene visible, generous margins, no cropped heads/hands/objects, no readable text, no logos, no watermark."
   - Save every project-used image into the deck workspace. Do not leave referenced images only in a generated-image cache or temp folder.
   - Before delivery, confirm `generated_or_selected_image_count == slide_count`, unless the user explicitly approved placeholders or fewer images.
   - Do not silently replace GenImage with CSS placeholders, stock-like decoration, or repeated generic images. Use placeholders only when the user explicitly asks for them or GenImage is unavailable and the user approves the compromise.

6. Build web-native slides.
   - Use a fixed 1920x1080 stage scaled to the viewport.
   - Keep slide UI zero-dependency unless the project already uses a stack.
   - Use explicit layout zones. Never let important text and image occupy the same zone.
   - Use large image panels or art cards with real dimensions; avoid tiny corner images unless intentionally editorial.
   - Keep cards at 8px radius or less; avoid nested cards.
   - Match image container aspect ratio to image asset aspect ratio whenever possible. A 16:9 generated image should sit in a 16:9 panel; avoid tall containers that make landscape images look unfinished.
   - Use `object-fit: cover` only when the container and asset share the same aspect ratio or the crop has been visually approved. Use `object-fit: contain` only when letterboxing is intentional and acceptable.

7. Design the bottom controls.
   - Use a compact capsule control for Prev, slide count, Next, keyboard hints, and optional PDF export.
   - Hide deck controls in print/PDF.
   - If adding a PDF button, prefer `window.print()` for user export and also generate a verified PDF artifact when requested.

## Visual QA Checklist

Run browser checks before delivery:

- All slides stay 16:9 and fit without body overflow.
- Every slide has its intended image loaded.
- Every slide image matches that slide's core idea; do not accept a set of images that merely share the chosen style but repeat the same generic scene.
- Apply the content relevance gate to the rendered images: a reviewer should be able to name the slide's key idea and the image's visual link without relying on the title. Reject images whose only rationale is style consistency.
- Apply the scene-diversity pass to the rendered deck: reject multiple meeting, workshop, presentation, office-review, or dashboard scenes unless each is directly justified by its slide's message.
- Every slide's image looks complete in the rendered slide, not merely loaded. Inspect screenshots for cut-off subjects, wrong crop, accidental blank space inside image panels, and mismatched aspect ratios.
- Text boxes and image panels do not overlap.
- No slide places all content in the top half while leaving the bottom empty unless it is a deliberate statement slide.
- Logic pages use readable structures: 2x2 grids, pipelines, stacks, or simple left-right comparisons.
- Closing slides put final copy in the upper/middle reading zone; avoid loose support text floating over the headline.
- Navigation controls work and do not cover important content.
- Create a contact sheet or equivalent all-slide overview from browser screenshots for decks over 10 slides. Review it manually before delivery.
- For decks over 20 slides, check the contact sheet for visual rhythm and repeated silhouettes: same title position, same image box, same three-card row, same text density, same image placement, same interaction type, or same diagram pattern appearing too often.
- Verify the confirmed language(s) render correctly. When Traditional Chinese is selected, check for mojibake markers such as ` `, `Ã`, or `Â`.

Do not treat automated checks as sufficient. A deck is not ready until at least one human visual pass over all slides has happened.

## PDF Export Rule

Print/PDF export must force animated content visible:

```css
@media print {
  @page { size: 1920px 1080px; margin: 0; }
  .slide {
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
    break-after: page;
  }
  .reveal {
    opacity: 1 !important;
    transform: none !important;
    filter: none !important;
    transition: none !important;
  }
  .deck-controls { display: none !important; }
}
```

Verify more than page count. Check that every PDF page has visible content, not only the slide that was active when export was triggered.

## Delivery Gate

Before final response:

- Re-open or screenshot the current deck after the last edit, not before.
- Confirm slide count, loaded image count, and PDF page count.
- Confirm `generated_or_selected_image_count == slide_count`, unless the user explicitly approved placeholders or fewer images.
- For decks over 20 slides, confirm the layout-variety reference was read, every `references/style and layout/` screenshot was inspected, and the slide-format plan was followed.
- Read `references/final-deck-audit.md` and delegate and deploy a subagent final audit before handing the final deck to the user. Fix audit failures, or clearly report any unresolved blocker and compromise.
- Summarize the flow in one short line so the user can see the teaching arc.
- Remove temporary QA screenshots, crop sheets, and helper files. Keep only final assets used by the deck.
- If a simplification was used, state its ceiling. Do not hide compromises such as reused image assets, placeholder art, or skipped visual checks.

## Common Failure Fixes

- Double image/blur overlap: remove duplicate pseudo-background layers; keep one real image surface.
- Upper-content cluster with empty bottom: redesign into a two-zone composition with image and content occupying the middle band.
- Disconnected logic lines: replace decorative connectors with a pipeline, numbered stack, or 2x2 matrix.
- Closing slide overlap: move support copy into the quote flow or a separated thought block.
- Incomplete or wrongly cropped images: replace contact-sheet/even-grid crops with per-slide generated images or manually inspected crops; then match the slide image panel to the asset aspect ratio.
- Style-subject overfit: rewrite prompts so the style reference supplies look and feel only, then regenerate each slide from its actual message and visual metaphor.
- Blank PDF pages: print CSS is hiding animation reveals; force `.reveal` visible in `@media print`.
