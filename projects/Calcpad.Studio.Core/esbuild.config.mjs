import * as esbuild from 'esbuild';

await esbuild.build({
  entryPoints: ['./Interop.fs.ts'],
  outfile: './build/js/interop.js',
  platform: 'node',
  format: 'esm',
  target: 'es2022',
  sourcemap: 'linked',
  bundle: true,
  minify: false
});

await esbuild.build({
  entryPoints: ['./Interop.fs.ts'],
  outfile: './build/js/interop.min.js',
  platform: 'browser',
  format: 'iife',
  globalName: 'Calcpad.Studio',
  target: 'es2022',
  sourcemap: 'linked',
  bundle: true,
  minify: true
});
