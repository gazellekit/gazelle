import * as esbuild from 'esbuild';

await esbuild.build({
  entryPoints: ['./interop/JS.fs.js'],
  bundle: true,
  minify: true,
  sourcemap: false,
  target: 'es2022',
  outfile: 'fable_build/fortress.min.js',
  globalName: 'Fortress',
  format: 'iife'
});

await esbuild.build({
  entryPoints: ['./interop/JS.fs.js'],
  bundle: true,
  minify: false,
  sourcemap: false,
  target: 'es2022',
  outfile: 'fable_build/fortress.js',
  globalName: 'Fortress',
  format: 'iife'
});