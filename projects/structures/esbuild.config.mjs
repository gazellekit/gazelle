import * as esbuild from 'esbuild';

await esbuild.build({
  entryPoints: ['./src/main.ts'],
  outfile: './build/structures.js',
  platform: 'node',
  format: 'esm',
  target: 'es2022',
  sourcemap: 'linked',
  bundle: true,
  minify: false
});

await esbuild.build({
  entryPoints: ['./src/main.ts'],
  outfile: './build/structures.min.js',
  platform: 'browser',
  format: 'iife',
  globalName: 'Structures',
  target: 'es2022',
  sourcemap: 'linked',
  bundle: true,
  minify: true
});

