import * as esbuild from 'esbuild';

await esbuild.build({
  entryPoints: ['./Core.fs.ts'],
  outfile: './build/js/core.js',
  platform: 'node',
  format: 'esm',
  target: 'es2022',
  sourcemap: 'linked',
  bundle: true,
  minify: false
});

await esbuild.build({
  entryPoints: ['./Core.fs.ts'],
  outfile: './build/js/core.min.js',
  platform: 'browser',
  format: 'iife',
  globalName: 'Calcpad.Studio',
  target: 'es2022',
  sourcemap: 'linked',
  bundle: true,
  minify: true
});
