#!/bin/bash

# ---------------------------
# Fast Batch Simplify Flood Shapefiles (Skip makevalid)
# ---------------------------

ZIP_DIR="./data/flood"
OUT_DIR="./data/flood_clean"
TMP_DIR="/tmp/flood_work"

mkdir -p "$OUT_DIR"
mkdir -p "$TMP_DIR"

for zip in "$ZIP_DIR"/*.zip; do
  # Skip if not a file
  [ -f "$zip" ] || continue

  echo "===================================="
  echo "Processing: $(basename "$zip")"

  # Clear temp folder
  rm -rf "$TMP_DIR"/*

  # Extract ZIP for speed
  unzip -q "$zip" -d "$TMP_DIR"

  # Find first shapefile
  shp=$(find "$TMP_DIR" -name "*.shp" | head -n 1)

  if [ -z "$shp" ]; then
    echo "  ✗ No shapefile found - skipping"
    continue
  fi

  echo "  ✓ Found shapefile: $(basename "$shp")"

  name=$(basename "$shp" .shp)
  out="$OUT_DIR/${name}_clean.gpkg"

  # ---------------------------
  # Step 1: Reproject (degrees → meters)
  # ---------------------------
  echo "  Step 1: Reproject to EPSG:32651 (meters)"
  ogr2ogr \
    -nlt MULTIPOLYGON \
    "$TMP_DIR/proj.gpkg" \
    "$shp" \
    -t_srs EPSG:32651 \
    -progress

  # ---------------------------
  # Step 2: Simplify geometry
  # ---------------------------
  echo "  Step 2: Simplify geometry"
  ogr2ogr \
    -nlt MULTIPOLYGON \
    "$TMP_DIR/simple.gpkg" \
    "$TMP_DIR/proj.gpkg" \
    -simplify 1 \
    -progress

  # ---------------------------
  # Step 3: Save output (skip makevalid)
  # ---------------------------
  cp "$TMP_DIR/simple.gpkg" "$out"
  echo "  ✓ Saved output (simplified, not validated): $out"

  # Clean temp folder
  rm -rf "$TMP_DIR"/*
done

echo "===================================="
echo "✔ Done. All ZIP files processed."
