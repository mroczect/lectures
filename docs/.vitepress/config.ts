import { defineConfig } from 'vitepress';

export default defineConfig({
  lang: 'id-ID',
  title: 'Proyek Keren Saya',
  titleTemplate: ':title - Dokumentasi Lengkap',
  description: 'Dokumentasi super lengkap dengan VitePress 2.0',
  head: [
    ['link', { rel: 'icon', href: '/favicon.ico' }],
    ['link', { rel: 'preconnect', href: 'https://fonts.googleapis.com' }],
    ['link', { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' }],
    [
      'link',
      {
        href: 'https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap',
        rel: 'stylesheet',
      },
    ],
  ],

  cleanUrls: true,
  rewrites: {},

  srcDir: './docs',
  srcExclude: ['**/README.md', '**/TODO.md'],
  outDir: './docs/.vitepress/dist',
  cacheDir: './docs/.vitepress/cache',

  ignoreDeadLinks: [/^https?:\/\/localhost/, '/playground'],

  appearance: true,
  lastUpdated: true,

  markdown: {
    headers: true,

    theme: {
      light: 'github-light',
      dark: 'github-dark',
    },

    lineNumbers: true,

    anchor: {
      permalink: true,
    },
  },

  themeConfig: {
    logo: '/logo.svg',
    siteTitle: 'Proyek Keren',

    nav: [
      { text: 'Home', link: '/' },
      { text: 'Guide', link: '/guide/' },
      { text: 'Reference', link: '/reference/' },
      {
        text: 'Dropdown',
        items: [
          { text: 'Item A', link: '/item-a' },
          { text: 'Item B', link: '/item-b' },
        ],
      },
    ],

    sidebar: {
      '/guide/': [
        {
          text: 'Pendahuluan',
          items: [
            { text: 'Apa itu VitePress?', link: '/guide/what-is-vitepress' },
            { text: 'Memulai', link: '/guide/getting-started' },
            { text: 'Routing', link: '/guide/routing' },
          ],
        },
        {
          text: 'Menulis',
          items: [
            { text: 'Ekstensi Markdown', link: '/guide/markdown' },
            { text: 'Menangani Aset', link: '/guide/asset-handling' },
            { text: 'Frontmatter', link: '/guide/frontmatter' },
            { text: 'Menggunakan Vue di Markdown', link: '/guide/using-vue' },
            { text: 'Internasionalisasi', link: '/guide/i18n' },
          ],
        },
        {
          text: 'Kustomisasi',
          items: [
            { text: 'Tema Kustom', link: '/guide/custom-theme' },
            {
              text: 'Memperluas Tema Default',
              link: '/guide/extending-default-theme',
            },
            { text: 'Data Loading Build-Time', link: '/guide/data-loading' },
            { text: 'Kompatibilitas SSR', link: '/guide/ssr-compat' },
            { text: 'Menghubungkan ke CMS', link: '/guide/cms' },
          ],
        },
      ],
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/username/repo' },
      { icon: 'twitter', link: 'https://twitter.com/username' },
      { icon: 'discord', link: 'https://discord.gg/invite' },
    ],

    footer: {
      message: 'Dirilis di bawah Lisensi MIT.',
      copyright: 'Copyright © 2026-present Nama Anda',
    },

    editLink: {
      pattern: 'https://github.com/username/repo/edit/main/docs/:path',
      text: 'Edit halaman ini di GitHub',
    },

    lastUpdated: {
      text: 'Terakhir diperbarui',
      formatOptions: {
        dateStyle: 'short',
        timeStyle: 'medium',
      },
    },

    search: {
      provider: 'local',
      options: {
        translations: {
          button: {
            buttonText: 'Cari',
            buttonAriaLabel: 'Cari',
          },
          modal: {
            displayDetails: 'Tampilkan daftar lengkap',
            resetButtonTitle: 'Reset pencarian',
            backButtonTitle: 'Tutup pencarian',
            noResultsText: 'Tidak ada hasil',
            footer: {
              selectText: 'Pilih',
              selectKeyAriaLabel: 'Enter',
              navigateText: 'Navigasi',
              navigateUpKeyAriaLabel: 'Panah atas',
              navigateDownKeyAriaLabel: 'Panah bawah',
              closeText: 'Tutup',
              closeKeyAriaLabel: 'Esc',
            },
          },
        },
        miniSearch: {
          searchOptions: {
            fuzzy: 0.2,
            prefix: true,
            boost: { title: 4, text: 2, titles: 1 },
          },
        },
      },
    },

    docFooter: {
      prev: 'Sebelumnya',
      next: 'Berikutnya',
    },

    outline: {
      level: [2, 3],
      label: 'Di halaman ini',
    },
  },
});
