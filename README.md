# coolest-art-01

A colossal whale built from cathedral stained glass, swimming through a storm of gold dust. Dramatic backlighting and a deep indigo-and-amber palette give it the weight of a religious painting.

## AI prompt used

```
a colossal whale made of cathedral stained glass swimming through a storm of gold dust,
dramatic backlight, deep indigo and amber palette, ultra detailed digital painting
```

Model: flux via image.pollinations.ai, 768x768, seed 13.
Post: bottom strip cropped to remove the generator watermark (768x660).

## How to run

```
python3 main.py
```

Copies `entry.png` from this repository into the output directory.

The output directory defaults to `/output` and can be overridden:

```
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## Note on the artwork

The image was created with an AI image model using the prompt above. The prompt
was authored and directed by the human submitter; the model only rendered it.
No manual repainting or compositing was applied beyond cropping the generator
watermark off the bottom edge.

## License

MIT — see `LICENSE`.
