const isEnglish = document.documentElement.lang === 'en';
const themeButton = document.querySelector('.theme-toggle');
const colorScheme = window.matchMedia('(prefers-color-scheme: dark)');
function updateThemeButton() {
  const dark = document.documentElement.dataset.theme === 'dark';
  themeButton.setAttribute('aria-pressed', String(dark));
  themeButton.setAttribute('aria-label', isEnglish ? (dark ? 'Switch to light theme' : 'Switch to dark theme') : (dark ? '切换至浅色主题' : '切换至深色主题'));
  document.querySelector('meta[name="theme-color"]').content = dark ? '#191d1b' : '#f8f8f5';
}
themeButton.hidden = false;
updateThemeButton();
themeButton.addEventListener('click', () => {
  const next = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
  document.documentElement.dataset.theme = next;
  try { localStorage.setItem('marzovo-theme', next); } catch (_) { /* Session-only preference. */ }
  updateThemeButton();
});
colorScheme.addEventListener('change', (event) => {
  try { if (localStorage.getItem('marzovo-theme')) return; } catch (_) { return; }
  document.documentElement.dataset.theme = event.matches ? 'dark' : 'light';
  updateThemeButton();
});
const languageLink = document.querySelector('.language-toggle');
const languagePath = languageLink.getAttribute('href');
function keepSection() { languageLink.setAttribute('href', languagePath + location.hash); }
keepSection();
window.addEventListener('hashchange', keepSection);
const copyButton = document.querySelector('.copy-email');
const status = document.querySelector('#copy-status');
copyButton.hidden = false;
copyButton.addEventListener('click', async () => {
  try {
    await navigator.clipboard.writeText('13683217958@163.com');
    status.textContent = isEnglish ? 'Email copied. Looking forward to hearing from you!' : '邮箱已复制，期待你的来信！';
  } catch (_) {
    status.textContent = isEnglish ? 'Please select and copy: 13683217958@163.com' : '请手动选择并复制：13683217958@163.com';
  }
});
