import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Lectures',
  description:
    'Dokumentasi kuliah Program Studi Teknologi Rekayasa Perangkat Lunak, Politeknik Negeri Batam.',
  cleanUrls: true,

  themeConfig: {
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Pengantar', link: '/intro' },
      { text: 'V1', link: '/v1/' },
      { text: 'Lisensi', link: '/license' },
    ],

    sidebar: {
      '/': [
        {
          text: 'Global',
          items: [
            { text: 'Pengantar', link: '/intro' },
            { text: 'Format & Aturan', link: '/global/format/' },
            { text: 'Lisensi', link: '/license' },
          ],
        },
      ],
      '/v1/': [
        {
          text: 'V1 — Semester 1',
          items: [
            { text: 'Ikhtisar', link: '/v1/' },
            { text: 'Mata Kuliah', link: '/v1/courses/' },
            { text: 'Informasi', link: '/v1/information/' },
            { text: 'Tugas', link: '/v1/task/' },
          ],
        },
      ],
    },

    socialLinks: [{ icon: 'github', link: 'https://github.com/mroczect/lectures' }],

    search: { provider: 'local' },
    outline: { level: [2, 3] },
  },
})
