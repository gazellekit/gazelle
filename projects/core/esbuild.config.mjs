import * as esbuild from 'esbuild';

await esbuild.build({
  entryPoints: ['./build/main.js'],
  bundle: true,
  minify: true,
  sourcemap: false,
  target: 'es2022',
  outfile: 'build/calcpad.min.js',
  globalName: 'Calcpad',
  format: 'iife'
});

await esbuild.build({
  entryPoints: ['./build/main.js'],
  bundle: true,
  minify: false,
  sourcemap: false,
  target: 'es2022',
  outfile: 'build/calcpad.js',
  globalName: 'Calcpad',
  format: 'iife'
});