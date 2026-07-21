# Artful Deck Generator

Create web-native HTML presentation decks that feel designed rather than pasted together: clear narrative, concise human copy, art-directed imagery, stable 16:9 layouts, and visual QA.

## What it does

- Turns PDFs, notes, outlines, or existing slides into polished HTML decks.
- Shapes content into a teaching arc: pain point → core concepts → practical method → close.
- Requires a confirmed visible-language choice before writing slide copy.
- Uses one purposeful, slide-specific image per new slide and prevents generic repeated scenes.
- Supports Formal Business, Professional HR, AI and Technology, Mature Cartoon, and Painterly Human–AI Cooperation visual treatments.
- Checks layouts, image relevance, visual rhythm, and print/PDF output before delivery.

## Use it in Codex

Install this repository as a Codex skill, then invoke it in a task:

```
Use $artful-deck-generator to turn my source material into an artful, visually balanced web-native presentation.
```

The skill asks for a language and image style when they are not already specified.

## Included resources

- `scripts/quick_validate.py` — dependency-free validator for the skill definition.
- `references/image-art-reference.md` — image direction and crop guidance.
- `references/layout-variety-reference.md` — layout variety guidance for longer decks.
- `references/final-deck-audit.md` — delivery audit checklist.
- `references/style and layout/` — visual layout examples.
- `references/*.png` and `references/*.jpg` — selected treatment references.

## Validate

After editing the skill:

```powershell
python scripts/quick_validate.py .
```

## Design principles

- Build the narrative before the layout.
- Treat images as visual arguments, not decoration.
- Keep slide copy short, speakable, and language-consistent.
- Use large, deliberate image panels and avoid repeated silhouettes.
- Confirm every slide renders correctly before delivery.
