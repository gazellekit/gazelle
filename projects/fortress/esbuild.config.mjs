import * as esbuild from 'esbuild';

await esbuild.build({
  entryPoints: ['./src/Fortress.fs.ts'],
  outfile: './build/js/fortress.js',
  platform: 'node',
  format: 'esm',
  target: 'es2022',
  sourcemap: 'linked',
  bundle: true,
  minify: false
});

await esbuild.build({
  entryPoints: ['./src/Fortress.fs.ts'],
  outfile: './build/js/fortress.min.js',
  platform: 'browser',
  format: 'iife',
  globalName: 'Fortress',
  target: 'es2022',
  sourcemap: 'linked',
  bundle: true,
  minify: true
});
