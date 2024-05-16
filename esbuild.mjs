#!/usr/bin/env node
/**
 * Configuration to bundle scripts for esbuild.
 */
import * as esbuild from "esbuild";

await esbuild.build({
  entryPoints: ["src/frontend/main.ts"],
  bundle: true,
  format: "esm",
  minify: process.env.NODE_ENV === "production",
  sourcemap: process.env.NODE_ENV !== "production",
  outfile: "src/atsphinx/mini18n/_static/atsphinx-mini18n.js",
  target: ["chrome58", "firefox57", "safari11", "edge16"],
});
