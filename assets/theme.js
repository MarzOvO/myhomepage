// Apply the saved preference before the first paint. Storage is optional.
try {
  const saved = localStorage.getItem('marzovo-theme');
  const dark = saved === 'dark' || (saved !== 'light' && window.matchMedia('(prefers-color-scheme: dark)').matches);
  document.documentElement.dataset.theme = dark ? 'dark' : 'light';
} catch (_) { /* The default light theme works without browser storage. */ }
